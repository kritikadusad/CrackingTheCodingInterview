"""
Palindrome Permutation: Given a string, write a function to check
if it is a permutation of a palindrome. A palindrome is a word or 
phrase that is the same forwards and backwards. A permutation is a 
rearrangement of letters. The palindrome does not need to be limited
to just dictionary words. 
Example:
>>> ispalindrome_permutation("Tact Coa")
True
"""


def ispalindrome_permutation(astring):

    astring_split = astring.lower().split(" ")
    astring_no_spaces = "".join(astring_split)
    astring_chars = {}
    for char in astring_no_spaces:
        if char in astring_chars:
            astring_chars[char] += 1
        astring_chars[char] = 1
    for count in astring_chars.values():
        odd_char = 0
        if len(astring_no_spaces) % 2 == 0:
            if count % 2 != 0:
                return False
        else:
            if count % 2 != 0:
                odd_char += 1
        if odd_char > 1:
            return False
    return True


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")
