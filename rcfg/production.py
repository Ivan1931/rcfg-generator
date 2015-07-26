class Production:
    """Deals with a production"""
    def __init__(self, permitting, forbidding, trigger_variable, transform_to):

        """Creates a new production
        Arguments:
        permitting -- List of permitting variables. All of these must be present
                      to allow a transition to occur.
        forbidding -- List of forbidding variables. None of these must appear
                      for a transition to occur.
        trigger_variable -- The left hand side variable of the transition
                            function. This variable gets substituted in all
                            in transitions
        transform_to -- Right hand side of the transition function. In a string
                        (represented as a list of symboles) all instances of a
                        trigger_variable will be replaced by
                        instances of transform_to.
        """

        self.permitting = permitting
        self.forbidding = forbidding
        self.trigger_variable = trigger_variable
        self.transform_to = transform_to


    def can_transform(self, str):
        """ Checks if production permitting and forbidding conditions are meet

        Arguments:
        str -- List of symboles that production is to be applied to
        """

        return true

    def trigger_variable_locations(self, str):
        """ Determines the possitions of all trigger_variables present in string

        Arguments:
        str -- List of symboles that production is to be applied to
        """

        return []

    def transform_symbols(self, str):
        """Performs a production on string

        Arguments:
        str -- List of symboles that production is to be applied to
        """

        self.str = str
        self.possition = trigger_variable_locations(str).[0]

        str = s[:possition-1] + transform_to + s[possition:]

        return str
