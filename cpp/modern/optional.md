### 	简单用法

```cpp
std::optional<std::string> createStr(bool b){
    if (b){
		// return "what"; ok
        return std::make_optional("what");
    }

	// return {}; ok
    return std::nullopt;
    
    // return b ? std::make_optional("what") : std::nullopt
}

void main(){
    // 用法1
    if (auto ret = createStr(false); ret){
    	std::cout<<ret.value()<<std::endl;
	}
    
    // 用法2
    if (auto ret = createStr(false); ret.has_value()){
    	std::cout<<ret.value()<<std::endl;
	}
    
    // 用法3，如果为空返回默认值
    auto ret = createStr(false)；
    ret.value_or(“nothing”);
    
    // 用法4
    if (auto ret = createStr(false); ret.has_value()){
    	std::cout<<*ret<<std::endl;
	}
}

```

### 比较大小

对于定义了<，>，== 操作符的类型，保存他们的optional对象也可以比较大小。如optional<int>之间比较大小和直接比较int数值的大小是一样的。比较特殊的是std::nullopt，在比较大小时，它总小于存储有效值的optional对象。

``` cpp
std::optional<int> int1(1);
std::optional<int> int2(10);
std::optional<int> int3;

std::cout << std::boolalpha;
std::cout << (int1 < int2) << std::endl; // true
std::cout << (int2 > int1) << std::endl; // true
std::cout << (int3 == std::nullopt) << std::endl; // true
std::cout << (int3 < int1) << std::endl; // true
```

### 内存
使用optional包装原始类型意味着需要存储原始类型的空间和额外的boolean flag，因此optional对象将占有更多的内存空间。此外，optional对象的内存排列须遵循与内部对象一致的内存对齐准则。

```cpp
if (sizeof(double) == 8 && sizeof(int) == 4){
    std::optional<double> optDouble; 
    assert(sizeof(optDouble) == 16);
	std::optional<int> optInt; 
    assert(sizeof(optInt) == 8);
}

```

