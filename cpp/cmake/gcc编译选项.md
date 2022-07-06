#### 编译选项

```cmake
set(CMAKE_C_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror -fno-permissive -fpermissive -g")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror -fno-permissive -fpermissive -g")
    
add_compile_options(-std=c++11)
```



-O0~3	开启编译器优化，-O0为不优化，-O3为最高级别的优化

-Os	优化生成代码的尺寸，使能所有-O2的优化选项，除了那些让代码体积变大的

-Og	优化调试体验，在保留调试信息的同时保持快速的编译，对于生成可调试代码，比-O0更合适，不会禁用调试信息

-Wall	使编译器输出所有的警告信息

-march	指定目标平台的体系结构，如-march=armv4t，常用于交叉编译
-mtune	指定目标平台的CPU以便GCC优化，如`-mtune=arm9tdmi`，常用于交叉编译

**-W/-Wextra**  -W是-Wextra的旧称。该选项可以使能一些**额外**的警告标志。所谓额外，是针对-Wall而言的，-Wall并没有使能所有的警告，尽管它有个`all`

-fpermissive 宽松模式，比如const T* 可以赋值给T*



-fno-elide-constructors 不进行RVO

```cpp
struct Foo {
  Foo() { std::cout << "Constructed" << std::endl; }
  Foo(const Foo &) { std::cout << "Copy-constructed" << std::endl; }
  Foo(Foo &&) { std::cout << "Move-constructed" << std::endl; }
  ~Foo() { std::cout << "Destructed" << std::endl; }
};

Foo f() {
  Foo foo;
  return foo;
}

int main() { 
    Foo foo = f(); 
}

/*
$ clang++ foo.cpp -std=c++11 -fno-elide-constructors && ./a.out
Constructed
Move-constructed
Destructed
Move-constructed
Destructed
Destructed

$ clang++ foo.cpp -std=c++11 && ./a.out
Constructed
Destructed
*/
```