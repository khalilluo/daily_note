全局变量早于main函数被初始化，在main函数后被调用析构函数。


单个参数的构造函数定义了从形参到该类型的一个隐式类型转换
CSample(int iNum)	// 构造函数
CSample s1(10);
**s1 = 20;		// 则先调用单参构造函数，实参为20创建一个临时对象。再调用copy-assignment赋值给s1**

CSample s2 = 100;	// 这里是初始化不是赋值

想要阻止隐式类型转换，可使用explicit修饰构造函数

在windows32位机上，空struct和class大小都是为1
类大小与成员函数、static成员无关

sizeof(数组名)则为整个数组在内存的大小，即元素大小*个数


友元不能传递，继承且是单向的

static成员不是类对象的一部分，不能在构造函数中初始化，应该在类定义外部初始化。
**static成员函数不能声明为const和virtual** 注意是成员函数而已

**使用static变量的函数一般是不可重入的，也不是线程安全的**
不建议在头文件中定义static
static在函数或者全局只对当前文件下可见？
对函数而言，static的作用仅限于隐藏。对变量而言，因为保持在bss区域，如果不初始化则为默认值。且可以保持局部变量的值
static全局变量只在定义的文件中可用，
bbs：未初始化静态局部变量区。data：初始化的静态局部变量区

类的static数据成员保存在全局（静态）区
static成员函数不能被声明为const、virtual和volatile

在单例模式中，可以利用全局变量优先初始化的特性，将static成员变量在全局中就做好初始化。这样不加锁的情况下依然可以保证线程安全




私有继承和保护继承在类定义内部不影响访问权限，即仍可以访问protect和public成员。但继承类对象不能访问类的所有成员，同理
public继承->接口继承、、、、private和protect继承->实现继承。因为只有public是把基类对象的方法对外了
在public继承下，derived的对象，指针和引用都可以赋值给base，此时发生了隐式类型转换。反过来是不合法的
而将derived对象给base对象会造成对象切割，即derived的成员丢失
在private和protect继承下，derived对象的指针不可以自动转换为base指针。reinterpret_cast<T>方法可以转换指针但不安全，而对象就不能转换类型

base指针可以强制转换为derived指针，static_cast和dynamic_cast，不安全。而base对象则不能转换为derived对象

```c++
template<typename T> class CMakeFinal
{
	friend T;
private:
	CMakeFinal(){}
	~CMakeFinal(){}
};

CFinalClass : virtual public CMakeFinal<CFinalClass>
{
public:
	CFinalClass(){}
	~CFinalClass(){}
};
```

则CFinalClass是不可继承的，注意是虚继承。

友元关系不能被继承



```cpp
int *pia = new int[10]; // 10个未初始化int
int *pia2 = new int[10](); // 10个值初始化为0的int

unsigned char *p1; 
unsigned long *p2; 
p1=(unsigned char *)0x801000; 
p2=(unsigned long *)0x810000; 

/*
解析：p1指向字符型，一次移动一个字符型，1个字节；p1+5后移5个字节，16进制表示为5；

     p2指向长整型，一次移动一个长整型，4个字节，p2+5后移20字节，16进制表示为14。

 #char每次移动1个字节；short移动2个字节 ；int , long ,float移动4个字节 ；double移动8个字节
 */
```

