"""
String Compression: Implement a method to perform basic string
compression using the counts of repeated characters. If the 
compressed string would not become smaller than the original 
string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).
Example:
>>> string_compress("aabcccccaaa")
'a2b1c5a3'
"""


def string_compress(astring):
    compressed = ""
    count = 1
    for i, char in enumerate(astring[:-1]):
        if char == astring[i + 1]:
            count += 1
        else:
            compressed += astring[i] + str(count)
            count = 1
    compressed += astring[-1] + str(count)
    return compressed


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")


# cccccaaa
