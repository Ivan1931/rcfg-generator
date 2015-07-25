class Symbol(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, that):
        self.symbol == that.symbol and self.__class__ == that.__class__
