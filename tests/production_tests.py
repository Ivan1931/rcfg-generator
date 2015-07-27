from nose.tools import *
from rcfg.production import Production
from rcfg.variable import Variable

def creation_test():
    """We can create it!"""
    test_production = Production([], [], None, [])

def perform_valid_production_test():
    "Tests performing a valid production on a single valued string"
    permittedSymbol = [Variable("S")]
    production = Production(permittedSymbol, [Variable("S")], Variable("S"), [Variable("S"), Variable("S")])
    production_result = production.perform([Variable("S")])
    assert production_result == [Variable("S"), Variable("S")]
