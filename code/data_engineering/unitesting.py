# Testing is a crucial part of programming to ensure code works as expected.
# The `pytest` module helps automate and simplify testing.

# To use pytest, you need to install it first. You can install it using pip:
# Run the following command in your terminal or command prompt:
# pip install pytest

import pytest

# Function to capitalize the first letter of a word
def capitalize_first_letter(word):
    """
    Capitalize the first letter of a given word.

    Args:
        word (str): The word to capitalize.

    Returns:
        str: The word with the first letter capitalized.
    """
    return word.capitalize()

# Test the function
result = capitalize_first_letter("hello")  # Should return "Hello"
print("Formatted word:", result)

# Unit tests using pytest
# Tests are typically defined in separate files inside a folder named `tests`.
# For example, you can create a file named `test_capitalize.py` inside the `tests` folder.
# The naming convention for test files is `test_*.py` or `*_test.py`.
# Below is an example of how to define test cases for the `capitalize_first_letter` function.
# Each test function should start with `test_` so that pytest can recognize it as a test.

# To run the tests, you can use the following methods:

# 1. Run the tests from the terminal using the pytest command:
#    pytest
#    (This will automatically discover and run all test files in the `tests` folder.)

# 2. Run a specific test file or test function:
#    pytest tests/test_capitalize.py
#    pytest tests/test_capitalize.py::test_capitalize_first_letter

# Example of test results:
# If all tests pass, you will see something like:
# ============================= test session starts =============================
# collected 4 items
# tests/test_capitalize.py ....                                           [100%]
# ============================== 4 passed in 0.02s =============================

# If a test fails, pytest will show detailed information about the failure,
# including the expected and actual results.
