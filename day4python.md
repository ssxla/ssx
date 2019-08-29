acsii 表 可表示256种字符

中文为unicode编码 2个字节 utf-8可变长

encode（“编码”）编码

list 

 	list.append() 增加 

​	 list.pop 删除并拿出元素

​	 list.insert(位置，数据) 插入   

​	 "".join(list) []

元组 () 

​	定义后不能被改变

字典 {“1”：“2”} 键：值    键唯一

​	语法和列表差不多 

​	追加 字典名.["键"]=值 

​	.items（） 返回键值对应 

​	.value（）返回值 

set 只有键 集合的运算

​	set.add(key)

​	set.remove(key)

数字形和字符串形，元组是值传递

列表，字典是引用传递

*为变长的参数

**可选参数能写能不写参数

列表生成式【a+b for a in "abc" for b in "zxc"】 全排列

class 类名(objeck) （）里是父类 python objeck是所以类的父类

__init__构造函数

封装 属性（数据）只想被类里面的函数修改

—— 私有

多态子类能重写父类的方法 父类能指向子类的对象 接口

with open("路径",w+) as f:          w+是写文件 r+读文件

​	f.write("hello wo")

多线程能并发进行 包 threaing 

队列 先近先出 可以充当缓冲

res.encoding=res.apparent_encoding 将页面进行中文编码

.select('.类名 > ul >li >a') 遍历这个目录下的全部a标签   #id值   ‘标签名’

bs4 

​	将 a=BeautifulSoup(open('soup.html', encoding='utf8'), 'lxml') soup的网页打开 编码方式为utf-8 lxml为文件解析库，通过他能解析生成对象

​	a.a.attrs 能够获取到所有属性和值

​	a.a.attrs['href'] 获取指定的值

res.find_all("a") 找到所有的a

queue：

​	





optionparser





socket：

​	socket.socket(socket.AF-INET,sock.SOCK_)创建

​	connect() 尝试连接端口 传的是元组   开放的端口返回的是0

​	.send("\r\n").encode("utf-8")

​	.recv