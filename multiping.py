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

def arg_ip_list():
    lst = []
    if len(sys.argv) <= 2:
        print(" Please enter at least one IP address")
        sys.exit()

    for i in range(2,len(sys.argv)):
        ip = sys.argv[i]
        lst.append(ip)

    return lst

def arg_ip_2():
    if len(sys.argv) != 4:
        print(" Please enter TWO IP address")
        sys.exit()
    elif sys.argv[2] == sys.argv[3]:
        print(" Please enter TWO different IP address")
        sys.exit()        
    else:
        ip1 = sys.argv[2].split('.')
        ip2 = sys.argv[3].split('.')
        if ip1[0] == ip2[0] and ip1[1] == ip2[1]:
            if ip1[2] == ip2[2] and ip1[3] < ip2[3]:
                range_ip = int(ip2[3]) - int(ip1[3])
                return [ip1[0]+'.'+ip1[1]+'.'+ip1[2]+'.'+str(x) for x in range(int(ip1[3]), range_ip+2)]
            elif ip1[2] < ip2[2] and ip1[3] == ip2[3]:
                range_ip = int(ip2[2]) - int(ip1[2])
                return [ip1[0]+'.'+ip1[1]+'.'+str(x)+'.'+ip1[3] for x in range(int(ip1[2]), range_ip+2)]    
            else:
                print(" Unsupported format")
                sys.exit()
        else:
            print(" Unsupported format")
            sys.exit()

def ip_from_file():
    lst = []
    try:
        with open('ip_list.txt', 'r') as fo:
            for line in fo.readlines():
                lst.append(line)
        return lst
    except FileNotFoundError:
        print(" Can't find file 'ip_list.txt'")
        sys.exit()

def help():
    print("usage:  multiping <operation> [...]")
    print("operations:")
    print("    multiping [-h help]")
    print("    multiping [-i ip_addr] [ip_address1 ip_address2 ip_address3...]")
    print("    multiping [-s series]  [ip_address1 ip_address2]")
    print("    multiping [-f file]    [None. Default file is 'ip_list.txt']\n")


iplst = []
if len(sys.argv) == 1:
    print(" error: no operation specified (use -h for help)")
    sys.exit()
elif sys.argv[1] == '-i':
    iplst = arg_ip_list()
elif sys.argv[1] == '-c':
    iplst = arg_ip_2()
elif sys.argv[1] == '-f':
    iplst = ip_from_file()
elif sys.argv[1] == '-h':
    help()
    sys.exit()
else:
    print(" multiping: invalid option \'%s\'" %(sys.argv[1]))
    sys.exit()

# 建立 n 個子執行緒
threads = []
for i in range(len(iplst)):
    threads.append(threading.Thread(target = job, args = (i, iplst[i])))
    threads[i].start()

# 主執行緒繼續執行自己的工作
# ...
while True:
    print('------------------------------------------------------------')
    time.sleep(1)

    for i in range(len(iplst)):
        if threads[i].is_alive():
            break

        sys.exit()

# 等待所有子執行緒結束
for i in range(len(iplst)):
    threads[1].join()

print("Done.")

