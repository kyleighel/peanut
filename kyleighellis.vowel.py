# kyleigh ellis
# 4th period


def vowel_counter(string):
    vowelcnt = 0
    vowels = ['a','e','i', 'o', 'u']
    for letter in string:
        if letter in vowels:
            vowelcnt += 1

    return vowelcnt


print(vowel_counter("vowels"))
            
