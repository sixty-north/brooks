"""Plotter.

Plot overlain time series for different runs of the Brooks' Law simulator.

Usage:
    plotter [--output=<output-file>] [--time=<time-attribute>] <attribute> <tsv>...
    plotter (-h | --help)
    plotter --version

Arguments:
    attribute       The name of a model state attribute to be charted at each step.
    tsv             One or more TSV file paths or a single dash for stdin.

Options:
  --time=<time-attribute>  The name of the model state attribute used as the time axis. [default: elapsed_time]
  --output=<output-file>   Output file: [default: stdout]
  -h --help                Show this screen.
  --version                Show version
"""
import os
import sys

from functools import reduce

from docopt import docopt

import pandas
import seaborn
import matplotlib.pyplot as plt

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    arguments = docopt(__doc__, argv=argv, version="Plotter 0.5")

    time_attr = arguments['--time']
    attribute = arguments['<attribute>']
    tsv_paths = arguments['<tsv>']

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

    frame.plot()

    plt.ylim(ymin=0)
    xlim_min, xlim_max = plt.xlim()
    plt.xlim(xmax=(xlim_max - xlim_min) * 1.05)
    plt.show()

    return 0


if __name__ == '__main__':
    sys.exit(main())


