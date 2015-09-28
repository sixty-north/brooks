from datetime import timedelta


def initial():
    seconds_per_day = timedelta(days=1).total_seconds()
    return dict(
        step_duration_seconds=seconds_per_day,
        num_function_points_requirements=500,
        num_function_points_developed=0,
        num_personnel=20,
        development_rate_function_points_per_person_per_second=0.1 / seconds_per_day
    )


def intervene(step_number, elapsed_time, state):
    """Intervene in the current step before the main simulation step is executed."""
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    return state.num_function_points_developed >= state.num_function_points_requirements


def complete(step_number, elapsed_time_seconds, state):
    return state
