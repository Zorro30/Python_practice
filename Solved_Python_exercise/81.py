'''
Consider a staircase of size : 4
print:
   #
  ##
 ###
####
'''
def staircase(n):
    j = 1
    for i in range(n-1,-1,-1):
        print(' '*i+'#'*j)
        j +=1

staircase(6)