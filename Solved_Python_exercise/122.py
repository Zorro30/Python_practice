'''
Python | Merge Python key values to list

Input = [{'gfg' : 2, 'is' : 4, 'best' : 6},{'it' : 5, 'is' : 7, 'best' : 8},{'CS' : 10}] 
Output = {‘is’: [4, 7], ‘it’: [5], ‘gfg’: [2], ‘CS’: [10], ‘best’: [6, 8]}
'''

test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},  
             {'it' : 5, 'is' : 7, 'best' : 8}, 
             {'CS' : 10}] 

#Brute force way
fin = {}
for dic in test_list:
    for key,val in dic.items():
        if key in fin.keys():
            fin[key].append(val)
        else:
            fin[key] = [val]
print(fin)

#Using setdefault()+loop
fin = {}
for dic in test_list:
    for key,val in dic.items():
        fin.setdefault(key,[]).append(val)
print(fin)