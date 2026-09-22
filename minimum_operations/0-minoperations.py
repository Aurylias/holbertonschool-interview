def minOperations(n):
    """Get to the given value with minimal operation"""
    if n <= 1:
        return 0
    total_operations = 0
    divisor = 2

    while divisor <= n:
        while n % divisor == 0:
            total_operations += divisor
            n //= divisor
        divisor += 1

    return total_operations
