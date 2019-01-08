"""
URLify: Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficient space at the end to hold 
the additional characters, and that you are given the 'true' length
of the string. 
Example:
>>> URLify("Mr John Smith       ", 13)
'Mr%20John%20Smith'
"""


def URLify(astring, length):
    """Given a string, URLify it by replacing
    spaces with '%20'."""
    astring_URL = ""
    for char in astring[:length]:
        if char == " ":
            astring_URL += "%20"
        else:
            astring_URL += char
    return astring_URL


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")
