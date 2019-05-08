# in generators once the function yields, the function is paused and the control is transferred to the caller.
from time import sleep
def compute():
    for i in range(10):
        sleep(.5)
        yield i

for val in compute():
    print(val)