### Lambda 表达式

根据传递的行为，捕获列表
也分为以下几种：

1. 值捕获与参数传值类似，值捕获的前提是变量可以拷贝，不同之处则在于，被捕获的变量在lambda
    表达式被创建时拷贝，而非调用时才拷贝：

  ```cpp
  void lambda_value_capture() {
  	int value = 1;
  	auto copy_value = [value] {
  		return value;
  	};
  	value = 100;
  	auto stored_value = copy_value();
  	std::cout << "stored_value = " << stored_value << std::endl;
  	// 这时, stored_value == 1, 而value == 100.
  	// 因为copy_value 在创建时就保存了一份value 的拷贝
  }
  ```

  

2. 引用捕获与引用传参类似，引用捕获保存的是引用，值会发生变化。

   ```cpp
   void lambda_reference_capture() {
   	int value = 1;
   	auto copy_value = [&value] {
   		return value;
   	};
   	value = 100;
   	auto stored_value = copy_value();
   	std::cout << "stored_value = " << stored_value << std::endl;
   	// 这时, stored_value == 100, value == 100.
   	// 因为copy_value 保存的是引用
   }
   ```

   

3. 隐式捕获
手动书写捕获列表有时候是非常复杂的，这种机械性的工作可以交给编译器来处理，这时候可以在
捕获列表中写一个& 或= 向编译器声明采用引用捕获或者值捕获.
总结一下，捕获提供了lambda 表达式对外部值进行使用的功能，捕获列表的最常用的四种形式可
以是：
• [] 空捕获列表
• [name1, name2, . . . ] 捕获一系列变量
• [&] 引用捕获, 让编译器自行推导捕获列表
• [=] 值捕获, 让编译器执行推导引用列表

4. 表达式捕获
    这部分内容需要了解后面马上要提到的右值引用以及智能指针
    上面提到的值捕获、引用捕获都是已经在外层作用域声明的变量，因此这些捕获方式捕获的均为左
    值，而不能捕获右值。
    **C++14** 给与了我们方便，允许捕获的成员用任意的表达式进行初始化，这就允许了右值的捕获，被
    声明的捕获变量类型会根据表达式进行判断，判断方式与使用auto 本质上是相同的：

  ```cpp
  #include <iostream>
  #include <utility>
  int main() {
  	auto important = std::make_unique<int>(1);
  	auto add = [v1 = 1, v2 = std::move(important)](int x, int y) -> int {
  		return x+y+v1+(*v2);
  	};
  	std::cout << add(3,4) << std::endl;return 0;
  }
  ```

  在上面的代码中，important 是一个独占指针，是不能够被捕获到的，这时候我们需要将其转移为
  右值，在表达式中初始化。

#### 泛型Lambda

上一节中我们提到了auto 关键字不能够用在参数表里，这是因为这样的写法会与模板的功能产生
冲突。但是Lambda 表达式并不是普通函数，所以Lambda 表达式并不能够模板化。这就为我们造成了
一定程度上的麻烦：参数表不能够泛化，必须明确参数表类型。
幸运的是，这种麻烦只存在于C++11 中，**从C++14 开始，Lambda 函数的形式参数可以使用auto**
关键字来产生意义上的泛型：

```cpp
auto add = [](auto x, auto y) {
	return x+y;
};
add(1, 2);
add(1.1, 2.2);
```


匿名函数本质就是一个匿名类，如果捕获变量的话则匿名类中包含捕获的数据作为成员变量
``` c++
auto f = []{};

  // 经过编译，
  class __lambda_5_14
  {
    public: 
    inline /*constexpr */ void operator()() const
    {
    }
    
    using retType_5_14 = auto (*)() -> void;
    inline constexpr operator retType_5_14 () const noexcept
    {
      return __invoke;
    };
    
    private: 
    static inline /*constexpr */ void __invoke()
    {
      __lambda_5_14{}.operator()();
    }
    
    
  };
  
  __lambda_5_14 f = __lambda_5_14{};
```