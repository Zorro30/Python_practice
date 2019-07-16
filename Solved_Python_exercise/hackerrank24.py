'''
if the string s='abcac' and n=10, the substring we consider is abcacabcac,
the first 10 characters of her infinite string. 
There are 4 occurrences of a in the substring.

eg: 
Input: aba
10

output:
7
'''



def repeatedString(s,n):
    count = s.count('a')
    if n/len(s)==0:
        print("in if")
        val = count*n
        return val
    else:
        rem_str = n%len(s)
        s_count = s[:rem_str].count('a')
        val = (count*(n//len(s)))+s_count
        return val

s = input()

n = int(input())

result = repeatedString(s, n)
print(result)

