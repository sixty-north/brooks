"""Functions for modelling communications overhead."""

from math import factorial as fac

def overhead_proportion(num_personnel):
    """The proportion of time spent on communication overhead.

    Abdel-Hamid model.
    """
    if not (0 <= num_personnel <= 31):
        raise ValueError("Communication overhead proportion personnel "
                         "number {} out of range".format(num_personnel))
    return ((num_personnel / 4.082)**2) / 100.0


def partitioned_overhead_proportion(num_personnel, max_team_size):
    """The proportion of time spent on communication overhead.

    This model assumes the Abdel-Hamid model for intra-team communication, with
    an additional term of ten times that for inter-team communication.
    """
    num_partitions = num_personnel / min(max(1, num_personnel), max_team_size)
    num_personnel_per_partition = num_personnel / num_partitions
    intra_team_overhead = overhead_proportion(num_personnel_per_partition)
    inter_team_overhead = 10 * overhead_proportion(num_partitions)

    return intra_team_overhead + inter_team_overhead
