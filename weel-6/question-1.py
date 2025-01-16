def to_binary(n):
    """
    Convert a positive integer to its binary representation.

    :param n: A positive integer
    :return: A string representing the binary form of n
    """
    if n < 0:
        raise ValueError("The number must be a positive integer.")
    return bin(n)[2:]  # Remove the '0b' prefix

# Example usage
number = 42
print(f"Binary representation of {number}: {to_binary(number)}")
