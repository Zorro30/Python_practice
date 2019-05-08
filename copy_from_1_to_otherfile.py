from sys import argv

script , from_file, to_file = argv

print ("copying from {} to {}".format(from_file,to_file))

input = open(from_file)
indata=input.read()

output = open (to_file,'w')
output.write(indata)

print ("ALL DONE")

output.close()
input.close()
