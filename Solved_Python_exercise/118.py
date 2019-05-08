'''
convert this to 
{'China': {'Content' : ['china', 'country', 'south', 'east', 'asia', 'most', 'populous']}}

to this 
{'Title': 'China', 
'Content':['china', 'country', 'south', 'east', 'asia', 'most', 'populous']}
'''

present_dict = {'China': {'Content' : ['china', 'country', 'south', 'east', 'asia', 'most', 'populous']}}
new_dict = dict()

for i,k in present_dict.items():
    new_dict['Title'] = i
    new_dict[next(iter(k))] = next(iter(k.values()))

print(new_dict)