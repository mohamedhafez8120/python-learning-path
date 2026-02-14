#!/usr/bin/env python3
"""
This module demonstrates how functions call each other and 
how data is returned and printed in Python.
"""

def get_title(first_name, last_name, job):
    """
    Takes three strings and glues them together into a title.
    We return the result so it can be used by other functions.
    """
    # We use f-strings here because they are easier to read than +
    title1 = f"{first_name} {last_name} the {job}"
    return title1

# Don't touch below this line

def test(first_name, last_name, job):
    """
    This function demonstrates the 'Hand-off'. It takes the 
    RETURN from get_title and then PRINTS it to the screen.
    """
    title = get_title(first_name, last_name, job)
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Job: {job}")
    print(f"Title: {title}")
    print("=====================================")

test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
