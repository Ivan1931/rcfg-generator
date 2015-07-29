from nose.tools import *
from rcfg.production import Production
from rcfg.variable import Variable

def setup():
    global test_production
    test_production = Production([Variable("A"), Variable("B")], [Variable("C"), Variable("D")], Variable("S"), Variable("A"))
    return [test_production], {}

def creation_test():
    """We can create it!"""
    test_production = Production([], [], None, [])

def perform_valid_single_production_test():
    "Tests performing a valid production on a single valued string"
    permittedSymbol = [Variable("S")]
    production = Production(permitting=permittedSymbol, forbidding=[], trigger_variable=Variable("S"), transform_to=[Variable("S"), Variable("S")])
    string = [Variable("S")]
    production_result = production.perform(string)
    assert production_result == [[Variable("S"), Variable("S")]]

@with_setup(setup)
def perform_valid_multiple_production_test():
    """Tests what happens when we call a production on
    multiple variables in a string"""
    string = [Variable("A"), Variable("B"), Variable("S")]
    assert test_production.perform(string) == [[Variable("A"), Variable("B"), Variable("A")]]

@with_setup(setup)
def can_perform_forbidden_test():
    """
    Tests whether we can perform a production when we have a forbidden string.
    Suprise! The answer is no!
    """
    string = [Variable("A"), Variable("B"), Variable("C"), Variable("D"), Variable("S")]
    assert not test_production.can_perform(string)

@with_setup(setup)
def can_perform_without_permitted_test():
    """
    Tests whether we can perform a production when we don't have a permited var
    Suprise! The answer is no!
    """
    string = [Variable("A"), Variable("S")]
    assert not test_production.can_perform(string)
