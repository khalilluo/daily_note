```c++
struct A { 
    int x;
    int getX() { return x; }
    int add(int y) { return x+y; }
};

A a{2};


/**************************************************************************/
// 如何制作一个只调用getX()给定的仿函数A
auto get1 = std::mem_fn(&A::getX);
auto get2 = std::bind(&A::getX, _1);	// _1代表的是类对象

get1(a); // yields 2
get2(a); // same

/**************************************************************************/
// 有参数时mem_fn更简洁
auto add1 = std::mem_fn(&A::add);
auto add2 = std::bind(&A::add, _1, _2);	// 第一个参数是类对象，第二个是参数

add1(a, 5); // yields 7
add2(a, 5); // same


/**************************************************************************/
// 如果要绑定特定的参数，mem_fn无法做到
auto add_5 = std::bind(&A::add, _1, 5);
add_5(a); // yields 7 
```





依次调用对象的成员函数

```c++
struct Test {
    int i = 0;
    Test(int i_) : i(i_){};
    void Print() const {
        std::cout << "i:" << i <<std::endl;
    }
};
int main() {
    std::vector<Test> test_vec;
    test_vec.emplace_back(1);
    test_vec.emplace_back(2);
    std::for_each(test_vec.cbegin(), test_vec.cend(), std::mem_fn(&Test::Print));
}
```

