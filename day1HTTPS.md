https数据流向的分析

​	https是使用对称加密和非对称加密的传输过程 对称加密是使用AES的方式 非对称加密是使用证书加密的方式

​		证书是RAS和哈希算法相结合的方式 RSA是身份验证 哈希算法是检测数据包有没有被修改

​		浏览器会把厂商的公钥证书进行保存，会把服务端发来的公钥进行解码验证服务端是否为正确的服务端

​	首先进行三次握手的过程

​		![捕获](C:\Users\hasee\Desktop\捕获.PNG)

​	客户端浏览器对服务器端发送client hello包 生成了第一个随机值和证书 （第一个和第二个随机值在传输过程中是明文传输第三个随机值为加密传输）

![1](C:\Users\hasee\Desktop\1.PNG)

​	服务器端对客户端发送确认位回应数据包收到

![2](C:\Users\hasee\Desktop\2.PNG)

​	服务器端对客户端发送server hello包也会发送一个随机值和证书（第二个随机值）客户端对服务器端的请求进行了确认

![3](C:\Users\hasee\Desktop\3.PNG)



​	![22](C:\Users\hasee\Desktop\22.PNG)

第一步和第二步的client hello和server hello 使得客户端和服务器端对证书的版本和信息进行了统一和哈希验证成功，进行了单端的验证，下面进行数据的交互使用AES算法进行加密。第三个随机值进行公钥加密后对服务器端发送三个随机值会组合成一个AES的加密算法

![4](C:\Users\hasee\Desktop\4.PNG)

​	服务端向客户端发送发送信息通知以后使用协商好的算法加密

![5](C:\Users\hasee\Desktop\5.PNG)

​	对客户端的浏览器的证书进行导出![6](C:\Users\hasee\Desktop\6.PNG)

对wireshark进行证书的导入

![7](C:\Users\hasee\Desktop\7.PNG)

发现被加密的网页数据

![8](C:\Users\hasee\Desktop\8.PNG)







