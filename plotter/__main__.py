"""Plotter.

Plot overlain time series for different runs of the Brooks' Law simulator.

Usage:
    plotter [--output=<output-file>] <attribute> <tsv>...

Arguments:
    tsv         One or more TSV file paths or a single dash for stdin.
    attribute   The name(s) of one or more a model state attribute(s) to be charted at each step.

Options:
  --output=<output-file>  Output file: [default: stdout]
  -h --help               Show this screen.
  --version               Show version
"""

import sys
from contextlib import contextmanager
from collections import OrderedDict

from docopt import docopt

import seaborn

def main(argv=None):
    if argv is None:
        argv = sys.argv

    arguments = docopt(__doc__, version="Plotter 0.5")

    tsv_paths = arguments['<tsv>']
    attributes = arguments['<attribute>']

    columns = read_tsvs(tsv_paths)

    ax = seaborn.tsplot(time=columns['elapsed_time'],
                        data=columns['software_development_rate'])

    seaborn.plt.show()

    return 0


def read_tsvs(tsv_paths):
    for tsv_path in tsv_paths:
        with open_in_stream(tsv_path) as tsv_file:
            line_reader = iter(tsv_file)
            try:
                header = next(line_reader).rstrip()
            except StopIteration:
                raise RuntimeError("File {!r} too short".format(tsv_path))
            headings = header.split('\t')
            columns = OrderedDict((heading, []) for heading in headings)
            for line in map(str.rstrip, line_reader):
                text_fields = line.split('\t')
                fields = [convert_field(text_field) for text_field in text_fields]
                for heading, field in zip(headings, fields):
                    columns[heading].append(field)
    return columns


def convert_field(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            if text == 'None':
                return 0.0
            return text

@contextmanager
def open_in_stream(filepath):
    if filepath == '-':
        yield sys.stdin
    else:
        f = open(filepath, 'rt')
        yield f
        f.close()

if __name__ == '__main__':
    sys.exit(main())


