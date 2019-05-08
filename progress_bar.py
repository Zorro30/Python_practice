from progress.bar import Bar
import time

bar = Bar('Downloading', max=100)
for i in range(100):
    # Do some work
    bar.next()
    time.sleep(0.025)
bar.finish()