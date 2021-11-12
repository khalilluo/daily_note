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
}
```

注意，不要在循环内修改计数器的条款在此不通用

### for-range 结构

一般形式为：`for ix, val := range coll { }`。

要注意的是，**`val` 始终为集合中对应索引的值拷贝**，因此它一般只具有只读性质，对它所做的任何修改都不会影响到集合中原有的值（除非指针）

能够迭代utf8的字符串







关键字 continue 只能被用于 for 循环中，且可以使用continue 到goto的标签