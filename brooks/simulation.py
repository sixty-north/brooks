class State:

    def __init__(
            self,
            step_duration_seconds):

        if step_duration_seconds <= 0:
            raise ValueError("Step duration {!r} must be positive".format(step_duration_seconds))
        self._step_duration_seconds = step_duration_seconds

    @property
    def step_duration_seconds(self):
        return self._step_duration_seconds

    def __repr__(self):
        return "{}(state_duration_seconds={})".format(
            self.__class__.__name__,
            self._step_duration_seconds
        )


def simulate(schedule):
    """

    Args:
        schedule: An object with the following methods:

             initial(state)
             step(state, input)
             complete(state)

    TODO: Consider making this a generator function

    """
    args = schedule.initial()
    state = State(**args)
    step_number = 0
    elapsed_time_seconds = 0
    while True:
        state = schedule.step(step_number, elapsed_time_seconds, state)
        if schedule.is_complete(step_number, elapsed_time_seconds, state):
            break
        step_number += 1
        elapsed_time_seconds += state.step_duration_seconds
    state = schedule.complete(state)
    print("number of steps: {}".format(step_number))
    print("elapsed time: {} s".format(elapsed_time_seconds))
    print(state)
