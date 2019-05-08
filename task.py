import random
import time

all = input ("Enter all the task you have separated with a ','!\n")
task= all.split(",")

print ("These are the task in your tasks list:")
print (task)

x=random.choice(task)
print ("The task '%s' is selected on Random! I hope you will complete and won't disappoint me!" %(x))

time.sleep(2)

print("I hope the task is in progress!!!")
#Since the task is in progress I would remove the task and print the left ones.
task.remove(x)

print("The remaining list of task is: %s"%(task))