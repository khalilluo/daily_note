<<<<<<< .mine
```CPP
#include <stdio.h>
#include <string.h>
void testArr(const char str[])
{
    printf("%lu %lu\n", sizeof(str), strlen(str));
}
int main(void)
{
    /*test 0*/
    char str[] = "hello";
    printf("test0 %lu %lu\n\n", sizeof(str), strlen(str)); //6 5

    /*test 1*/
    char str1[8] = "hello";
    printf("test1 %lu %lu\n\n", sizeof(str1), strlen(str1)); //8 5

    /**test 2*/
    char str2[] = {'h','e','l','l','o'};
    printf("test2 %lu %lu\n\n", sizeof(str2), strlen(str2)); //5 10

    /**test 3*/
    char *str3 = "hello";
    printf("test3 %lu %lu\n\n", sizeof(str3), strlen(str3)); //8 5

    /*test 4*/
    char str4[] = "hello";
    testArr(str4);//8 5

    /*test 5*/
    char str5[] = "hell\0o";
    printf("test5 %lu %lu\n", sizeof(str5), strlen(str5)); //7 4

    /*test 6*/
    char str6[10] = {0};
    printf("test6 %lu %lu\n\n", sizeof(str6), strlen(str6)); //10 0

    /*test 7*/
    char str7[5] = "hello";
    printf("test7 %lu %lu\n\n", sizeof(str7), strlen(str7)); //5 10

    /*test 8*/
    char str8[5] = {0};
    strncpy(str8,"hello",5);
    printf("%s\n",str8);//hellohello
    return 0;
}
```

特别注意观察test2和test7。
在解释这些测试之前，先复习一下sizeof，strlen以及数组的内容。

## sizeof

首先需要明确的是，sizeof是操作符，即它并不是函数，它的作用对象是数据类型，因此，它作用于变量时，也是对其类型进行操作。得到的结果是该数据类型占用空间大小，即size_t类型。
例如：

```
struct test
{
    int a;
    char b;
};
sizeof(int);//得到4
sizeof(test);//4字节对齐时，得到8
```

需要注意的是，它在计算数据类型占用空间大小时，会考虑字节对齐
另外**sizeof的时间复杂度是O(1)**。

## strlen

strlen是函数

```
size_t strlen(const char *s);
```

它用于计算字符串的长度。它的计算原则是：
从参数s所指向的内存开始往后计数，**直到内存中的内容是0（即’\0’）**为止。
例如：

```
#include<stdio.h>
#include<string.h>
int main()
{

    char *p = "hello";
    printf("%lu\n",strlen(p));//得到5
    return 0;
}
```

这里字符串hello的长度就是5，但是占用空间是多少呢？

```
sizeof("hello");//得到6
```

是6，而不是5。
注：strlen的时间复杂度为O（N）。

## 数组

关于数组，更多内容可以参考《[数组之谜](http://mp.weixin.qq.com/s?__biz=MzI2OTA3NTk3Ng==&mid=2649284000&idx=1&sn=55346d7560ba87f61320e46d13220122&chksm=f2f9aec7c58e27d104d88c93efc507368e8a051a8064041ebdedef4ac58f250d897096f72c85&scene=21#wechat_redirect)》。

### 字符串

字符串是以'\0'结尾的字符数组。

## 解析

实际上了解以上内容之后，很多问题迎刃而解。

#### test0

```
char str[] = "hello";
printf("test0 %lu %lu\n\n", sizeof(str), strlen(str)); //6 5
```

上面的初始化方法等价于下面的方式：

```
char str[] = {'h','e','l','l','o','\0'};
```

它实际上就是一个字符数组，只不过上面这种赋值方式会在末尾加上'\0'。

既然如此，那么用sizeof求得占用空间大小也就很明显了是6。而strlen是遇到'\0'，就结束，因此其求得长度为5。

#### test1

```
/*test 1*/
char str1[8] = "hello";
printf("test1 %lu %lu\n\n", sizeof(str1), strlen(str1)); //8 5
```

test1类似，只不过它占用空间是8，而长度仍然是5。

#### test2

```
/**test 2*/
char str2[] = {'h','e','l','l','o'};
printf("test2 %lu %lu\n\n", sizeof(str2), strlen(str2)); //5 10
```

sizeof求str2的大小很明显是5，而为啥那么strlen得到的是10呢？还记得strlen的原则吗，遇到'\0'则结束，但是'\0'在哪里？至少我在str2中没有看到，**所以你可能看到的结果是10，也可能是另外一个莫名其妙的值**，甚至可能导致程序崩溃。

#### test3

```
/**test 3*/
char *str3 = "hello";//最后有一个”隐形“的'\0'
printf("test3 %lu %lu\n\n", sizeof(str3), strlen(str3)); //8 5
```

为什么前者是8？很显然，**str3并不是一个数组，而是一个字符指针**，既然是指针类型，自然占着指针的大小，而64位程序中，它的大小就是你看到的8。后者还是从str3指向的地址开始，直到遇到'\0'，即得到长度5。

#### test4

```
/*test 4*/
char str4[] = "hello";
testArr(str4);//8 5
```

这在《[数组之谜](http://mp.weixin.qq.com/s?__biz=MzI2OTA3NTk3Ng==&mid=2649284000&idx=1&sn=55346d7560ba87f61320e46d13220122&chksm=f2f9aec7c58e27d104d88c93efc507368e8a051a8064041ebdedef4ac58f250d897096f72c85&scene=21#wechat_redirect)》中也提到过，**当数组作为参数时，实际上只是一个指针，所以用sizeof计算时，会得到8**。

#### test5

```
/*test 5*/
char str5[] = "hell\0o";
printf("test5 %lu %lu\n", sizeof(str5), strlen(str5)); //7 4
```

同理，str5的初始化等价于下面：

```
char str5[] = {'h','e'.'l','l','\0','o','\0'};
```

所以不用解释你也明白，**sizeof得到的结果是7。而strlen遇到第一个'\0'就停止继续计算了，因此得到4**。

#### test6

```
/*test 6*/
char str6[10] = {0};
printf("test6 %lu %lu\n\n", sizeof(str6), strlen(str6)); //10 0
```

相信这个也好理解，占用空间10，但是由于都是0，因此strlen得到长度为0。

#### test7

```
/*test 7*/
char str7[5] = "hello";
printf("test7 %lu %lu\n\n", sizeof(str7), strlen(str7)); //5 10
```

这也是非常危险的，**占用空间是5，它没有空间容纳最后的'\0'**，因此导致strlen计算的结果和test2一样，可能会是任意值。

#### test8

```
/*test 8*/
char str8[5] = {0};
strncpy(str8,"hello",5);
printf("%s\n",str8);//hellohello
```

这里在**实际编程中最容易遇到的问题之一**，数组大小为5，但是拷贝了5个字节大小的数据。如果你把它当成字符数组使用也没什么问题，但是由于它最后没有空间去容纳'\0'，因此你使用strlen，或者使用printf去打印的时候，可能发生难以预料的结果。

所以你可能会在你的项目代码中看到类似这样的写法，将字符数组的最后一个位置赋值为0：

```
str8[4] = '\0';
```

## 总结

文本关键点如下：

- sizeof计算类型占用空间大小，时间复杂度O(1)
- sizeof计算大小时会考虑字节对齐
- strlen计算字符串长度，时间复杂度O(N)
- strlen作用对象是字符串（以'\0'结尾）
- strlen遇到'\0'作罢，如果没有遇到，则不可预料
- 格外小心数组作为参数

另外注意下面两种方式hello存储的区域不一致：

```
char str[] = "hello";
char *str2 = "hello";//存储在数据区，只读
```

=======
```CPP
#include <stdio.h>
#include <string.h>
void testArr(const char str[])
{
    printf("%lu %lu\n", sizeof(str), strlen(str));
}
int main(void)
{
    /*test 0*/
    char str[] = "hello";
    printf("test0 %lu %lu\n\n", sizeof(str), strlen(str)); //6 5

    /*test 1*/
    char str1[8] = "hello";
    printf("test1 %lu %lu\n\n", sizeof(str1), strlen(str1)); //8 5

    /**test 2*/
    char str2[] = {'h','e','l','l','o'};
    printf("test2 %lu %lu\n\n", sizeof(str2), strlen(str2)); //5 10

    /**test 3*/
    char *str3 = "hello";
    printf("test3 %lu %lu\n\n", sizeof(str3), strlen(str3)); //8 5

    /*test 4*/
    char str4[] = "hello";
    testArr(str4);//8 5

    /*test 5*/
    char str5[] = "hell\0o";
    printf("test5 %lu %lu\n", sizeof(str5), strlen(str5)); //7 4

    /*test 6*/
    char str6[10] = {0};
    printf("test6 %lu %lu\n\n", sizeof(str6), strlen(str6)); //10 0

    /*test 7*/
    char str7[5] = "hello";
    printf("test7 %lu %lu\n\n", sizeof(str7), strlen(str7)); //5 10

    /*test 8*/
    char str8[5] = {0};
    strncpy(str8,"hello",5);
    printf("%s\n",str8);//hellohello
    return 0;
}
```

特别注意观察test2和test7。
在解释这些测试之前，先复习一下sizeof，strlen以及数组的内容。

## sizeof

首先需要明确的是，sizeof是操作符，即它并不是函数，它的作用对象是数据类型，因此，它作用于变量时，也是对其类型进行操作。得到的结果是该数据类型占用空间大小，即size_t类型。
例如：

```
struct test
{
    int a;
    char b;
};
sizeof(int);//得到4
sizeof(test);//4字节对齐时，得到8
```

需要注意的是，它在计算数据类型占用空间大小时，会考虑字节对齐
另外**sizeof的时间复杂度是O(1)**。

## strlen

strlen是函数

```
size_t strlen(const char *s);
```

它用于计算字符串的长度。它的计算原则是：
从参数s所指向的内存开始往后计数，**直到内存中的内容是0（即’\0’）**为止。
例如：

```
#include<stdio.h>
#include<string.h>
int main()
{

    char *p = "hello";
    printf("%lu\n",strlen(p));//得到5
    return 0;
}
```

这里字符串hello的长度就是5，但是占用空间是多少呢？

```
sizeof("hello");//得到6
```

是6，而不是5。
注：strlen的时间复杂度为O（N）。

## 数组

关于数组，更多内容可以参考《[数组之谜](http://mp.weixin.qq.com/s?__biz=MzI2OTA3NTk3Ng==&mid=2649284000&idx=1&sn=55346d7560ba87f61320e46d13220122&chksm=f2f9aec7c58e27d104d88c93efc507368e8a051a8064041ebdedef4ac58f250d897096f72c85&scene=21#wechat_redirect)》。

### 字符串

字符串是以'\0'结尾的字符数组。

## 解析

实际上了解以上内容之后，很多问题迎刃而解。

#### test0

```
char str[] = "hello";
printf("test0 %lu %lu\n\n", sizeof(str), strlen(str)); //6 5
```

上面的初始化方法等价于下面的方式：

```
char str[] = {'h','e','l','l','o','\0'};
```

它实际上就是一个字符数组，只不过上面这种赋值方式会在末尾加上'\0'。

既然如此，那么用sizeof求得占用空间大小也就很明显了是6。而strlen是遇到'\0'，就结束，因此其求得长度为5。

#### test1

```
/*test 1*/
char str1[8] = "hello";
printf("test1 %lu %lu\n\n", sizeof(str1), strlen(str1)); //8 5
```

test1类似，只不过它占用空间是8，而长度仍然是5。

#### test2

```
/**test 2*/
char str2[] = {'h','e','l','l','o'};
printf("test2 %lu %lu\n\n", sizeof(str2), strlen(str2)); //5 10
```

sizeof求str2的大小很明显是5，而为啥那么strlen得到的是10呢？还记得strlen的原则吗，遇到'\0'则结束，但是'\0'在哪里？至少我在str2中没有看到，**所以你可能看到的结果是10，也可能是另外一个莫名其妙的值**，甚至可能导致程序崩溃。

#### test3

```
/**test 3*/
char *str3 = "hello";//最后有一个”隐形“的'\0'
printf("test3 %lu %lu\n\n", sizeof(str3), strlen(str3)); //8 5
```

为什么前者是8？很显然，**str3并不是一个数组，而是一个字符指针**，既然是指针类型，自然占着指针的大小，而64位程序中，它的大小就是你看到的8。后者还是从str3指向的地址开始，直到遇到'\0'，即得到长度5。

#### test4

```
/*test 4*/
char str4[] = "hello";
testArr(str4);//8 5
```

这在《[数组之谜](http://mp.weixin.qq.com/s?__biz=MzI2OTA3NTk3Ng==&mid=2649284000&idx=1&sn=55346d7560ba87f61320e46d13220122&chksm=f2f9aec7c58e27d104d88c93efc507368e8a051a8064041ebdedef4ac58f250d897096f72c85&scene=21#wechat_redirect)》中也提到过，**当数组作为参数时，实际上只是一个指针，所以用sizeof计算时，会得到8**。

#### test5

```
/*test 5*/
char str5[] = "hell\0o";
printf("test5 %lu %lu\n", sizeof(str5), strlen(str5)); //7 4
```

同理，str5的初始化等价于下面：

```
char str5[] = {'h','e'.'l','l','\0','o','\0'};
```

所以不用解释你也明白，**sizeof得到的结果是7。而strlen遇到第一个'\0'就停止继续计算了，因此得到4**。

#### test6

```
/*test 6*/
char str6[10] = {0};
printf("test6 %lu %lu\n\n", sizeof(str6), strlen(str6)); //10 0
```

相信这个也好理解，占用空间10，但是由于都是0，因此strlen得到长度为0。

#### test7

```
/*test 7*/
char str7[5] = "hello";
printf("test7 %lu %lu\n\n", sizeof(str7), strlen(str7)); //5 10
```

这也是非常危险的，**占用空间是5，它没有空间容纳最后的'\0'**，因此导致strlen计算的结果和test2一样，可能会是任意值。

#### test8

```
/*test 8*/
char str8[5] = {0};
strncpy(str8,"hello",5);
printf("%s\n",str8);//hellohello
```

这里在**实际编程中最容易遇到的问题之一**，数组大小为5，但是拷贝了5个字节大小的数据。如果你把它当成字符数组使用也没什么问题，但是由于它最后没有空间去容纳'\0'，因此你使用strlen，或者使用printf去打印的时候，可能发生难以预料的结果。

所以你可能会在你的项目代码中看到类似这样的写法，将字符数组的最后一个位置赋值为0：

```
str8[4] = '\0';
```

## 总结

文本关键点如下：

- sizeof计算类型占用空间大小，时间复杂度O(1)
- sizeof计算大小时会考虑字节对齐
- strlen计算字符串长度，时间复杂度O(N)
- strlen作用对象是字符串（以'\0'结尾）
- strlen遇到'\0'作罢，如果没有遇到，则不可预料
- 格外小心数组作为参数

另外注意下面两种方式hello存储的区域不一致：

```
char str[] = "hello";
char *str2 = "hello";//存储在数据区，只读
```

>>>>>>> .theirs
