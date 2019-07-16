"""

Any person in the queue can bribe the person directly in front of them to swap 
positions. If two people swap positions, they still wear the same sticker 
denoting their original places in line. One person can bribe at most two others. 
For example, if n=8 and Person 5 bribes Person 4, the queue will look like this:1,2,3,5,4,6,7,8.


Print an integer denoting the minimum number of bribes needed to get the queue 
into its final state. Print Too chaotic if the state is invalid, 
i.e. it requires a person to have bribed more than  people.


eg: Input: 
2
5
2 1 5 3 4
5
2 5 1 3 4

Output:
3
Too chaotic

***Logic is to apply Simple bubble Sort implementation
"""

def minimumBribes(Q):

    swap = 0
    swaped = False
    for i,P in enumerate(Q):
        if P - (i+1) > 2:
            print("Too chaotic")
            return
    for i in range(len(Q)-1):
        for j in range(len(Q)-1):
            if Q[j] >Q[j+1]:
                Q[j],Q[j+1]=Q[j+1], Q[j]
                swap+=1
                swaped = True
        if swaped:
            swaped = False
        else:
            break
    return swap

n = int(input())

for i in range(n):
    q = int(input())
    series = list(map(int, input().rstrip().split()))
    print(minimumBribes(series))
