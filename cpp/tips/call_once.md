### 多线程
```cpp
static std::once_flag once;  
static Json::CharReaderBuilder builder;  
std::call_once(once, []() { builder["collectComments"] = false; });
```

一旦调用的函数抛出了异常，那么下次执行`std::call_once`时不会跳过，而是会再次尝试，知道函数执行成功，不抛出异常为止。



### 单线程
```cpp
static const int si = [this]{
	// do something
	return 0;
}();
```