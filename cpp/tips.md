dynamic_cast是使用typeid获取对象真正类型来转换，基类需包含虚函数

如果整数类型具有固定宽度需要从，利用类型<cstdint>报头，但请注意，它可选的实施方式中的标准品牌支持精确宽类型int8_t，int16_t，int32_t，int64_t，intptr_t，uint8_t，uint16_t，uint32_t，uint64_t和uintptr_t。

queue拿出front时使用右值，如果马上pop的话内容可能错乱

extern int x;   // declaration

explicit阻止构造函数隐式类型转换，主要在调用时体现

pass-by-value意味着“copy构造函数调用”

const返回值可以降低客户误操作的意外

const成员函数，使const对象调用方法成为可能。因为大部分函数是pass by reference-to-const

如果no-const函数返回值为内置类型，则返回reference是比较好的选择，否则对返回值改动不合法

mutable修饰的对象总是可变的
const成员函数不能调用no-const成员函数

如果const和no-const函数一样，代码大量重复：方法1封装一个private函数。方法2用 static_cast将对象转为const再用const_cast去除const属性

类成员变量只有在构造函数初始化列表中才是初始化，在构造函数体内是赋值而不是初始化。
而初始化列表里面的对象通常是调用copy构造函数，在函数体内是先调用default构造之后再调用copy-assignment
故：尽量使用初始化列表。  
class的成员变量总是以声明顺序被初始化，故在列表中的顺序并不重要

non-local static对象的初始化难以确定，最好的办法是不使用全局static对象、变量。改用local static，在函数第一次调用时此对象就会被第一次且唯一一次初始化，返回对象的reference。在singleton模式常用

default构造函数，copy构造函数，copy-assignment操作符和析构函数，如果自己没有定义则编译器会生成
内含reference成员变量，const成员变量和base class的copy-assignment是private的类，编译器都不能为其生成copy-assignment操作符

将成员函数声明为private且不实现，则任何人都无法调用这类函数。
继承uncopyable类，或者boost中的noncopyable类

如果基类析构没有被virtual修饰，通过基类指针删除的栈中的子类对象会造成“局部释放”，子类没有析构
如果类不想被继承，则析构函数不需要加virtual。因为带virtual的class会有一个virtual table pointer，这样类体积会增加
故：当成员函数带有virtual时，析构函数加virtual修饰是个好办法

在析构函数中，尽量将所有异常处理。否则使用容器时析构抛出两次异常会导致不可预见的情况出现
不得已的方法：退出或者吞下异常

在析构和构造函数中调用virtual函数，并不会调用子类的版本。故不要在这两个函数内调用virtual版本函数，包括它们调用的函数
构造顺序是base构造->derived构造，在base构造时子类可以视为不存在
在析构时顺序是derived->base，故derived析构后virtual函数上升到base版本

操作符=、+=、-=和*=返回一个reference to *this

在=操作符中处理自我赋值，注意成员变量可能是reference和pointer

copy函数（copy构造函数和copy-assignment）应该仔细复制每一个成员变量
继承时注意base class的复制，采用base::copy函数先对base处理。
添加成员变量时，copy函数也要同时更改

auto_ptr当通过copy构造函数和copy assignment操作符复制它们时，它们会变成null。复制的对象获取唯一拥有权


用类使用互斥量时，应该禁止类的复制。比如CSingleLock应该是禁止被复制的
可以利用shared_ptr的删除器，在类成员加入shared_ptr

