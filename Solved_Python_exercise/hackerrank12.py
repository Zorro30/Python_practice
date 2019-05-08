'''
input:
5 
CCEAEOSNDDEYUEHOT

C       C       E
 A     E O     S
  N   D   D   E
   Y U     E H
    O       T

output:
CANYOUDECODETHESE
'''

t = int(input())
arr = input()
n = len(arr) // t
for i in range(0,len(arr),4):
    print(arr[i])