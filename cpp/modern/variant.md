

### 简单用法

`std::variant`是类型安全的`union`

```cpp
#include <variant>
#include <iostream>

union my_union
{
    int i;
    float f;
    char c;
};

int main()
{
    std::cout << std::boolalpha;
    std::variant<int, float, char> variant;
    //这里的variant等价于my_union
    
    //在构造的时候，如果构造过程中抛出了异常，valueless_by_exception的返回值为true
    std::cout<< variant.valueless_by_exception()<<std::endl;   //false

    {
        variant = 12;   // variant包含了int类型
        int i = std::get<int>(variant);  //使用std::get<T>可以获取所含有的值

        try
        {
            auto f = std::get<float>(variant);  //此时的值为int，所以想要获取float的时候就会抛出异常
        }
        catch (const std::bad_variant_access & exception)
        {
            std::cout << exception.what() << std::endl;
        }

        variant = 1.0f;
        auto f = std::get<float>(variant);
        std::cout << f << std::endl;  //1.0
    }
    

    {
        //还可以使用索引来获取对应的值
        auto f = std::get<1>(variant);  
        try
        {
            auto i = std::get<0>(variant);
        }
        catch (const std::bad_variant_access & exception)
        {
            std::cout << exception.what() << std::endl;
        }

        variant = 1;
        auto i = std::get<0>(variant);
        std::cout<<i<<std::endl;  //1
    }

    variant = 2.0f;
    std::cout << variant.index() << std::endl;  //1

    variant = 2;
    std::cout << variant.index() << std::endl;  //0

    // 判断是否保存该类型
    if (std::holds_alternative<int>(variant)) {
		std::cout << L"var1 is " << typeid(int).name() << std::endl;
        std::cout << "value " << std::get<int>(variant);
	}
    return 0;
}
```



