from sys import argv
from file_read_backwards import FileReadBackwards

script, input_file = argv

def print_all(file):
    print (file.read())

def print_one(line_count, file): 
    print (line_count, file.readline())

def rewind(file):
    #line = file.seek(3,0)
    with FileReadBackwards('current_file',encoding='utf-8') as f:
        for line in f:
            print (line)

current_file = open(input_file)

'''print ("Whole file read!")
print_all(current_file)
'''
'''print ("Rewind!")'''
rewind(sample.txt)

'''print ("Only one line!")
line_count=1
print_one(line_count,current_file)
'''
