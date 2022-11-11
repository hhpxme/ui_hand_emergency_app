import os
import time

btn = []

for i in os.listdir('video'):
    btn.append([str(i), str(time.ctime(os.stat('video/' + i).st_ctime))])

print(btn[3][0])
