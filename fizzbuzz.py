def is_divisable(num, divisor):
    return (num % divisor == 0)

def is_divisable_by_three(num):
    return is_divisable(num, 3)

def is_divisable_by_five(num):
    return is_divisable(num, 5)

def is_divisable_by_fifteen(num):
    return is_divisable(num, 15)

def fizzbuzz(num):
    if is_divisable_by_fifteen(num):
        return 'FizzBuzz'
    if is_divisable_by_three(num):
        return 'Fizz'
    if is_divisable_by_five(num):
        return 'Buzz'
    return num
