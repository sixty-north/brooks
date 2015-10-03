"""Plotter.

Plot overlain time series for different runs of the Brooks' Law simulator.

Usage:
    plotter [--output=<output-file>] [--xsize=<inches> --ysize=<inches> --dpi=<dots-per-inch>] [--xmax=<time-axis-maximum>] [--ymax=<attribute-axis-maximum] [--start-color=<index>] [--time=<time-attribute>] <attribute> <tsv>...
    plotter (-h | --help)
    plotter --version

Arguments:
    attribute       The name of a model state attribute to be charted at each step.
    tsv             One or more TSV file paths or a single dash for stdin.

Options:
  --time=<time-attribute>          The name of the model state attribute used as the time axis. [default: elapsed_time]
  --output=<output-file>           Output file: [default: interactive]
  --xsize=<inches>                 The horizontal size of the plot in inches
  --ysize=<inches>                 The vertical size of the plot in inches
  --dpi=<dots-per-inch>            The number of dots per inch for plotting
  --xmax=<time-axis-maximum>       The maximum value on the time (x) axis
  --ymax=<attribute-axis-maximum>  The maximum value on the attribute (y) axis
  --start-color=<index>            The one-based index of the initial color cycle index. [default: 1]
  -h --help                        Show this screen.
  --version                        Show version
"""
import os
import sys

from functools import reduce

from docopt import docopt

import pandas
import seaborn  # Although apparently unused, this import has side-effects.
import matplotlib.pyplot as plt

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    arguments = docopt(__doc__, argv=argv, version="Plotter 0.5")

    time_attr = arguments['--time']
    attribute = arguments['<attribute>']
    tsv_paths = arguments['<tsv>']
    output = arguments['--output']

    run_frames = []
    for tsv_path in tsv_paths:
        run_name, _ = os.path.splitext(os.path.basename(tsv_path))
        loaded_frame = pandas.read_table(tsv_path, na_values=['None'])
        run_frame = loaded_frame[[time_attr, attribute]].copy()
        run_frame.rename(columns={attribute: run_name}, inplace=True)
        run_frames.append(run_frame)

    frame = reduce(lambda a, b: pandas.merge(a, b, on=time_attr, how='outer'), run_frames)
    frame.set_index(time_attr, inplace=True, verify_integrity=True)
    frame.fillna(0, inplace=True)

    if arguments['--xsize'] is not None:
        assert arguments['--ysize'] is not None
        xsize_inches = float(arguments['--xsize'])
        ysize_inches = float(arguments['--ysize'])
        dpi = float(arguments['--dpi'])
        plt.figure(figsize=(xsize_inches, ysize_inches), dpi=dpi)

    start_color_index = int(arguments['--start-color']) - 1
    color_cycle = plt.gca()._get_lines.color_cycle
    for i in range(start_color_index):
        next(color_cycle)

    frame.plot(ax=plt.gca())

    plt.ylim(ymin=0)
    if arguments['--xmax'] is None:
        xlim_min, xlim_max = plt.xlim()
        plt.xlim(xmax=(xlim_max - xlim_min) * 1.05)
    else:
        xmax = float(arguments['--xmax'])
        plt.xlim(xmax=xmax)

    if arguments['--ymax'] is not None:
        ymax = float(arguments['--ymax'])
        plt.ylim(ymax=ymax)

    plt.ylabel(attribute)

    if output == 'interactive':
        plt.show()
    else:
        savefig_args = {}
        if arguments['--dpi'] is not None:
            savefig_args['dpi'] = dpi

        plt.gcf().savefig(output, **savefig_args)

    return 0


if __name__ == '__main__':
    sys.exit(main())


