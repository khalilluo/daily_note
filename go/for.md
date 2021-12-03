### 基于条件判断的迭代

for 结构的第二种形式是没有头部的条件判断迭代（类似其它语言中的 while 循环），基本形式为：`for 条件语句 {}`。

```go
package main

import "fmt"

func main() {
	var i int = 5

    // 即其他语言的while
	for i >= 0 {
		i = i - 1
		fmt.Printf("The variable i is now: %d\n", i)
	}
    
    // map类型的切片
    items := make([]map[int]int, 5)
	for i:= range items {
		items[i] = make(map[int]int, 1)
		items[i][1] = 2
	}
	fmt.Printf("Version A: Value of items: %v\n", items)
}
```

注意，不要在循环内修改计数器的条款在此不通用

### for-range 结构

一般形式为：`for ix, val := range coll { }`。

要注意的是，**`val` 始终为集合中对应索引的值拷贝**，因此它一般只具有只读性质，对它所做的任何修改都不会影响到集合中原有的值（除非指针）

能够迭代utf8的字符串



**range**

```go
   	nums := []int{2, 3, 4}
    sum := 0
    for _, num := range nums {		// 提供索引和值，不需要索引用空值定义符表示
        sum += num
    }
    fmt.Println("sum:", sum)
    

	for i := range person {		// 只有一个循环变量的时候是索引
		fmt.Printf("person[%d]: %s\n", i, person[i])
	}


    for i, num := range nums {
        if num == 3 {
            fmt.Println("index:", i)
        }
    }
    
    kvs := map[string]string{"a": "apple", "b": "banana"}
    for k, v := range kvs {			// range map时是键值对
        fmt.Printf("%s -> %s\n", k, v)
    }
    
    for i, c := range "go" { // 字符串中迭代 unicode 编码。第一个返回值是rune 的起始字节位置，然后第二个是 rune 自己
        fmt.Println(i, c) 
        // 输出0 103    1 111
    }
	
```



**使用双返回值判断是否存在key**

```go
_, ok := map1[key1] // 如果key1存在则ok == true，否则ok为false
```

或者和 if 混合使用：

```go
if _, ok := map1[key1]; ok {
	// ...
}
```



关键字 continue 只能被用于 for 循环中，且可以使用continue 到goto的标签