import funcy


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

    def can_perform(self, string):
        """Checks if the production can happen in the given context"""
        for forbidden in self.forbidding:
            if forbidden in string:
                return False
        for permitted in self.permitting:
            if permitted not in permitting:
                return False
        return True

    def perform(self, string):
        """
        Performs the production on an arbitrary string.
        Returns:
            * List of symbols (string) where the production has been performed
                if the context allows this production to happen (can_perform is true)
            * The origional string if the context does not allow productions
        """
        if self.can_perform(string):
            return funcy.mapcat(lambda sym: sym if sym == self.trigger_variable else transform_to, string)
        else:
            return string
