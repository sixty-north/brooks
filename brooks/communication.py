"""Functions for modelling communications overhead."""

from math import exp

def no_overhead(num_personnel):
    return 0

def quadratic_overhead_proportion(num_personnel):
    """The proportion of time spent on communication overhead.

    Abdel-Hamid model.
    """
    if not (0 <= num_personnel < 31):
        raise ValueError("Communication overhead proportion personnel "
                         "number {} out of range".format(num_personnel))
    if num_personnel == 1:
        return 0
    return ((num_personnel / 4.082)**2) / 100.0


def partitioned_overhead_proportion(num_personnel, max_team_size):
    """The proportion of time spent on communication overhead.

    This model assumes the Abdel-Hamid model for intra-team communication, with
    an additional term of ten times that for inter-team communication.
    """
    num_partitions = num_personnel / min(max(1, num_personnel), max_team_size)
    num_personnel_per_partition = num_personnel / num_partitions
    intra_team_overhead = quadratic_overhead_proportion(num_personnel_per_partition)
    inter_team_overhead = 10 * quadratic_overhead_proportion(num_partitions)

    return intra_team_overhead + inter_team_overhead


def gompertz_overhead_proportion(num_personnel):
    """A Gompertz function which saturates at high numbers of personnel."""
    a = 1.0       # These values are adjusted to closely
    b = 6.5       # match the Abdel-Hamid curve in the
    c = 1 / 13    # range 0 to 30
    return (a * exp(-b * exp(-c * num_personnel))) - (a * exp(-b))
