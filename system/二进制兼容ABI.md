## 什么是二进制兼容

所谓“二进制兼容性”指的就是在升级（也可能是 bug fix）库文件的时候，不必重新编译使用这个库的可执行文件或使用这个库的其他库文件，程序的功能不被破坏。



## C++ ABI 的主要内容：

- 函数参数传递的方式，比如 x86-64 用寄存器来传函数的前 4 个整数参数

- 虚函数的调用方式，通常是 vptr/vtbl 然后用 vtbl[offset] 来调用

- struct 和 class 的内存布局，通过偏移量来访问数据成员

- name mangling

- RTTI 和异常处理的实现（以下本文不考虑异常处理）

  

## 破坏兼容

- **给函数增加默认参数**，现有的可执行文件无法传这个额外的参数。

- 增加虚函数，会造成 vtbl 里的排列变化。（不要考虑“只在末尾增加”这种取巧行为，因为你的 class 可能已被继承。）

- 增加默认模板类型参数，比方说 Foo 改为 Foo >，这会改变 name mangling

- 改变 enum 的值，把 enum Color { Red = 3 }; 改为 Red = 4。这会造成错位。当然，由于 enum 自动排列取值，添加 enum 项也是不安全的，**除非是在末尾添加。**


给 class Bar 增加数据成员，造成 sizeof(Bar) 变大，以及内部数据成员的 offset 变化，这是不是安全的？通常不是安全的，但也有例外。

- 如果客户代码里有 new Bar，那么肯定不安全，因为 new 的字节数不够装下新 Bar。相反，如果 library 通过 factory 返回 Bar* （并通过 factory 来销毁对象）或者直接返回 shared_ptr，客户端不需要用到 sizeof(Bar)，那么可能是安全的。 同样的道理，直接定义 Bar bar; 对象（无论是函数局部对象还是作为其他 class 的成员）也有二进制兼容问题。

- 如果客户代码里有 Bar* pBar; pBar->memberA = xx;，那么肯定不安全，因为 memberA 的新 Bar 的偏移可能会变。相反，如果只通过成员函数来访问对象的数据成员，客户端不需要用到 data member 的 offsets，那么可能是安全的。

- 如果客户调用 pBar->setMemberA(xx); **而 Bar::setMemberA() 是个 inline function**，那么肯定不安全，因为偏移量已经被 inline 到客户的二进制代码里了。如果 setMemberA() 是 outline function，其实现位于 shared library 中，会随着 Bar 的更新而更新，那么可能是安全的

  

## 可能兼容

前面我说“不能轻易修改”，暗示有些改动多半是安全的，这里有一份白名单

只要库改动不影响现有的可执行文件的二进制代码的正确性，那么就是安全的，我们可以先部署新的库，让现有的二进制程序受益。

- 增加新的 class

- 增加 non-virtual 成员函数（因为普通函数是通过符号查找的？）

- 修改数据成员的名称，因为生产的二进制代码是按偏移量来访问的，当然，这会造成源码级的不兼容。

  

## 解决方案

#### 静态链接

#### 版本管理

对应1.1.x之间兼容，1.2.x不兼容

#### PIML

只暴露non-virtual接口，impl在接口文件中问指针，有一定的性能损失

[![qjSNeH.png](https://s1.ax1x.com/2022/04/06/qjSNeH.png)](https://imgtu.com/i/qjSNeH)

#### Qt

在类中用宏展开的方式定义私有数据类，用Q_D返回const private类的指针访问数据

