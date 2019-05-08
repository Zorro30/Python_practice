'''
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.
For example, assume her scores for the season are represented in the array score= [12,24,10,24]. 
Scores are in the same order as the games played. She would tabulate her results as follows:

eg:
input:
9
10 5 20 20 4 5 2 25 1
output:
2 4  (max,min)
'''

def breakingRecords(scores):
    minimum = 0
    maximum = 0
    maxi = scores[0]
    mini = scores[0]
    for i in range(len(scores)-1):
        if scores[i] > scores[i+1]:
            if scores[i+1]<mini:
                minimum+=1
                mini = scores[i+1]
        elif scores[i] < scores[i+1]:
            if scores[i+1]>maxi:
                print(scores[i+1])
                maximum+=1 
                maxi = scores[i+1]
    print(maximum,minimum)


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)