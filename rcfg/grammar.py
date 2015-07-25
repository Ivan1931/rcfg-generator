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
