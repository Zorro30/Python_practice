from file_read_backwards import FileReadBackwards

with FileReadBackwards('sample.txt', encoding='utf-8') as file:
    for line in file:
        print (line)