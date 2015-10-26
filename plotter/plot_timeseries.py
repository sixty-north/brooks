from functools import reduce

import pandas
import seaborn  # unused, but apparently has important side-effects
import matplotlib.pyplot as plt


def plot_timeseries(tsvs,
                    time_attr,
                    attribute,
                    start_color,
                    output,
                    xsize=None,
                    ysize=None,
                    dpi=None,
                    xmax=None,
                    ymax=None):
    """
    Args:
        tsvs: An iterable of (source, name) tuples where source is any valid
            value for pandas.read_table.
    """
    run_frames = []
    for tsv, run_name in tsvs:
        loaded_frame = pandas.read_table(tsv, na_values=['None'])
        run_frame = loaded_frame[[time_attr, attribute]].copy()
        run_frame.rename(columns={attribute: run_name}, inplace=True)
        run_frames.append(run_frame)

    frame = reduce(
        lambda a, b: pandas.merge(a, b, on=time_attr, how='outer'),
        run_frames)
    frame.set_index(time_attr, inplace=True, verify_integrity=True)
    frame.fillna(0, inplace=True)

    if xsize is not None:
        assert ysize is not None
        assert dpi is not None
        plt.figure(figsize=(xsize, ysize), dpi=dpi)

    start_color_index = start_color - 1
    color_cycle = plt.gca()._get_lines.color_cycle
    for i in range(start_color_index):
        next(color_cycle)

    frame.plot(ax=plt.gca())

    plt.ylim(ymin=0)
    if xmax is None:
        xlim_min, xlim_max = plt.xlim()
        plt.xlim(xmax=(xlim_max - xlim_min) * 1.05)
    else:
        plt.xlim(xmax=xmax)

    if ymax is not None:
        plt.ylim(ymax=ymax)

    plt.ylabel(attribute)

    if output == 'interactive':
        plt.show()
    else:
        savefig_args = {}
        if dpi is not None:
            savefig_args['dpi'] = dpi

        plt.gcf().savefig(output, **savefig_args)
