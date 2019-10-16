'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

eg:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
'''

def swap_case(s):
    new = []
    for i in s:
        if i.isupper():
            new.append(i.lower())
        elif i.islower():
            new.append(i.upper())
        else:
            new.append(i)
    return ''.join(new)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)