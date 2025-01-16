def unique_sorted_letters(s):
    """
    Return a sorted list of all unique letters in the given string.

    :param s: Input string
    :return: Sorted list of unique letters
    """
    # Use a set to extract unique letters and sort the result
    unique_letters = sorted(set(char for char in s if char.isalpha()))
    return unique_letters

# Test cases
print(f"Unique sorted letters in 'cheese': {unique_sorted_letters('cheese')}")
print(f"Unique sorted letters in 'banana': {unique_sorted_letters('banana')}")
print(f"Unique sorted letters in 'Hello, World!': {unique_sorted_letters('Hello, World!')}")
print(f"Unique sorted letters in '12345': {unique_sorted_letters('12345')}")
