""" In golf course, each hole has a "par", value which is the maximum number of swings that players should ideally need to clear the hole. 

Once a player has cleared the hole, the par is subtracted from the player's effective swing count, resulting in the player's score for that hole (i.e. 2 swings for a par 3 scores -1).

The final score for a player on a course is the total of his scores for each hole in the course.

Given a score card for a 18-hole course, your program must output the player's score.
Input
Line 1: 18 numbers separated by spaces, representing the pars for each hole.
Line 2: 18 numbers separated by spaces, representing the player's swing count for each hole.
Output
Line 1: the player's final score for the course. """

total = 0
par = [i for i in input().split()]
score = [i for i in input().split()]
for i in range(len(par)):
    total += (int(score[i]) - int(par[i]))
print(total)