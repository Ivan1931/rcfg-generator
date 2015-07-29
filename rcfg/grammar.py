class Grammar(object):
    """Grammar represents a random context free string grammar"""
    def __init__(self, variables, terminals, start_symbol, productions):
        """
        Arguments:
        variables -- List of variables that represent the variable alphabet of the grammar
        terminals -- List of symbols that represent the terminal alphabet of the grammar
        start_symbol -- Starting variable in the grammar
        productions -- List of production objects that represent the production transition functions
        """
        self.variables = variables
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions

    def possible_productions(self, string):
        """Create list of possible productions

        Arguments:
        string -- list of symbols representing the string
        """
        for production in productions:
            if production.can_perform(string):
                possibleProductionList.append(production)

        return possibleProductionList

    def possible_strings(self, string):
        """Create list of possible future strings that have been produced using
        the productions obtained in possible_Production

        Arguments:
        string -- list of symbols representing the string
        """
        productions = self.possible_productions(string)
        possible = []
        for production in productions:
            for possible_string in production.perform(string):
                possible.append(possible_string)
        return possible
