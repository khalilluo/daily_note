C++11 中引入 `std::ref` 用于取某个变量的引用，这个引入是为了解决一些传参问题。

我们知道 C++ 中本来就有引用的存在，为何 C++11 中还要引入一个 `std::ref` 了？主要是考虑函数式编程（如 `std::bind`）在使用时，**是对参数直接拷贝，而不是引用。下面通过例子说明**

示例1：

 

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```c++
#include<iostream>
#include<functional>

void f(int& n1, int& n2, const int& n3)
{
    std::cout << "In function: " << n1 << ' ' << n2 << ' ' << n3 << '\n';
    ++n1; // increments the copy of n1 stored in the function object
    ++n2; // increments the main()'s n2
    // ++n3; // compile error
}

int main()
{
    int n1 = 1, n2 = 2, n3 = 3;
    std::function<void()> bound_f = std::bind(f, n1, std::ref(n2), std::cref(n3));
    n1 = 10;
    n2 = 11;
    n3 = 12;
    std::cout << "Before function: " << n1 << ' ' << n2 << ' ' << n3 << '\n';
    bound_f();
    std::cout << "After function: " << n1 << ' ' << n2 << ' ' << n3 << '\n';
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

```c++
root@ubuntu:~/c++# ./obj 
Before function: 10 11 12
In function: 1 11 12
After function: 10 12 12   --n2增加1
root@ubuntu:~/c++# 
f(int& n1, int& n2, const int& n3) 参数都是引用
```

上述代码在执行 `std::bind` 后，在函数 `f()` 中 **`n1` 的值仍然是 1，`n2` 和 `n3` 改成了修改的值**，说明 `std::bind` 使用的是参数的拷贝而不是引用，因此必须显示利用 `std::ref` 来进行引用绑定。具体为什么 `std::bind` 不使用引用，可能确实有一些需求，使得 C++11 的设计者认为默认应该采用拷贝，如果使用者有需求，加上 `std::ref` 即可。

示例2：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
#include<iostream>
#include<string>
#include<thread>





void threadFunc(std::string &str, int a)
{
    str = "change by threadFunc";
    a = 13;
}

int main()
{
    std::string str("main");
    int a = 9;
    std::thread th(threadFunc, std::ref(str), a);

    th.join();

    std::cout<<"str = " << str << std::endl;
    std::cout<<"a = " << a << std::endl;

    return 0;
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

```
root@ubuntu:~/c++# ./obj
str = change by threadFunc
a = 9
root@ubuntu:~/c++# 
```

 

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```c++
#include<iostream>
#include<string>
#include<thread>


void threadFunc(std::string &str, int a)
{
    str = "change by threadFunc";
    a = 13;
}

int main()
{
    std::string str("main");
    int a = 9;
    std::thread th(threadFunc, std::ref(str), std::ref(a));

    th.join();

    std::cout<<"str = " << str << std::endl;
    std::cout<<"a = " << a << std::endl;

    return 0;
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

```c++
root@ubuntu:~/c++# ./obj 
str = change by threadFunc
a = 9
root@ubuntu:~/c++# 
```

 

可以看到，和 `std::bind` 类似，多线程的 `std::thread` 也是必须显式通过 `std::ref` 来绑定引用进行传参，否则，形参的引用声明是无效的。

 

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```c++
#include<iostream>
#include<string>
#include<thread>





void threadFunc(std::string &str, int & a)
{
    str = "change by threadFunc";
    a = 13;
}

int main()
{
    std::string str("main");
    int a = 9;
    std::thread th(threadFunc, std::ref(str), std::ref(a));

    th.join();

    std::cout<<"str = " << str << std::endl;
    std::cout<<"a = " << a << std::endl;

    return 0;
}
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

```c++
threadFunc(std::string &str, int & a) 都采用引用
root@ubuntu:~/c++#  g++ -std=c++11 -pthread obj.cpp  -o obj
root@ubuntu:~/c++# ./obj 
str = change by threadFunc
a = 13
```





#### 总结：

bind和线程参数引用是副本，如果是对象则会调用拷贝构造函数生成另外一个对象，如果希望在里面修改参数需要使用std::ref，且参数**也是引用才能修改。注意保证引用的可用性**

**但是为了保证线程的安全，这样的方式不可以用detach使主线程与子线程分开**