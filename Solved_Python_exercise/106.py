""" A pangram is a sentence that uses every letter of the alphabet at least once.

Your program must indicate whether the given string is a pangram or not. """

s = input()
s = set(s)
if len(s) == 27:
    print('true')
else:
    print('false')