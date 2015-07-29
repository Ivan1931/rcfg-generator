class Symbol(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, that):
        return self.symbol == that.symbol and self.__class__ == that.__class__
