def letters_in_either(word1, word2):
    """
    Return a sorted list of letters that appear in at least one of the two words.
    """
    return sorted(set(word1) | set(word2))

def letters_in_both(word1, word2):
    """
    Return a sorted list of letters that appear in both words.
    """
    return sorted(set(word1) & set(word2))

def letters_in_either_but_not_both(word1, word2):
    """
    Return a sorted list of letters that appear in either word, but not in both.
    """
    return sorted(set(word1) ^ set(word2))

# Test cases
word1 = "cheese"
word2 = "cheer"
print(f"Letters in either '{word1}' or '{word2}': {letters_in_either(word1, word2)}")
print(f"Letters in both '{word1}' and '{word2}': {letters_in_both(word1, word2)}")
print(f"Letters in either but not both '{word1}' and '{word2}': {letters_in_either_but_not_both(word1, word2)}")
