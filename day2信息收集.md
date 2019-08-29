先明确目标 注意能扫描的地方

渗透深度 

src 漏洞盒子 

先知 reebuf 嘶吼 看雪 安全脉搏 安全网站 https://www.shentoushi.top/

wfuzz

shodan 

1. 信息收集 

   ​	1.1域名信息 子域名爆破 （phpinfo.me layer子域名挖掘机）

   ​	1.2who is 查询（工信部备案中心 （http://beian.miit.gov.cn/publish/query/indexFirst.action）站长之家） 反查能够知道其他资产 git下载 clone git上的url

   ​	1.3 谷歌搜索语法 site 资产名 （域名下的所有域名）

   ​			inurl php?id=1 (域名中包含php?id=1)

   ​			intitle 后台 （title中包含后台页面）

   ​			intext  <?php @eval([$_POST[""]);]> 文本中有一句话的页面    特殊的字段如（转到父目录） 阿帕奇 index.of

   ​			filetype (文件类型) 不支持使用MP3

   ​	1.4真实的IP kail下dig域名获取为ip，cdn 域名的节点页面加载的更快 cdn绕过找一个偏站（子域名）让目标站给我发送一个邮件查看邮件原文可以看到邮件来源的ip地址 对这个站进行dig就能知道主站的ip 

   ​	1.5 namp -T 4 精确并且快 主机发现

   ​		namp -v -Pn -sS -T4 -p1-65535 ip -oN ./名字.txt > out.out & &后台运行 将输出流打印到文件流中 jobs 看进程

   ​		namp 网址 --srcipt http-enum   收集web服务有用的信息

   ​	1.6WEBDAV 网站头 PUT COPY 

   ​	1.7web的开发的语言 

   ​	1.8web组件类型及版本（email oa cms 中间件 编辑器（fackeditor 论坛博客的文本编辑）开源框架 ）

   ​	1.9目录爆破 fuzz模糊测试   robots.txt .htaccess(Apache的配置文件上传绕过) web_ini  ./git源码泄漏  .swp vim不正常退出会生成备份文件

   ​	1.10旁站 

   ​	1.11waf wafwoof

   ​	mongdb	27017    weblogic 7001

   ​	iis asp 映射 .asa .cdx .cer .shtm .shtml .stn

   

   # .htaccess攻击

   ​	将不能解析php文件的文件夹能够解析php文件 一些配置/upload/image/目录下不能解析php文件，这时候是无法执行的，你可以直接上传一个，htaccess文件去从新写一条配置，这个时候就可以解析你定义的php了

   ​	把payload加入到.htaccess文件中

   ​			<FilesMatch "pino">    //将后缀名为pino的文件按php的形式解析
   ​			SetHandler application/x-httpd-php
   ​			</FilesMatch>

   ​	上传.htaccess文件使得已经上传一句话木马按照php的形式解析

   ​	

   # DjangoUEditor 1.9.143 富文本编辑器

   ssv-92826

   ​	能够在抓包时在url的位置上定义新的存储文件名能够覆盖上传的名字

   https://images.seebug.org/content/images/2017/03/9459B28D-49F1-41C9-9C44-CB751B766948.png

   正则表达式

   .   匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 
   * 匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*
     {n,m}   m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格

   * ket.*key，它将会匹配最长的以ket开始，以key结束的字符串。这个随便构造ket1454key和ket1key一样的效果所以随便构造。只需要ket开头key结尾。 
     .{4,7}点号匹配任意字符，.{4,7}就是匹配任意字符4到7次可以是7777，jdijfh等等，随意。 
     :\/.\/ 前面转意所以加\中间有个点好也是匹配任意字符 

     (.*key)/i 这个比较明显就是key结尾就是，前面随便写i表达式的结尾处的不区分大小写 i 标记指定不区分大小写。

     [[:punct:]] 任意的符号 \不翻译

     hongya{3}= hongyaaa

     

