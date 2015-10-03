import brooks.communication


def initial():
    """Configure the initial model state."""
    return dict(
        step_duration_days=1,
        num_function_points_requirements=500,
        num_function_points_developed=0,
        num_new_personnel=20,
        num_experienced_personnel=0,
        personnel_allocation_rate=0,
        personnel_assimilation_rate=0,
        assimilation_delay_days=20,
        nominal_productivity=0.1,
        new_productivity_weight=0.8,
        experienced_productivity_weight=1.2,
        training_overhead_proportion=0.25,
        communication_overhead_function=brooks.communication.quadratic_overhead_proportion,
        software_development_rate=None,
    )


def intervene(step_number, elapsed_time, state):
    """Intervene in the current step before the main simulation step is executed."""
    if elapsed_time == 110:
        state.num_new_personnel += 5
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    """Determine whether the simulation should end."""
    return state.num_function_points_developed >= state.num_function_points_requirements


def complete(step_number, elapsed_time_seconds, state):
    """Finalise the simulation state for the last recorded step."""
    state.software_development_rate = 0
    return state
