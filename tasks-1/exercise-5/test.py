import unittest
from code import calculate_factorial

def test_calculate_factorial():
    # Test case 1: Factorial of 0 should be 1
    assert calculate_factorial(0) == 1

    # Test case 2: Factorial of 1 should be 1
    assert calculate_factorial(1) == 1

    # Test case 3: Factorial of 5 should be 120
    assert calculate_factorial(5) == 120

    # Test case 4: Factorial of 10 should be 3628800
    assert calculate_factorial(10) == 3628800

    # Test case 5: Factorial of a negative number should return None
    assert calculate_factorial(-5) is None

    print("All tests passed!")

if __name__ == "__main__":
    test_calculate_factorial()