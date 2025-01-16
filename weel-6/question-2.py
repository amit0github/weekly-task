def find_factors(n):
    """
    Find all factors of an integer.

    :param n: An integer (positive or negative)
    :return: A list of factors of n
    """
    if n == 0:
        raise ValueError("Zero does not have factors.")
    n = abs(n)  # Consider absolute value for factors
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Avoid duplicate factors for perfect squares
                factors.append(n // i)
    return sorted(factors)

# Test cases
print(f"Factors of 28: {find_factors(28)}")
print(f"Factors of -15: {find_factors(-15)}")
print(f"Factors of 1: {find_factors(1)}")
