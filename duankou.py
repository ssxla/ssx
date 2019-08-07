import socket
import threading
from optparse import OptionParser
import re
import queue
RED = '\033[1;31m'
GREE = '\033[1;32m'
YLLO = '\033[1;33m'
que =queue.Queue()
USAGE = '''
Usage: python pscan.py 8.8.8.8
       python pscan.py 8.8.8.8 -p 21,80,8080
       python pscan.py 8.8.8.8 -p 21,80.8080 -n 50
'''

class Scanner(object):#定义一个scanner类
    def __init__(self,target,port,threadnum = 100,lis=None,url=None):#传了IP  端口  线程
        if target==None:
            self.target=None
        elif re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",target):#校验用户上传的ip
            self.target = target 
        else:
            print("[*] Ip Invalid !!")#否则提示报错
            exit()
        if lis != None:
            lujin="D:/qiye/code/"+lis
            with open(lujin,"r+") as file:
                wenjian=file.read().split(" ")
                flag=str(wenjian[1])
                if flag[0:1] > '0' and flag[0:1] <= '9':
                    self.lis = wenjian
                else:
                    ip = []
                    for i in wenjian:
                        ip.append(socket.gethostbyname(i))
                    self.lis=ip
        else:
            self.lis=None
        self.port = port
        self.threadnum = threadnum
        if url != None:
            ip=socket.gethostbyname(url)
            self.target=ip
        else:
            self.url = None

    def start(self):
        if self.port == 65535:
            for i in range(0,65536):
                que.put(i)
        else:
            for i in self.port:
                if int(i) < 0 or int(i) > 65535:
                    print('\n[-] 端口错误！请指定0~65535之间的端口')
                    exit()
                que.put(i)              
        try:           
            if self.target!= None:
                print("[*] 正在扫描%s"%self.target)                           
            thread_poll = []
            for i in range(0,int(self.threadnum)):
                th = threading.Thread(target=self.run,args=())   #添加分配线程挨个运行 将run函数加入
                thread_poll.append(th)
            for th in thread_poll:
                th.setDaemon(True)  #设置成子线程的主线程一起结束
                th.start()
            que.join()       #使主线程等待子线程结束
            print("[*] 完成扫描！！")

        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("[*] 用户自行退出扫描")

    def run(self):
        while not que.empty():
            port = int(que.get())
            if self.target == None:
                for i in self.lis:
                    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    sk.settimeout(0.5)
                    if sk.connect_ex((i,port)) == 0:
                        sk.send("Hello\r\n".encode("utf-8"))  #将Hello的数据包进行utf-8的编码发送给连接的ip
                        banner = sk.recv(2048).decode("utf-8")  #将返回的数据包放在2k的空间里进行utf-8解码
                        if banner:
                            print("[*] %s"%i,"开启的端口") 
                            print ("[*]%d%s-------------open\t"%(port,banner))   
                        else:
                            print("[*] %s"%i,"开启的端口") 
                            print ("[*]%d-------------open\t"%(port))
                        sk.close()
            else:
                if self.portScan(port):
                    banner = self.getSocketBanner(port)
                    if banner:
                        print ("[*]%d%s-------------open\t"%(port,banner))   
                    else:
                        print ("[*]%d-------------open\t"%(port))
            
            que.task_done()

    def portScan(self,port):
        try:
            sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sk.settimeout(0.5)
            if self.target != None:
                if sk.connect_ex((self.target,port)) == 0:
                    return True
                else:
                    return False           
        except Exception as e:
            print("portscan:error",e)
            pass
        except KeyboardInterrupt:
            print("[*] 用户自行退出扫描")
            exit()
        finally:
            sk.close()

    def getSocketBanner(self,port):
        try:
            sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #建立tcp连接
            sk.settimeout(0.5)      #如果连接超过0.5秒则认为超时
            if self.target != None:
                sk.connect((self.target,port)) #建立全连接
                sk.send("Hello\r\n".encode("utf-8"))  #将Hello的数据包进行utf-8的编码发送给连接的ip
                return sk.recv(2048).decode("utf-8")  #将返回的数据包放在2k的空间里进行utf-8解码
        except Exception as e:
            pass
        finally:
            sk.close()
            
parser = OptionParser()

parser.add_option('-p','--port',action="store",type="str",dest="port",help="All ports to be scanned default All port")
parser.add_option('-n','--num',action="store",type="int",dest="threadnum",help="Thread num default 100")
parser.add_option('-l','--list',action="store",type="str",dest="lis",help="Text")
parser.add_option('-u','--url',action="store",type="str",dest="url",help="The url")
#指定-p 扫指定 未指定全扫
(option , args) = parser.parse_args() #option 是在parser.add_option出现过的属性 args没有指定的属性
if option.port ==None and option.threadnum == None and len(args) == 1 :#如果用户只传了ip 没指定端口和线程
    scanner = Scanner(args[0],65535)#全端口扫描 做一个扫描类
    scanner.start()
elif option.port != None and option.threadnum == None and len(args) == 1:#只-p没-n
    port = option.port.split(',')#只按，分隔解析这个列表
    scanner = Scanner(args[0],port)#处理列表
    scanner.start()
elif option.port ==None and option.threadnum != None and len(args) == 1:#指定了线程
    scanner = Scanner(args[0],65535,option.threadnum)
    scanner.start()
elif option.port != None and option.threadnum != None and len(args) == 1:
    port = option.port.split(',')    
    scanner = Scanner(args[0],port,option.threadnum)
    scanner.start()
elif option.lis != None and option.url==None and option.port==None and len(args) == 0: #文本或url是否空
    scanner = Scanner(None,65535,lis=option.lis)
    scanner.start()
elif option.lis != None and option.url==None and option.port!=None and len(args) == 0: 
    port = option.port.split(',')
    scanner = Scanner(None,port,lis=option.lis)
    scanner.start()
elif option.lis == None and option.url!= None and option.port ==None and len(args) == 0:
    scanner =Scanner(None,65535,url=option.url)
    scanner.start()
elif option.lis == None and option.url!= None and option.port !=None and len(args) == 0:
    port = option.port.split(',')
    scanner =Scanner(None,port,url=option.url)
    scanner.start()

else:#以上都没有做到
    print(GREE+USAGE+GREE)#给用户提示说明
    parser.print_help()

