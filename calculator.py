# https://github.com/Caadden/lab11-CC-MK
# My partner dropped this lab, so I tried to do both.

import math

def square_root(a):
    if a < 0:
        raise ValueError("Invalid values.")
    else:
        return math.sqrt(a)

def hypotenuse(a, b): # math.hypot(a, b) can have negative nums
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
        if a == 0:
            raise ZeroDivisionError("Division by Zero!")
        else:
            return b / a

def log(a, b): # use math library + raise ValueError
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid values.")
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b