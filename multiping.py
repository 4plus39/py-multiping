import os
import sys
import time
import keyboard
import threading


# 子執行緒的工作函數
def job(num, hostname):
    response = os.system("ping -i 1 " + hostname)
  
iplst = list()

for i in range(1,len(sys.argv)):
    iplst.append(sys.argv[i])

# 建立 n 個子執行緒
threads = []
for i in range(len(iplst)):
    threads.append(threading.Thread(target = job, args = (i, iplst[i])))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...


# 等待所有子執行緒結束
for i in range(len(iplst)):
    threads[i].join()

print("Done.")
