

## 数组

一个数组可以由零个或多个元素组成，一旦声明了，数组的长度就固定了，不能动态变化。`len()` 和 `cap()` 返回结果始终一样

数组是值类型问题，**在函数中传递的时候是传递的值，如果传递数组很大，这对内存是很大开销**。

所以通常参数定义为切片，传参时讲数组转为切片传递（func (arr[:])）

```go
func main() {
	var arr =  [5] int {1, 2, 3, 4, 5}
	modifyArr(&arr)
	fmt.Println(arr)
    
    // a是长度为4的数组
    // for循环时是索引
    a := [...]string{"a", "b", "c", "d"}
    for i := range a {
        fmt.Println("Array item", i, "is", a[i])
    }
   
}

func modifyArr(a *[5] int) {
    // 使用指针传递，可以改变原数组值
	a[1] = 20
}


```

数组赋值问题，同样类型的数组（长度一样且每个元素类型也一样）才可以相互赋值，反之不可以

```go
var arr =  [5] int {1, 2, 3, 4, 5}
var arr_1 [5] int = arr
var arr_2 [6] int = arr  // 报错
```

第一种变化：

```go
var arrAge = [5]int{18, 20, 15, 22, 16}
```

注意 `[5]int` 可以从左边起开始忽略：`[10]int {1, 2, 3}` :这是一个有 10 个元素的数组，除了前三个元素外其他元素都为 0。

第二种变化：

```go
var arrLazy = [...]int{5, 6, 7, 8, 22}
```

`...` 可同样可以忽略，从技术上说它们其实变化成了切片。

第三种变化：`key: value 语法`

```go
var arrKeyValue = [5]string{3: "Chris", 4: "Ron"}
```

只有索引 3 和 4 被赋予实际的值，其他元素都被设置为空的字符串，所以输出结果为：





```go
	if num := 9; num < 0 { // 在条件语句之前可以有一个语句；任何在这里声明的变量都可以在所有的条件分支中使用
        fmt.Println(num, "is negative")
    } else if num < 10 {
        fmt.Println(num, "has 1 digit")
    } else {
        fmt.Println(num, "has multiple digits")
    }
	// go 没有三目运算符
```

```go
	switch time.Now().Weekday() {
    case time.Saturday, time.Sunday:  // 在一个 case 语句中，你可以使用逗号来分隔多个表达式
        fmt.Println("it's the weekend")
    default:
        fmt.Println("it's a weekday")
    }

  	t := time.Now()
    switch {
    case t.Hour() < 12:		// case 可以使用非常亮判断
        fmt.Println("it's before noon")
    default:
        fmt.Println("it's after noon")
    }
```



range

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

结构体

```go
	type person struct {    
        name string    
        age  int 
    }
	
	// 使用这个语法创建了一个新的结构体元素。
    fmt.Println(person{"Bob", 20}) 

	// 你可以在初始化一个结构体元素时指定字段名字。
    fmt.Println(person{name: "Alice", age: 30}) 

	// 省略的字段将被初始化为零值。
    fmt.Println(person{name: "Fred"})

	// & 前缀生成一个结构体指针。
    fmt.Println(&person{name: "Ann", age: 40})

	// 使用点来访问结构体字段。
    s := person{name: "Sean", age: 50}
    fmt.Println(s.name)
	
	// 也可以对结构体指针使用. - 指针会被自动解引用。
    sp := &s
    fmt.Println(sp.age)
	
	// 结构体是可变的。
    sp.age = 51
    fmt.Println(sp.age)

	//匿名结构体
	p4 := struct {
		Name string
		Age int
	} {Name:"匿名", Age:33}


	// 输出
	{Bob 20}
	{Alice 30}
	{Fred 0}
	&{Ann 40}
	Sean
	50
	51
```

```go
// 生成json
package main

import (
	"encoding/json"
	"fmt"
)

type Result struct {
	Code    int    `json:"code"`
	Message string `json:"msg"`
}

func main() {
	var res Result
	res.Code    = 200
	res.Message = "success"

	//序列化
	jsons, errs := json.Marshal(res)
	if errs != nil {
		fmt.Println("json marshal error:", errs)
	}
	fmt.Println("json data :", string(jsons))
	
	//反序列化
	var res2 Result
	errs = json.Unmarshal(jsons, &res2)
	if errs != nil {
		fmt.Println("json unmarshal error:", errs)
	}
	fmt.Println("res2 :", res2)
}

// 输出
json data : {"code":200,"msg":"success"}
res2 : {200 success}
```

