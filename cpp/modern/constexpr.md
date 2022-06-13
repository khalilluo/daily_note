


## 编译时确认分支
```c++

// C++17之前
// 只有一个模板参数时调用此模板
template<int N>
int sum()
{
    return N;
}

// 模板参数 > 2 个时调用此模板
template <int N, int N2, int... Ns>
int sum()
{
    return N + sum<N2, Ns...>();
}



// c++17开始
// 方案1
template <int N, int... Ns>
auto sum()
{
    if constexpr (0 == sizeof...(Ns))
        return N;
    else
        return N + sum<Ns...>();
}

// 方案2 折叠表达式
//
template<typename ...Ns>
auto sum(Ns... ns) {
    return (ns + ...);
}

```


避免编译错误

```cpp
template<typename T>
std::string toStr(T t) {
	// 如果没有constexpr，如果调用toStr(std::string{"123"})则编译错误
    if constexpr (std::is_same_v<T, std::string>)
        return t;
    else
        return std::to_string(t);
}
```