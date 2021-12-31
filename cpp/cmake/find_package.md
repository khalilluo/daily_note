find_package

![img](image/a1a133f7-7ba1-4cd5-b00f-5da21b92884c.png)



##### **Module模式查找顺序**

Module模式下是要查找到名为Find.cmake的文件。

先在CMAKE_MODULE_PATH变量对应的路径中查找。如果路径为空，或者路径中查找失败，则在cmake module directory（cmake安装时的Modules目录，比如/usr/local/share/cmake/Modules）查找

