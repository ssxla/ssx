mysql数据库 默认库          但mysql5.5之前没有这个库                 

base64 == 4的倍数 

16进制 0x          2进制 0b

get 传参有长度限制        post 传参没有长度限制

head头 查看信息

telnet明文传输 23

https ssl 心脏滴血

\u unicode编码

gb2312 标置%u 中文编码 宽字节注入 %df

utf-7 标志  +  -

utf-8 标志 &#x ；

任意文件遍历 iis（目录浏览的选项）  apache（httpd.conf）

phpstudy 能够通过默认密码登录mysql数据库

 

OPENVAS 

先启动服务并配置登录信息

systemctl restart openvas-manager.service

openvasmd --user = admin --new-password=123456 //更改密码

openvasmd --create-user=用户名 *//创建用户*

openvas

openvas-start //启动服务器

先添加目标

​	conflguration new target

添加扫描信息 scan management 

​			new task

php 文件包含漏洞

​	php://filter/read=convert.base64-encode/resource=php页面（down源码）