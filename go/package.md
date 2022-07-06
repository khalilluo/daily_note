Import with `.` :  
	

	import . "./pack1"

当使用`.`来做为包的别名时，你可以不通过包名来使用其中的项目。例如：`test := ReturnStr()`。

在当前的命名空间导入 pack1 包，一般是为了具有更好的测试效果。

Import with `_` : 

	import _ "./pack1/pack1"

pack1包只导入其副作用，也就是说，只执行它的init函数并初始化其中的全局变量。

