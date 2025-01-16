def is_prime(n):
    """
    Determine if a given integer is a prime number.

    :param n: An integer
    :return: True if n is a prime number, False otherwise
    """
    if n <= 1:
        return False  # Primes are greater than 1
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3
    # Check divisors up to the square root of n
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Test cases
print(f"Is 2 prime? {is_prime(2)}")  # True
print(f"Is 15 prime? {is_prime(15)}")  # False
print(f"Is 17 prime? {is_prime(17)}")  # True
print(f"Is 1 prime? {is_prime(1)}")  # False
print(f"Is 97 prime? {is_prime(97)}")  # True
print(f"Is -7 prime? {is_prime(-7)}")  # False
