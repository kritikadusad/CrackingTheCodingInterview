def isunique(astring):
    """ Returns True if all characters in 
    given string are unique."""
    results = []
    for i in range(len(astring)):
        if astring[i] in astring[i + 1:]:
            return False
        results.append(True)
    return True


print(isunique("hello"))
print(isunique("hi my n"))
