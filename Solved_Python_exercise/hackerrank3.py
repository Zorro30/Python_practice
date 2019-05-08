'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, 
the red region denotes his house, where s is the start point, and t is the endpoint. 
The apple tree is to the left of his house, and the orange tree is to its right. 
You can assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.

Input Format

The first line contains two space-separated integers denoting the respective values of s and t. 
The second line contains two space-separated integers denoting the respective values of a and b. 
The third line contains two space-separated integers denoting the respective values of m and n. 
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a. 
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

eg:
input:
7 11
5 15
3 2
-2 2 1
5 -6

output:
1
1
'''

def countApplesAndOranges(s, t, a, b, apples, oranges):

    result_apple = map(lambda x: x+a,apples)
    result_orange = map(lambda x: x+b,oranges)
    fin_apple = [x for x in result_apple if x in range(s,t+1)]
    fin_org = [x for x in result_orange if x in range(s,t+1)]
    print(len(fin_apple))
    print(len(fin_org))

s,t = input().split(' ')
a,b = input().split(' ')
m,n = input().split(' ')
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(int(s), int(t), int(a), int(b), apples, oranges)