"""
Description
----
Calculate standard errors and confidence intervals as a function of block length using
stationary bootstrap and extrapolate to infinite time.

Reference
----
Appendix from: Hess, B., Determining the shear viscosity of model liquids from molecular
dynamics simulations. J. Chem. Phys. 2002, 116 (1), 209-217.

Command line inputs
----
Flag name and type (string = str,  integer = int, floating point = flt).
If no type is given then the variable is logical and only the flag is needed.

:infile str:        Required. Name of input file.
:colnum int:        Required. Number of column in file with quantity to analyze with
                    column numbers starting from 0.
:outfile_prefix:    Required. Prefix for output file names.
:-eq str:           Optional. Equilibration time. Default = 0.0.
:-tu str:           Optional. Units for time. Default = ps (picoseconds).
:-vary_prefac:      Optional. Allow the prefactor to be varied during the fit,
                    otherwise sets the prefactor to 2*sigma^2/T.
:-sl flt:           Optional. Significance level (alpha) for confidence intervals. The
                    confidence interval bounds will be at the 100*alpha/2 and
                    100*(1 - alpha/2) percentiles. Default = 0.05.
:-mb int:           Optional. Minimum number of blocks to use. Default = 30.
:-nb int:           Optional. Number of bootstrap samples to use. Default = 100.
:-np int:           Optional. Number of processes to use for bootstrap calculation.
:-indir str:        Optional. Name of directory to read input from.
                    Default = current directory.
:-outdir str:       Optional. Name of directory to write output to.
                    Default = current directory.
"""


import argparse
import os

from arch.bootstrap import StationaryBootstrap
from joblib import Parallel, delayed, cpu_count
from lmfit import minimize, Parameters
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats


class ConfidenceInterval:

    def __init__(self, infile, colnum):
        '''
        Inputs
        ----
        :infile: Input file with time in first column and variable to analyze in second column.
                 The time step of the data is assumed to be constant.
        :colnum int: Required. Number of column in file with quantity to analyze with
                     column numbers starting from 0.
        '''

        self._infile = infile
        self._colnum = colnum

    def __call__(self, outfile_prefix=None, eqtime=0.0, skip=1, indir='.', time_unit='ps',
                 vary_prefactor=False, sig_level=0.05, block_size_number=100, min_blocks=30,
                 custom_func=None, nbootstrap=100, nprocs=1, outdir='.'):
        """
        Description
        ----
        Compute standard errors & confidence intervals as a function of block length,
        fit to a function, and extrapolate to infinite number of blocks.

        Inputs
        ----
        :outfile_prefix: Prefix for ouput file names. Defaults to infile without extension + '_'.
        :indir: Path to the input file.
        :eqtime: Equilibration time. Default = 0.0
        :skip: Frequency to keep data. Default = 1, keep all data.
        :time_units: Units of time in infile. Default = 'ps'
        :sig_level: Significance level for confidence intervals. Default = 0.05
        :min_blocks: Minimum number of blocks. Default = 30
        :nbootstrap: Number of bootstrap samples. Default = 100
        :nprocs: Number of processboes. Default = 1
        :outdir: Output directory. Default = '.'
        """

        self._indir = indir
        self._eqtime = eqtime
        self._skip = skip
        self._nbootstrap = nbootstrap
        self._custom_func = custom_func

        if outfile_prefix is None:
            # prefix for output files from infile
            outfile_prefix = '.'.join(self._infile.split('.')[:-1]) + '_'

        # open log file
        logfile = open(outdir + '/' + outfile_prefix + 'log.txt', 'w')

        # get data
        (time, self._data) = self._read_inputs()
        data_len = len(self._data)

        # total time & time step
        time_step = time[1] - time[0]
        time_total = time[-1] - time[0]
        logfile.write('Time step: ' + str(time_step) + ' ' + time_unit + '\n')
        logfile.write('Total time: ' + str(time_total) + ' ' + time_unit + '\n\n')

        # number of blocks
        nblocks = np.array(range(min_blocks, data_len+1), dtype=int)

        # block sizes in number of points
        block_sizes = (data_len/nblocks).astype(int)
        block_sizes = np.unique(block_sizes)
        nskip = max(int(np.floor(len(block_sizes)/block_size_number)), 1)
        block_sizes = np.unique(np.hstack((block_sizes[::nskip], block_sizes[-21:])))
        nblocks = (data_len/block_sizes).astype(int)

        # block sizes in time units
        block_lengths = time_step*block_sizes

        # stationary bootstrap for different block sizes
        result = np.array(Parallel(n_jobs=nprocs)
                          (delayed(self._bootstrap)(block_size) for block_size in block_sizes))

        nfunc = int(result.shape[1]/2)
        mn = result[:, :nfunc]
        se = result[:, nfunc:]

        # standard deviation, mean for all data
        sigma_data = se[0, :]*np.sqrt(data_len)
        mean_data = np.mean(mn, axis=0)

        logfile.write('Mean of data: ' + str(mean_data) + '\n')
        logfile.write('Standard deviation of data: ' + str(sigma_data) + '\n\n')

        # fitting to standard error
        unc_factor = stats.t.isf(sig_level/2.0, df=nbootstrap-1)
        wghts = np.ones(len(block_lengths))  # All weights equal
        params = Parameters()

        for ifunc in range(nfunc):

            prefactor_ini = 2.0*sigma_data[ifunc]**2.0/time_total
            if vary_prefactor:
                params.add('prefactor', value=prefactor_ini)
            else:
                params.add('prefactor', value=prefactor_ini, vary=False)

            fit_cnt = 0
            while True:

                tau1_ini = np.random.rand()*block_lengths[-1]
                alpha_max = np.mean(se[-3:])**2.0/(tau1_ini*prefactor_ini)
                alpha_ini = np.random.rand()*min(alpha_max, 1.0)
                tau2_ini = ((np.mean(se[-3:])**2.0/prefactor_ini) - alpha_ini*tau1_ini)/\
                           (1.0 - alpha_ini)

                params.add('alpha', value=alpha_ini, min=0.0, max=1.0)
                params.add('tau1', value=tau1_ini)
                params.add('tau2', value=tau2_ini)

                try:

                    fit = minimize(residual, params, args=(block_lengths, se[:, ifunc], wghts),
                                   method='nelder')
                    prefactor = fit.params['prefactor'].value
                    alpha = fit.params['alpha'].value
                    tau1 = fit.params['tau1'].value
                    tau2 = fit.params['tau2'].value
                    se_extrap = extrap(prefactor, alpha, tau1, tau2)
                    unc_extrap = unc_factor*se_extrap

                    break

                except ValueError:
                    fit_cnt += 1

                if fit_cnt > 1000:
                    tau1 = -1
                    tau2 = -1
                    break

            # fit with only one term (set alpha = 1) if tau1 or tau2 are negative or
            # greater than time_total
            if tau1 < 0 or tau2 < 0 or tau1 > time_total or tau2 > time_total:

                if tau1 > time_total or tau2 > time_total:
                    logfile.write('WARNING: Time constant > total time, \
                                   possibly insufficient data\n\n')

                params['alpha'].set(value=1.0, vary=False)

                fit_cnt = 0
                while True:

                    tau1_ini = np.random.rand()*block_lengths[-1]
                    params['tau1'].set(value=tau1_ini)

                    try:

                        fit = minimize(residual, params, args=(block_lengths, se[:, ifunc], wghts),
                                       method='nelder')
                        prefactor = fit.params['prefactor'].value
                        tau1 = fit.params['tau1'].value
                        se_extrap = extrap(prefactor, 1.0, tau1, 0.0)
                        unc_extrap = unc_factor*se_extrap

                        break

                    except ValueError:
                        fit_cnt += 1

                    if fit_cnt > 1000:

                        outdata = np.column_stack((block_lengths, se[:, ifunc]))

                        np.savetxt(\
                            os.path.join(outdir,
                                         outfile_prefix + 'block_fit_' + str(ifunc) + '.dat'),
                            outdata, header='Time (' + time_unit + '), Standard error')

                        se_extrap = np.mean(se[-3:])
                        unc_extrap = unc_factor*se_extrap
                        outdata = np.array([se_extrap, unc_extrap]).reshape(1, -1)
                        np.savetxt(os.path.join(outdir, outfile_prefix + \
                                                'block_error_extrapolation_' + str(ifunc) + '.dat'),
                                   outdata,
                                   header='Failed fit, use means of SE, unc values for 3 ' + \
                                                       'points with longest block lengths')

                        continue

            # Number of effective samples and correlation time where standard error has reached 99%
            # of its limitng value
            se_target = 0.99*se_extrap
            if se_target > se[-1, ifunc]:
                t0 = block_lengths[-1]
            else:
                ind = np.argmin(np.abs(se_target - se[:, ifunc]))
                t0 = block_lengths[ind]
            min_result = opt.minimize(se_diff, t0,
                                      args=(se_target, fit.params['prefactor'], fit.params['alpha'],
                                            fit.params['tau1'], fit.params['tau2']),
                                      method='Nelder-Mead')
            t_corr = min_result.x[0]
            n_eff = min_blocks*block_lengths[-1]/t_corr


            # Save residuals vs. number of blocks to file
            outdata = np.column_stack((nblocks, fit.residual))
            np.savetxt(\
                outdir + '/' + outfile_prefix + 'residuals_' + str(ifunc) + '.dat', outdata,
                header='No. of blocks | Residuals of standard error | Residuals of uncertainty')

            # save fit
            outdata = np.column_stack((block_lengths, se[:, ifunc], se[:, ifunc]-fit.residual))
            np.savetxt(outdir + '/' + outfile_prefix + 'block_error_fit_' + str(ifunc) + '.dat',
                       outdata,
                       header='Time (' + time_unit + '), Standard error, Fit to standard error')

            # Extrapolate to infinite time, save mean, se, uncertainty, parameters
            logfile.write("Extrapolated standard error: " + str(se_extrap) + '\n\n')

            outdata = np.column_stack((mean_data[ifunc], se_extrap, unc_extrap,
                                       fit.params['prefactor'], fit.params['alpha'],
                                       fit.params['tau1'], fit.params['tau2'], t_corr, n_eff))
            np.savetxt(\
                os.path.join(outdir,
                             outfile_prefix + 'block_error_extrapolation_' + str(ifunc) + '.dat'),
                outdata,
                header='Mean, Standard error, uncertainty, prefactor, alpha, ' + \
                       'tau1 (' + time_unit + '), tau2(' + time_unit + '), correlation time (' + \
                       time_unit + '), effective number of samples')

            logfile.close()

    def _read_inputs(self):
        '''
        Description
        ----
        Read in data, remove equilibration time, and split into time and data vectors.
        '''

        # read file: try numpy binary format, otherwise assume text (possibly xvg)
        try:
            data = np.load(self._indir + '/' + self._infile)
        except (OSError, ValueError):
            data = self._read_xvg()

        # throw away equilibration time
        data = data[data[:, 0] >= self._eqtime, :]

        # skip some data if skip > 1
        data = data[::self._skip, :]

        # split columns into time and data variables
        time = data[:, 0]
        data = data[:, self._colnum]

        return (time, data)

    def _read_xvg(self):
        """
        Description
        ----
        Read xvg file or any data file with no header or a header containing comment
        characters "#" or "@", discard header.
        """

        infile = self._indir + '/' + self._infile

        with open(infile, 'r') as fid:

            cnt = 0
            nskiprows = 0
            while nskiprows == 0:
                data = fid.readline()
                if data[0] != '#' and data[0] != '@':
                    nskiprows = cnt
                cnt = cnt + 1

        return np.loadtxt(infile, skiprows=nskiprows)


    def _bootstrap(self, block_size):
        """
        Description
        ----
        Stationary bootstrap for different block sizes

        Inputs
        ----
        :block_size: Number of points per block

        Outputs
        ----
        List containing mean, standard error
        """

        bs = StationaryBootstrap(block_size, self._data)

        try:
            bs_results = eval('bs.apply(' + self._custom_func + ', nbootstrap)')
        except TypeError:
            bs_results = bs.apply(np.mean, self._nbootstrap)

        mn = np.mean(bs_results, axis=0)
        se = np.std(bs_results, ddof=1, axis=0)

        return list(np.hstack((mn, se)))

def residual(params, t, se, wghts):
    """
    Description
    ----
    Compute residuals for fit.

    Inputs
    ----
    :params: Parameters for the model
    :se: Standard error as a function of block length

    Outputs
    ----
    :residuals: Residuals
    """

    prefactor = params['prefactor'].value
    alpha = params['alpha'].value
    tau1 = params['tau1'].value
    tau2 = params['tau2'].value

    model = se_func(t, prefactor, alpha, tau1, tau2)

    residuals = (se - model)*wghts

    return residuals

def se_func(t, prefactor, alpha, tau1, tau2):
    """
    Description
    ----
    Function for fitting standard error as a function of block length.

    Inputs
    ----
    :prefactor: Prefactor.
    :alpha: Fraction for tau1 term.
    :tau1: Time constant for first term.
    :tau2: Time constant for second term.

    Outputs
    ----
    Value of fit for various block lengths.
    """

    term1 = alpha*tau1*(1.0 + (tau1/t)*(np.exp(-t/tau1) - 1.0))
    term2 = (1.0 - alpha)*tau2*(1.0 + (tau2/t)*(np.exp(-t/tau2) - 1.0))
    return np.sqrt(prefactor*(term1 + term2))

def extrap(prefactor, alpha, tau1, tau2):
    """
    Description
    ----
    Extrapolate fitted function to infinite number of blocks

    Inputs
    ----
    :prefactor: Prefactor.
    :alpha: Fraction for tau1 term.
    :tau1: Time constant for first term.
    :tau2: Time constant for second term.

    Outputs
    ----
    Value at infinity
    """

    return np.sqrt(prefactor*(alpha*tau1 + (1.0-alpha)*tau2))

    # def _se_func_ssd(params, prefactor, t, se):
    #     alpha = params[0]
    #     tau1 = params[1]
    #     tau2 = params[2]
    #     return np.sum((self._se_func(prefactor, alpha, tau1, t, tau2) - se)**2.0)

def se_diff(t, se_target, prefactor, alpha, tau1, tau2):
    """
    Description
    ----
    Difference squared between the fitted function and a target standard error.
    Used to solve for block length at the target standard error.

    Inputs
    ----
    :t: Block length in time units.
    :se_target: Target standard error.
    :prefactor: Prefactor.
    :alpha: Fraction for tau1 term.
    :tau1: Time constant for first term.
    :tau2: Time constant for second term.

    Outputs
    ----
    Difference squared between the fitted function at t and se_target.
    """

    se = np.sqrt(prefactor*(alpha*tau1*(1.0 + (tau1/t)*(np.exp(-t/tau1) - 1.0)) + \
                            (1.0 - alpha)*tau2*(1.0 + (tau2/t)*(np.exp(-t/tau2) - 1.0))))
    return (se - se_target)**2.0

if __name__ == "__main__":

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('infile',
                        help='File with time in the first column and other quantities \
                        in subsequent columns.')
    PARSER.add_argument('colnum', type=int,
                        help='Column number in the file with the quantity to be \
                        analyzed. The first column is numbered 0.')
    PARSER.add_argument('-op', '--outprefix',
                        help='Prefix for output files. Default is the prefix of the \
                        input file.', default=None)
    PARSER.add_argument('-id', '--indir', default='.',
                        help='Directory input file is located in. Default is current \
                        directory')
    PARSER.add_argument('-od', '--outdir', default='.',
                        help='Directory to write data to. Default is current directory.')
    PARSER.add_argument('-tu', '--time_unit', default='ps',
                        help="String to specify time units. 'ns', 'ps', etc. Default \
                        is 'ps'.")
    PARSER.add_argument('-eq', '--eqtime', type=float, default=0.0,
                        help='Equilibration time in unit of input file. Default is 0.0')
    PARSER.add_argument('-sk', '--skip', type=int, default=1,
                        help='Only use every this many data points from the input file.')
    PARSER.add_argument('-vp', '--vary_prefac',
                        help='Vary the prefactor instead of constraining it to a \
                        constant value of 2 times the standard deviation of all data \
                        divided by the total time covered by the data. This is a flag.',
                        action='store_true')
    PARSER.add_argument('-sl', '--sig_level', type=float, default=0.05,
                        help='Significance level for computing confidence intervals. \
                        Default is 0.05.')
    PARSER.add_argument('-mb', '--min_blocks', type=int, default=30,
                        help='Minimum number of blocks. Default is 30.')
    PARSER.add_argument('-bsn', '--block_size_number', type=int, default=100,
                        help='Number of block sizes to consider. Default is 100.')
    PARSER.add_argument('-cf', '--custom_func', default=None,
                    help='Custom lambda function taking a single argument. ' + \
                         'This function contains the definition of the quantities ' + \
                         'which you wish to obtain the uncertainties for and should ' + \
                         'return a single value or a numpy row vector. ' + \
                         'Example -- lambda x: np.hstack((np.mean(x), np.percentile(x, 90))). ' + \
                         'If not specified, np.mean is used.')
    PARSER.add_argument('-nb', '--nbootstrap', type=int, default=100,
                        help='Number of bootstrap samples. Default is 100.')
    PARSER.add_argument('-np', '--nprocs', type=int, default=cpu_count(),
                        help='Number of processes to use for calculation. \
                        Default is the total number of available cores.')

    ARGS = PARSER.parse_args()

    get_confidence_interval = ConfidenceInterval(ARGS.infile, ARGS.colnum)
    get_confidence_interval(outfile_prefix=ARGS.outprefix, eqtime=ARGS.eqtime, skip=ARGS.skip,
                            indir=ARGS.indir, time_unit=ARGS.time_unit,
                            vary_prefactor=ARGS.vary_prefac, sig_level=ARGS.sig_level,
                            block_size_number=ARGS.block_size_number, min_blocks=ARGS.min_blocks,
                            custom_func=ARGS.custom_func, nbootstrap=ARGS.nbootstrap,
                            nprocs=ARGS.nprocs, outdir=ARGS.outdir)
