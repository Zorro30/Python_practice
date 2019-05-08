# benifits of using yield, 
# No need of storage and less computation cost since we get the data one by one and not all data at one time.

from time import sleep

def compute(x):
    for i in range(x):
        yield(i)
        sleep(0.5)

for val in compute(10):
    print(val)