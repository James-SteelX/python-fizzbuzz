from fizzbuzz import *

def test_for_is_divisable():
    assert is_divisable(3, 3) == True

def test_for_number_divided_by_three():
    assert is_divisable_by_three(3) == True

def test_for_number_divided_by_five():
    assert is_divisable_by_five(5) == True

def test_for_number_divided_by_fifteen():
    assert is_divisable_by_fifteen(15) == True

def test_for_fizzbuzz_when_num_divisable_by_fifteen():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_for_fizz_when_num_divisable_by_three():
    assert fizzbuzz(3) == 'Fizz'

def test_for_buzz_when_num_divisable_by_five():
    assert fizzbuzz(5) == 'Buzz'

def test_for_returning_number_when_not_divisable():
    assert fizzbuzz(7) == 7

def test_for_returning_number_when_not_divisable():
    assert fizzbuzz(22) == 22
