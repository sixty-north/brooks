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
import os.path
import sys

from docopt import docopt

from plotter.plot_timeseries import plot_timeseries


def as_type(val, ctor):
    """Construct an object from a string if the string is not `None`, else
    just return `None`.

    Args:
      val: The string
      ctor: The constructor for the type to construct from `val`.

    Return: If `val` is not `None`, return `ctor(val)`. Otherwise `None`.
    """
    if val is None:
        return None
    return ctor(val)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    arguments = docopt(__doc__, argv=argv, version="Plotter 0.5")

    time_attr = arguments['--time']
    attribute = arguments['<attribute>']
    tsv_paths = arguments['<tsv>']
    output = arguments['--output']

    tsvs = ((tsv,
             os.path.splitext(
                 os.path.basename(tsv))[0])
            for tsv in tsv_paths)

    return plot_timeseries(
        tsvs,
        time_attr,
        attribute,
        int(arguments['--start-color']),
        output,
        as_type(arguments['--xsize'], float),
        as_type(arguments['--ysize'], float),
        as_type(arguments['--dpi'], float),
        as_type(arguments['--xmax'], float),
        as_type(arguments['--ymax'], float))


if __name__ == '__main__':
    sys.exit(main())
