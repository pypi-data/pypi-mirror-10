#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
import os
import subprocess
import sys
import getdist
from getdist import MCSamples, chains, IniFile

def runScript(fname):
    subprocess.Popen(['python', fname])

def main(args):
    if not os.path.isfile(args.ini_file):
        print('Parameter file does not exist ', args.ini_file)
        sys.exit()

    # Input parameters
    ini = IniFile(args.ini_file)

    # File root
    if args.chain_root is not None:
        in_root = args.chain_root
    else:
        in_root = ini.params['file_root']
    if in_root == '':
        print('Chain Root file name not given ', in_root)
        sys.exit()
    rootname = os.path.basename(in_root)

    ignorerows = ini.float('ignore_rows', 0.0)

    samples_are_chains = ini.bool('samples_are_chains', True)

    # Create instance of MCSamples
    mc = MCSamples(in_root, files_are_chains=samples_are_chains)

    mc.initParameters(ini)

    if ini.bool('adjust_priors', False) or ini.bool('map_params', False):
        print('To adjust priors or define new parameters, use a separate python script; see the python getdist docs for examples')
        sys.exit()

    plot_ext = ini.string('plot_ext', 'py')
    finish_run_command = ini.string('finish_run_command', '')

    no_plots = ini.bool('no_plots', False)
    plots_only = ini.bool('plots_only', False)
    no_tests = plots_only or ini.bool('no_tests', False)
    make_plots = ini.bool('make_plots', False)

    thin_factor = ini.int('thin_factor', 0)
    thin_cool = ini.float('thin_cool', 1.0)

    make_single_samples = ini.bool('make_single_samples', False)
    single_thin = ini.int('single_thin', 1)
    cool = ini.float('cool', 1.0)

    chain_exclude = ini.int_list('exclude_chain')

    shade_meanlikes = ini.bool('shade_meanlikes', False)
    plot_meanlikes = ini.bool('plot_meanlikes', False)

    out_dir = ini.string('out_dir')
    if out_dir:
        print('producing files in directory ', out_dir)
    mc.out_dir = out_dir

    out_root = ini.string('out_root')
    if out_root:
        rootname = out_root
        print('producing files with with root ', out_root)
    mc.rootname = rootname

    plot_data_dir = ini.string('plot_data_dir') or 'plot_data/'

    abs_plot_data_dir = plot_data_dir
    if not os.path.isdir(abs_plot_data_dir):
        os.mkdir(abs_plot_data_dir)
    mc.plot_data_dir = plot_data_dir

    rootdirname = os.path.join(out_dir, rootname); mc.rootdirname = rootdirname

    if 'do_minimal_1d_intervals' in ini.params:
        print('do_minimal_1d_intervals no longer used; set credible_interval_threshold instead')
        sys.exit()

    line = ini.string('PCA_params', '')
    if line.lower() == 'all':
        PCA_params = mc.paramNames.list()
    else:
        PCA_params = line.split()
    PCA_num = ini.int('PCA_num', len(PCA_params))
    if PCA_num != 0:
        if PCA_num < 2:
            print('Can only do PCA for 2 or more parameters')
            sys.exit()
        PCA_func = ini.string('PCA_func', '')
        # Characters representing functional mapping
        if PCA_func == '':
            PCA_func = ['N'] * PCA_num  # No mapping
        PCA_NormParam = ini.string('PCA_normparam', '') or None

    make_scatter_samples = ini.bool('make_scatter_samples', False)

    # ==============================================================================

    first_chain = ini.int('first_chain', 0)
    last_chain = ini.int('chain_num', -1)
    # -1 means keep reading until one not found

    # Chain files
    chain_files = chains.chainFiles(in_root, first_chain=first_chain, last_chain=last_chain, chain_exclude=chain_exclude)

    mc.loadChains(in_root, chain_files)

    mc.removeBurnFraction(ignorerows)
    mc.deleteFixedParams()
    mc.makeSingle()

    def filterPars(names):
        return [ name for name in names if mc.paramNames.parWithName(name) ]

    if cool != 1:
        print('Cooling chains by ', cool)
        mc.cool(cool)

    plotparams = []
    line = ini.string('plot_params', '')
    if line not in ['', '0']:
        plotparams = filterPars(line.split())

    line = ini.string('plot_2D_param', '')
    plot_2D_param = None
    if line.strip() and line != '0':
        plot_2D_param = line.strip()

    cust2DPlots = []
    if not plot_2D_param:
        # Use custom array of specific plots
        num_cust2D_plots = ini.int('plot_2D_num', 0)
        for i in range(1, num_cust2D_plots + 1):
            line = ini.string('plot' + str(i))
            pars = filterPars(line.split())
            if len(pars) != 2: raise Exception('plot_2D_num parameter not found, not varied, or not wrong number of parameters')
            cust2DPlots.append(pars)

    triangle_params = []
    triangle_plot = ini.bool('triangle_plot', False)
    if triangle_plot:
        line = ini.string('triangle_params')
        if line: triangle_params = filterPars(line.split())
        triangle_num = len(triangle_params)
        triangle_plot = triangle_num > 1

    num_3D_plots = ini.int('num_3D_plots', 0)
    plot_3D = []
    for ix in range(1, num_3D_plots + 1):
        line = ini.string('3D_plot' + str(ix))
        pars = filterPars(line.split())
        if len(pars) != 3: raise Exception('3D_plot parameter not found, not varied, or not wrong number of parameters')
        plot_3D.append(pars)

    mc.updateBaseStatistics()

    if not no_tests:
        mc.getConvergeTests(mc.converge_test_limit, writeDataToFile=True, feedback=True)

    mc.writeCovMatrix()
    mc.writeCorrelationMatrix()

    # Output thinned data if requested
    # Must do this with unsorted output
    if thin_factor != 0:
        thin_ix = mc.thin_indices(thin_factor)
        filename = rootdirname + '_thin.txt'
        mc.WriteThinData(filename, thin_ix, thin_cool)

    # Produce file of weight-1 samples if requested
    if (num_3D_plots and not make_single_samples or make_scatter_samples) and not no_plots:
        make_single_samples = True
        single_thin = max(1, int(round(mc.norm / mc.max_mult)) // mc.max_scatter_points)

    if make_single_samples:
        filename = os.path.join(plot_data_dir, rootname.strip() + '_single.txt')
        mc.makeSingleSamples(filename, single_thin)

    print(mc.getNumSampleSummaryText().strip())
    if mc.likeStats: print(mc.likeStats.likeSummary().strip())

    if PCA_num > 0 and not plots_only:
        mc.PCA(PCA_params, PCA_func, PCA_NormParam, writeDataToFile=True)

    # Do 1D bins
    mc.setDensitiesandMarge1D(writeDataToFile=not no_plots, meanlikes=plot_meanlikes)

    if not no_plots:
        # Output files for 1D plots
        print('Calculating plot data...')

        # Write paramNames file
        mc.getParamNames().saveAsText(os.path.join(plot_data_dir, rootname + '.paramnames'))
        mc.getBounds().saveToFile(os.path.join(plot_data_dir, rootname + '.bounds'))

        done2D = {}

        filename = rootdirname + '.' + plot_ext
        mc.WriteScriptPlots1D(filename, plotparams)
        if make_plots: runScript(filename)

        # Do 2D bins
        if plot_2D_param == 'corr':
            # In this case output the most correlated variable combinations
            print('...doing 2D plots for most correlated variables')
            cust2DPlots = mc.getCorrelatedVariable2DPlots()
            plot_2D_param = None
        elif plot_2D_param:
            mc.paramNames.parWithName(plot_2D_param, error=True)  # just check

        if cust2DPlots or plot_2D_param:
            print('...producing 2D plots')
            filename = rootdirname + '_2D.' + plot_ext
            done2D = mc.WriteScriptPlots2D(filename, plot_2D_param, cust2DPlots, plots_only, shade_meanlikes=shade_meanlikes)
            if make_plots: runScript(filename)

        if triangle_plot:
            # Add the off-diagonal 2D plots
            print('...producing triangle plot')
            filename = rootdirname + '_tri.' + plot_ext
            mc.WriteScriptPlotsTri(filename, triangle_params)
            for i, p2 in enumerate(triangle_params):
                for p1 in triangle_params[i + 1:]:
                    if not done2D.get((p1, p2)) and not plots_only:
                        mc.get2DDensityGridData(p1, p2, writeDataToFile=True, meanlikes=shade_meanlikes)
            if make_plots: runScript(filename)

        # Do 3D plots (i.e. 2D scatter plots with coloured points)
        if num_3D_plots:
            print('...producing ', num_3D_plots, '2D colored scatter plots')
            filename = rootdirname + '_3D.' + plot_ext
            mc.WriteScriptPlots3D(filename, plot_3D)
            if make_plots: runScript(filename)

    if not plots_only:
    # Write out stats marginalized
        mc.getMargeStats().saveAsText(rootdirname + '.margestats')

    # Limits from global likelihood
        if mc.loglikes is not None: mc.getLikeStats().saveAsText(rootdirname + '.likestats')

    # System command
    if finish_run_command:
        finish_run_command = finish_run_command.replace('%ROOTNAME%', rootname)
        finish_run_command = finish_run_command.replace('%PLOTDIR%', plot_data_dir)
        finish_run_command = finish_run_command.replace('%PLOTROOT%', os.path.join(plot_data_dir, rootname))
        os.system(finish_run_command)


if __name__ == '__main__':
    try:
        import argparse
    except ImportError:
        print('Make sure you are using python 2.7+')
        raise

    parser = argparse.ArgumentParser(description='GetDist sample analyser')
    parser.add_argument('ini_file', help='.ini file with analysis settings')
    parser.add_argument('chain_root', nargs='?', help='Root name of chain to analyse (e.g. chains/test)')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s ' + getdist.__version__)
    main(parser.parse_args())
