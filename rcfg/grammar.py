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

    def possible_Production(self, str):
        """Create list of possible productions

        Arguments:
        str -- list of symbols representing the string
        """

        self.str = str
        self.possibleProductionList = []

        for x in productions:
            if x.can_transform(str):
                possibleProductionList.append(x)

        return possibleProductionList

    def is_valid(self, str):
        """Create list of possible future strings that have been produced using
        the productions obtained in possible_Production

        Arguments:
        str -- list of symbols representing the string
        """

        self.str = str
        self.possibleProductionList = possible_Production(str)
        self.futureString = []

        for x in possibleProductionList:
            newProduction = x.transform_symbols(str)
            futureString.append(newProduction)

        return futureString
