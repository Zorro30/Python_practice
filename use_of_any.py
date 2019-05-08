'''
any prints True if it comes across any True condition in the loop, otherwise it prints False 
'''

j = input()
print (any(s.isalnum() for s in j))
print (any(s.isalpha() for s in j))
print (any(s.isdigit() for s in j))
print (any(s.islower() for s in j))
print (any(s.isupper() for s in j))