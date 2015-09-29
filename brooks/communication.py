def communication_overhead_proportion(num_personnel):
    """The proportion of time spent on communication overhead.

    Abdel-Hamid model.
    """
    if not (0 <= num_personnel <= 30):
        raise ValueError("Communication overhead proportion personnel number {} out of range".format(num_personnel))
    return ((num_personnel / 4.082)**2) / 100.0