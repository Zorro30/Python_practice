'''
Python | Merge list of tuple into list by joining the strings

Input = [('Hello', 'There'), ('Namastey', 'India'), ('Incredible', 'India')]
Output = ['Hello_There', 'Namastey_India', 'Incredible_India']

'''
Input = [('Hello', 'There'), ('Namastey', 'India'), ('Incredible', 'India')]

fin = []
for tup in Input:
    fin.append('-'.join(tup))

    #['-'.join(tup) for tup in Input] Can also be done using list compherension.
print(fin)