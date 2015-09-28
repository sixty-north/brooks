from datetime import timedelta


step_duration_seconds = timedelta(days=1)

def initial():
    return dict(
        step_duration_seconds=timedelta(days=1).total_seconds(),
    )


def step(step_number, elapsed_time, state):
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    return elapsed_time_seconds >= timedelta(days=500).total_seconds()


def complete(state):
    return state
