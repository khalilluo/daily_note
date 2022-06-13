#### 经典的匹配对应的类型产生不同函数

```cpp
template <typename T>
typename std::enable_if<std::is_trivial<T>::value>::type SFINAE_test(T value)
{
    std::cout<<"T is trival"<<std::endl;
}

template <typename T>
typename std::enable_if<!std::is_trivial<T>::value>::type SFINAE_test(T value)
{
    std::cout<<"T is none trival"<<std::endl;
}
```


#### 用参数校验传入类似是否合法

```cpp
template <typename T>  
bool checkID(const typename std::enable_if<std::is_same_v<typename std::decay<T>::type, uint64_t>, T>::type &t, const Json::Value& value) {  
    if (!value.isUInt64())  
        return false;  
  
 if (value.asUInt64() != t){  
        return false;  
 }  
  
    return true;  
}  
  
template <typename T, typename = typename std::enable_if<std::is_same_v<T, std::string>>::type>  
bool checkID( const T& t, const Json::Value& value) {  
    if (!value.isString())  
        return false;  
  
 if (value.asString() != t){  
        return false;  
 }  
    return true;  
}
```

#### 编译时期来确定某个 type 是否具有我们需要的性质
以下代码检查类型是否为指针
```cpp
```cpp
template <class T>
struct is_pointer
{
    template <class U>
    static char is_ptr(U *);

    template <class X, class Y>
    static char is_ptr(Y X::*);

    template <class U>
    static char is_ptr(U (*)());

    static double is_ptr(...);

    static T t;
    enum { value = sizeof(is_ptr(t)) == sizeof(char) };
};

struct Foo {
    int bar;
};

void testTypeCheck() {
    typedef int * IntPtr;
    typedef int Foo::* FooMemberPtr;
    typedef int (*FuncPtr)();

    printf("%d\n",is_pointer<IntPtr>::value);        // prints 1
    printf("%d\n",is_pointer<FooMemberPtr>::value);  // prints 1
    printf("%d\n",is_pointer<FuncPtr>::value);       // prints 1
}
```

检查是否含有某个函数

```cpp
template<typename T>
struct has_no_destroy {
    template<typename C>
    static char test(decltype(&C::no_destroy));


    template<typename C>
    static int32_t test(...);

    const static bool value = sizeof(test<T>(0)) == 1;
};

```cpp
struct A {

};

struct B {
    void no_destroy(){}
};
struct C {
    int no_destroy;
};

struct D : B {

};

void testNoDestroy() {
    printf("%d\n",has_no_destroy<A>::value);
    printf("%d\n",has_no_destroy<B>::value);
    printf("%d\n",has_no_destroy<C>::value);
    printf("%d\n",has_no_destroy<D>::value);
}
// 其作用就是用来判断是否有 no_destroy 函数

```

### 检查是否包含方法
[[检查对象是否含有某种方法]]