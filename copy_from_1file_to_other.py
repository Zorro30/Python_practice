from sys import argv
from os.path import exists

script, file1, file2 = argv

infile= open(file1)
data1= infile.read()

print ("Does the 2nd file exists? %r" %exists(file2))

outfile = open (file2,'w')
outfile.write(data1)

infile.close()
outfile.close()
