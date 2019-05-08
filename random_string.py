import string
import random

for i in random.sample(string.ascii_letters,6):
    print(i)
print("--------------------------------")
for i in random.choice(string.ascii_letters):
    print (i)