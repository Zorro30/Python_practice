import os

process = input('input the process you want to kill: ')
os.system('rm -rf kill.txt')
os.system('ps -eaf | grep {} >> kill.txt'.format(process))
with open('kill.txt','r') as f:
    content = f.readlines()

for i in content:
    val = i[5:11]
    os.system('kill -9 {}'.format(i))
    print('Killed process no. {}'.format(i))