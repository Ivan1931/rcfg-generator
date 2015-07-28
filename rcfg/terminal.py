from symbol import Symbol


class Terminal(Symbol):
    def __init__(self, symbol):
        assert(0 < len(symbol))
        super(Symbol, self).__init__()
