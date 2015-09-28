
def initial():
    return dict(
        step_duration_days=1,
        num_function_points_requirements=500,
        num_function_points_developed=0,
        num_new_personnel=0,
        num_experienced_personnel=20,
        nominal_productivity=0.1
    )


def intervene(step_number, elapsed_time, state):
    """Intervene in the current step before the main simulation step is executed."""
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    return state.num_function_points_developed >= state.num_function_points_requirements


def complete(step_number, elapsed_time_seconds, state):
    return state
