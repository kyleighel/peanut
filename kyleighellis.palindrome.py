# kyleigh ellis
# 4th period

def palindrome(string):
    # alphabet charas
    newstr = " "
    for character in string:
        if character.isalpha():  # if letter
            newstr += character.lower()  # lowercase

    # check
    return newstr == newstr[::-1]


print(palindrome("racecar"))
