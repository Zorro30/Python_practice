'''
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, s=[2,2,1,3,2] . She wants to find segments summing to Ron's birth day, d=4 with a length equalling his birth month, m=2. In this case, there are two segments meeting her criteria:[2,2] and [1,3].

eg:
input:
5
1 2 1 3 2
3 2
output:
2
'''

def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count+=1
    print(count)


n = int(input().strip())
s = list(map(int, input().rstrip().split()))
d,m = map(int,input().rstrip().split())

result = birthday(s, d, m)