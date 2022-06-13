## #

#运算符用于在预处理期将宏参数转换为字符串
在预处理期完成，因此只在宏定义中有效
编译器不知道#的转换作用
用法

```cpp
#define STRING(x)  #x
printf("%s\n",STRING(Hello World!));  // "Hello World!"
```

## ##
##运算符用于在预处理期粘连两个标识符
在预处理期完成，因此只在宏定义中有效
编译器不知道##的连接作用
用法

```cpp
#define CONNECT(a,b)  a##b
int CONNECT(a,1);//int a1;
a1 = 2;
```

## 注意事项

当宏参数是另一个宏的时候，需要注意的是凡宏定义里有用’#’或’##’的地方宏参数是不会再展开。即， 只有当前宏生效, 参数里的宏！不！会！生！效 ！！！！

- **举例**

```cpp
#define A          (2)
#define STR(s)     #s
#define CONS(a,b)  int(a##e##b)
printf("int max: %s\n",  STR(INT_MAX));    // INT_MAX ＃include<climits>
printf("%s\n", CONS(A, A));                // compile error --- int(AeA)
```


两句print会被展开为：

```cpp
printf("int max: %s\n","INT_MAX");
printf("%s\n", int(AeA));
```

- **分析**
  由于A和INT_MAX均是宏，且作为宏CONS和STR的参数，并且宏CONS和STR中均含有#或者##符号，所以A和INT_MAX均不能被解引用。导致不符合预期的情况出现。

- **解决方案**
  解决这个问题的方法很简单. 加多一层中间转换宏. 加这层宏的用意是把所有宏的参数在这层里全部展开,
  那么在转换宏里的那一个宏(_STR)就能得到正确的宏参数.e

```cpp
#define A           (2)
#define _STR(s)     #s
#define STR(s)      _STR(s)          // 转换宏
#define _CONS(a,b)  int(a##e##b)
#define CONS(a,b)   _CONS(a,b)       // 转换宏
```


结果：

```cpp
printf("int max: %s\n",STR(INT_MAX));
//输出为: int max:0x7fffffff
//STR(INT_MAX) -->  _STR(0x7fffffff) 然后再转换成字符串； 

printf("%d\n", CONS(A, A));
//输出为：200
//CONS(A, A) -->  _CONS((2), (2))  --> int((2)e(2))
```

