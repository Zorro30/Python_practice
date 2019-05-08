'''import time

def countdown(n):
    while n > 0:
        n = n - 1
        if n == 0:
            print ("Blast OFF!")
            exit(0)

countdown(500)'''

from datetime import datetime as dt
import time

start = dt.now()
time.sleep(10)
end = dt.now()
print ("Total time:{}".format(end - start))