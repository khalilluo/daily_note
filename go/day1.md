常数表达式可以执行任意精度的运算

数值型常量是没有确定的类型的，直到它们被给定了一个类型，比如说一次显示的类型转化

声明变量是变量名在前，类型在后，跟C++等不一样

一个数组可以由零个或多个元素组成，一旦声明了，数组的长度就固定了，不能动态变化。`len()` 和 `cap()` 返回结果始终一样

数组是值类型问题，在函数中传递的时候是传递的值，如果传递数组很大，这对内存是很大开销

```go
func main() {
	var arr =  [5] int {1, 2, 3, 4, 5}
	modifyArr(&arr)
	fmt.Println(arr)
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

切片是一种动态数组，比数组操作灵活，长度不是固定的，可以进行追加和删除。

`len()` 和 `cap()` 返回结果可相同和不同 （不指定长度就是切片？）

```go
	var sli_1 [] int      //nil 切片
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_1),cap(sli_1),sli_1)

	var sli_2 = [] int {} //空切片
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_1),cap(sli_2),sli_2)

	var sli_3 = [] int {1, 2, 3, 4, 5}
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_3),cap(sli_3),sli_3)

	sli_4 := [] int {1, 2, 3, 4, 5}
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_4),cap(sli_4),sli_4)

	var sli_5 [] int = make([] int, 5, 8)
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_5),cap(sli_5),sli_5)

	sli_6 := make([] int, 5, 9)
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_6),cap(sli_6),sli_6)


	// 输出
	// len=0 cap=0 slice=[]
	// len=0 cap=0 slice=[]
	// len=5 cap=5 slice=[1 2 3 4 5]
	// len=5 cap=5 slice=[1 2 3 4 5]
	// len=5 cap=8 slice=[0 0 0 0 0]
    // len=5 cap=9 slice=[0 0 0 0 0]
```

切片的操作是右闭区间

切片append可以添加多个元素，且需要赋值给其他对象，否则编译不通过

使用copy可以复制切片（一维是深拷贝，不影响原切片，二维？）

Slice 可以组成多维数据结构。内部的 slice 长度可以不同，这和多位数组不同。

```go
	// 数组-
	var twoD [2][3]int
    for i := 0; i < 2; i++ {
        for j := 0; j < 3; j++ {
            twoD[i][j] = i + j
        }
    }
    fmt.Println("2d: ", twoD)	
	// 输出 2d:  [[0 1 2] [1 2 3]]

	// 切片
	twoD := make([][]int, 3)
    for i := 0; i < 3; i++ {
        innerLen := i + 1
        twoD[i] = make([]int, innerLen)
        for j := 0; j < innerLen; j++ {
            twoD[i][j] = i + j
        }
    }
    fmt.Println("2d: ", twoD)

	// 输出 2d:  [[0] [1 2] [2 3 4]]
```





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

map

```go
	m := make(map[string]int) // make(map[key-type]val-type).创建空的map
	n := map[string]int{"foo": 1, "bar": 2}
	
    m["k1"] = 7
    m["k2"] = 13
	delete(m, "k2") // 删除一对key-value

	// 从 map 中取值时，可选的第二返回值指示这个键是在这个 map 中。这可以用来消除键不存在和键有零值，像 0 或者 "" 而产生的歧义
	_, prs := m["k2"] // prs值为false
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
	type person struct {    name string    age  int }
	
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

