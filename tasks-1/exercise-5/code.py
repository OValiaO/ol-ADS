def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0:
        return 1  # 0! is defined as 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
