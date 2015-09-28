class State:
    """Aggegated instantaneous state of the simulation."""

    def __init__(
            self,
            step_duration_days,
            num_function_points_requirements,
            num_function_points_developed,
            num_new_personnel,
            num_experienced_personnel,
            personnel_allocation_rate,
            personnel_assimilation_rate,
            nominal_productivity,
            new_productivity_weight,
            experienced_productivity_weight):
        self.step_duration_days = step_duration_days
        self.num_function_points_requirements = num_function_points_requirements
        self.num_function_points_developed = num_function_points_developed
        self.num_new_personnel = num_new_personnel
        self.num_experienced_personnel = num_experienced_personnel
        self.personnel_allocation_rate = personnel_allocation_rate
        self.personnel_assimilation_rate = personnel_assimilation_rate
        self.nominal_productivity = nominal_productivity
        self.new_productivity_weight = new_productivity_weight
        self.experienced_productivity_weight = experienced_productivity_weight
        pass

    @property
    def step_duration_days(self):
        return self._step_duration_days

    @step_duration_days.setter
    def step_duration_days(self, value):
        if value <= 0:
            raise ValueError("Step duration {!r} days must be positive".format(value))
        self._step_duration_days = value

    @property
    def num_function_points_requirements(self):
        return self._num_function_points_requirements

    @num_function_points_requirements.setter
    def num_function_points_requirements(self, value):
        if value < 0:
            raise ValueError("Number of required function points {0} cannot be negative".format(value))
        self._num_function_points_requirements = value

    @property
    def num_function_points_developed(self):
        return self._num_function_points_developed

    @num_function_points_developed.setter
    def num_function_points_developed(self, value):
        if value < 0:
            raise ValueError("Number of developed function points {0} cannot be negative".format(value))
        self._num_function_points_developed = value

    @property
    def num_new_personnel(self):
        return self._num_new_personnel

    @num_new_personnel.setter
    def num_new_personnel(self, value):
        if value < 0:
            raise ValueError("Number of new personnel {0} cannot be negative".format(value))
        self._num_new_personnel = value

    @property
    def num_experienced_personnel(self):
        return self._num_experienced_personnel

    @num_experienced_personnel.setter
    def num_experienced_personnel(self, value):
        if value < 0:
            raise ValueError("Number of experienced personnel {0} cannot be negative".format(value))
        self._num_experienced_personnel = value

    @property
    def personnel_allocation_rate(self):
        return self._personnel_allocation_rate

    @personnel_allocation_rate.setter
    def personnel_allocation_rate(self, value):
        self._personnel_allocation_rate = value

    @property
    def personnel_assimilation_rate(self):
        return self._personnel_assimilation_rate

    @personnel_assimilation_rate.setter
    def personnel_assimilation_rate(self, value):
        if value < 0:
            raise ValueError("Personnel assimilation rate {0} people/day cannot be negative")
        self._personnel_assimilation_rate = value

    @property
    def nominal_productivity(self):
        """Nominal productivity in function points per person per second."""
        return self._nominal_productivity

    @nominal_productivity.setter
    def nominal_productivity(self, value):
        if value <= 0:
            raise ValueError("Nominal productivity {0} function-points/person/day must be positive".format(value))
        self._nominal_productivity = value

    @property
    def new_productivity_weight(self):
        """The weight of nominal productivity effected by new personnel."""
        return self._new_productivity_weight

    @new_productivity_weight.setter
    def new_productivity_weight(self, value):
        self._new_productivity_weight = value

    @property
    def experienced_productivity_weight(self):
        """The weight of nominal productivity effected by experienced personnel."""
        return self._experienced_productivity_weight

    @experienced_productivity_weight.setter
    def experienced_productivity_weight(self, value):
        self._experienced_productivity_weight = value

    def __repr__(self):
        return "{}("                                 \
            "step_duration_days={}, "                \
            "num_functions_points_requirements={}, " \
            "num_functions_points_developed={}, "    \
            "num_new_personnel={}, "                 \
            "num_experienced_personnel={}, "         \
            "nominal_productivity={}, "              \
            "new_productivity_weight={}, "           \
            "experienced_productivity_weight={}"     \
            ")".format(
                self.__class__.__name__,
                self._step_duration_days,
                self._num_function_points_requirements,
                self._num_function_points_developed,
                self._num_new_personnel,
                self._num_experienced_personnel,
                self._nominal_productivity,
                self._new_productivity_weight,
                self._experienced_productivity_weight
            )