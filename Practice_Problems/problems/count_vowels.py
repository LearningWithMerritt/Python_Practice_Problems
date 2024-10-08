'''
Write a Python function count_vowels(s) that counts the number of vowels in a given string s.

The function should:

Accept a string s.
Return the total count of vowels (a, e, i, o, u) in the string.


count_vowels("hello")           # Returns: 2
count_vowels("programming")     # Returns: 3
count_vowels("AEIOU")           # Returns: 5
'''




































# DO NOT EDIT THE CODE BELOW###################
if __name__ == "__main__":
    from utils.test_tools import run_tests

    try:
        run_tests(count_vowels, __file__)
    except NameError as e:
        print(f"{e}\nDid you name your function correctly?")
        exit()
    
    
###############################################