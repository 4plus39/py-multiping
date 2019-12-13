import os
import sys
import time
import threading

class Ping:
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):
        while self._running:
            pass


# 子執行緒的工作函數
def job(num, hostname):
    response = os.system("ping -i 1 " + hostname)

def input(iplist):
    for i in range(1,len(sys.argv)):
        ip = check(sys.argv[i])
        iplist.append(ip)

def check(str_ip):
    ip_list = str_ip.split('.')
    for ip in ip_list:
        if int(ip)<0 or int(ip) >255:
            print(" Detected the WRONG ip format,please try again.")
            exit()
    return str_ip
    
# 建立 n 個子執行緒
threads = []
iplist = []

input(iplist)

for i in range(len(iplist)):
    threads.append(threading.Thread(target = job, args = (i, iplist[i])))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...
while True:
    print('---------------------------------------------------------------')
    time.sleep(1)
    

    
    for i in range(len(iplist)):
        if threads[i].is_alive():
            break

        exit()

# 等待所有子執行緒結束
for i in range(len(iplist)):
    threads[i].join()

print("Done.")

