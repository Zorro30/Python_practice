'''
Python | Convert list to indexed tuple list

Input = [4, 5, 8, 9, 10] 
Output = [(0, 4), (1, 5), (2, 8), (3, 9), (4, 10)]
'''

Input = [4,5,8,9,10]

fin = []
for ind, val in enumerate(Input):
    fin.append((ind,val))
print(fin)


#Also does the same
print(list(enumerate(Input)))