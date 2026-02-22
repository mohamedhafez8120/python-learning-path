#!/usr/bin/env python3
"""
Module calculating sums of odd numbers.
"""

def sum_of_odd_numbers(end):
    """Return the sum of odd integers greater than 1 and less than ``end``.

    The sequence begins at 3 and proceeds by steps of 2 (3, 5, 7, ...).  The
    upper boundary ``end`` is exclusive; if ``end`` is 4 the only contributing
    term is 3.  Values of ``end`` less than or equal to 3 produce ``0``.
    """
    total = 0
    # start at 3 to omit 1; range stops before ``end``
    for i in range(3, end, 2):
        total += i
    return total


# --------------------------------------------------
# don't touch below this line - examples/tests follow
# --------------------------------------------------

def test(end):
    """Print a quick result so the behaviour can be inspected manually."""
    print(f"sum_of_odd_numbers(end={end}) = {sum_of_odd_numbers(end)}")


if __name__ == "__main__":
    # manual sanity checks  (1 and ``end`` excluded)
    test(4)   # expected 3  (only 3)
    test(6)   # expected 8  (3 + 5)
    test(50)  # previously hard‑coded example, now 3+5+...+49
