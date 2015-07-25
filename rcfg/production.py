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
                        all instances of a trigger_variable will be replaced by
                        instances of transform_to.
        """
        self.permitting = permitting
        self.forbidding = forbidding
        self.trigger_variable = trigger_variable
        self.transform_to = transform_to
