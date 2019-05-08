from sys import argv

script , filename = argv

txt = open (filename)

print ("Here is your file {}".format(filename))

print (txt.readline())

txt.close()