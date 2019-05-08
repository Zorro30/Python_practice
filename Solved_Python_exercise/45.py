'''
I have a chocolate bar of size m*n. I wish to split it into unit-sized pieces. What is the minimum split I have to do with the bar?
 _ _      _   _      _   _   _   _
|_|_| => |_| |_| => |_| |_| |_| |_|
|_|_|    |_| |_|
Example For a chocolate bar of size 2*2, after the first split, it becomes 2 bars of 1*2. It needs the second and third splits on each smaller bar to divide them into 4 units. Once a bar is separated, I cannot stack them up to split them together. I have to handle them separately.
Minimum split is 3

Input
2 2
Output
3
'''
m, n = [int(i) for i in input().split()]
print(m*n-1)