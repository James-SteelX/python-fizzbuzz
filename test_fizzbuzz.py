from fizzbuzz import *

def test_for_is_divisable():
    assert is_divisable(3, 3) == True

def test_for_number_divided_by_three():
    assert is_divisable_by_three(3) == True

def test_for_number_divided_by_five():
    assert is_divisable_by_five(5) == True

def test_for_number_divided_by_fifteen():
    assert is_divisable_by_fifteen(15) == True
