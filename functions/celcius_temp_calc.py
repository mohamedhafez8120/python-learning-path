#!/usr/bin/env python3
"""
This module provides functions to convert fahrenheit to celsius
"""

def to_celsius(f):
    """
Converts fahrenheit temp to celsius using formula
    """
    c = (5/9) * (f - 32)
    return (c)

## Don't touch below this line


def test(f):
    """
    Converts a temperature and prints a formatted message with 2 decimal places.
    """
    
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")

test(100)
test(88)
test(104)
test(112)
test(70)
