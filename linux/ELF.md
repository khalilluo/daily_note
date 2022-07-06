## ELF文件

目标文件再不同的系统或平台上具有不同的命名格式，在Unix和X86-64 Linux上称为ELF(Executable and Linkable Format, ELF)。

ELF文件格式提供了两种不同的视角，在汇编器和链接器看来，ELF文件是由Section Header Table描述的一系列Section的集合，而执行一个ELF文件时，在加载器（Loader）看来它是由Program Header Table描述的一系列Segment的集合

[![qXzZVA.jpg](https://s1.ax1x.com/2022/04/06/qXzZVA.jpg)](https://imgtu.com/i/qXzZVA)

左边是从汇编器和链接器的视角来看这个文件，开头的ELF Header描述了体系结构和操作系统等基本信息，并指出Section Header Table和Program Header Table在文件中的什么位置，Program Header Table在汇编和链接过程中没有用到，所以是可有可无的，Section Header Table中保存了所有Section的描述信息。右边是从加载器的视角来看这个文件，开头是ELF Header，Program Header Table中保存了所有Segment的描述信息，Section Header Table在加载过程中没有用到，所以是可有可无的。注意Section Header Table和Program Header Table并不是一定要位于文件开头和结尾的，其位置由ELF Header指出，上图这么画只是为了清晰。

我们在汇编程序中用.section声明的Section会成为目标文件中的Section，此外汇编器还会自动添加一些Section（比如符号表）。Segment是指在程序运行时加载到内存的具有相同属性的区域，由一个或多个Section组成，比如有两个Section都要求加载到内存后可读可写，就属于同一个Segment。有些Section只对汇编器和链接器有意义，在运行时用不到，也不需要加载到内存，那么就不属于任何Segment。

目标文件需要链接器做进一步处理，所以一定有Section Header Table；可执行文件需要加载运行，所以一定有Program Header Table；而共享库既要加载运行，又要在加载时做动态链接，所以既有Section Header Table又有Program Header Table。



## .dynsym .symtab

动态符号表 (.dynsym) 用来保存与动态链接相关的导入导出符号，不包括模块内部的符号。

而 .symtab 则保存所有符号，包括 .dynsym 中的符号。



## 获取信息

readelf file -h

objdump file -f