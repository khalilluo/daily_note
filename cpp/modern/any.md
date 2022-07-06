```cpp
#include <any>
#include <iostream>
 
int main()
{
    std::cout << std::boolalpha;
 
    // any 类型
    std::any a = 1;
    std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';
    a = 3.14;
    std::cout << a.type().name() << ": " << std::any_cast<double>(a) << '\n';
    a = true;
    std::cout << a.type().name() << ": " << std::any_cast<bool>(a) << '\n';
 
    // 有误的转型
    try
    {
        a = 1;
        std::cout << std::any_cast<float>(a) << '\n';
    }
    catch (const std::bad_any_cast& e)
    {
        std::cout << e.what() << '\n';
    }
 
    // 拥有值
    a = 1;
    if (a.has_value())
    {
        std::cout << a.type().name() << '\n';
    }
 
    // 重置
    a.reset();
    if (!a.has_value())
    {
        std::cout << "no value\n";
    }
 
    // 指向所含数据的指针
    a = 1;
    int* i = std::any_cast<int>(&a);
    std::cout << *i << "\n";
}

/* 输出
i: 1
d: 3.14
b: true
bad any_cast
i
no value
1
*/
```

总结：

```c++
std::any a = 1; // 声明一个any类型的容器，容器中的值为int类型的1
a.type();  // 得到容器中的值的类型
std::any_cast<int>(a); // 强制类型转换, 转换失败可以捕获到std::bad_any_cast类型的异常
has_value(); // 判断容器中是否有值
reset(); // 删除容器中的值
std::any_cast<int>(&a); // 强制转换得到容器中的值的地址
```

