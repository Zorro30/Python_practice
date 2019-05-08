'''
Mario is marching to the castle to save the princess. In the last phase he has to jump over a number of pillars of different heights. When Mario jumps from a lower pillar to a higher pillar, he has to use High Jump. When he jumps to a pillar of lower or same height, he has to use Low Jump.
Your task is to find out how many High Jumps and Low Jumps Mario has to do.
'''

n = int(input())
l = list()
high_jump = 0
low_jump = 0
for i in input().split():
    l.append(i)
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        high_jump +=1
    elif l[i] >= l[i+1]:
        low_jump +=1
print(high_jump, low_jump)
