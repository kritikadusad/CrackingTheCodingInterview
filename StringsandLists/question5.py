"""
One Away: There are three types of edits that can be performed on strings: 
Insert a character, remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away.
Example:
>>> oneaway("pale", "ple")
True
>>> oneaway("pales", "pale")
True
>>> oneaway("bale", "pale")
True
>>> oneaway("pale", "bake")
False
"""


def oneaway(string1, string2):

    len_string1 = len(string1)
    len_string2 = len(string2)
    if abs(len_string1 - len_string2) <= 1:
        string1_dict = {}
        for char in string1:
            if char not in string1_dict:
                string1_dict[char] = 1
            string1_dict[char] += 1

        string2_dict = {}
        for char in string2:
            if char not in string2_dict:
                string2_dict[char] = 1
            string2_dict[char] += 1

        count = 0
        if len_string2 == len_string1:
            for char in string1_dict:
                try:
                    string1_dict[char] == string2_dict[char]
                except KeyError:
                    count += 1
            if count == 1:
                return True
        elif len_string2 > len_string1:
            for char in string2_dict:
                try:
                    string2_dict[char] == string1_dict[char]
                except KeyError:
                    count += 1
            if count == 0:
                return True
        else:
            for char in string2_dict:
                try:
                    string2_dict[char] == string1_dict[char]
                except KeyError:
                    count += 1
            if count == 0:
                return True
    return False


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
