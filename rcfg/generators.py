import funcy
import terminal
import random

def all_terminal(string):
    return funcy.all(lambda str: str.__class__ == terminal.Terminal)

def count_variables(string):
    return funcy.count_by(lambda sym: sym.__class__ == variable.Variable)

def randomly_walk_productions(grammar, max_depth, proportion_to_capture):
    """
    `randomly_walk_productions` randomly applies productions to all the possible
    generated strings. It starts at depth level zero and the grammars start symbol
    and walks until it reaches a certain depth. Returns all terminal strings that
    get generated

    grammar -- Grammar object
    max_depth -- maximum depth of the parse tree
    proportion_to_capture -- percentage of possible productions that should be
                             captured
    """
    strings = [grammar.start_symbol]
    for depth in range(0, max_depth):
        # find canditate strings - all possible strings that can be generated
        # by applying each production to each string in the list
        canditate_strings = funcy.flatten(funcy.map(lambda string: grammar.possible_strings(string), strings))
        random.shuffle(canditate_strings)
        # find number canditates to choose, convert to integer
        number_to_choose = int(proportion_to_capture * len(canditate_strings))
        strings = funcy.take(number_to_choose, canditate_strings)
    return filter(all_terminal, strings)
