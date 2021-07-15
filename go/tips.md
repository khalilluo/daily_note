```go
func main() {
    s := make([]int, 5)
    s = append(s, 1, 2, 3)
    fmt.Println(s)	// [0 0 0 0 0 1 2 3]
}
```





```go
package main

import "fmt"

func main() {
    slice := []int{0, 1, 2, 3}
    m := make(map[int]*int)

    for key, val := range slice {
        m[key] = &val
    }

    for k, v := range m {
    fmt.Println(k, "->", *v)
    }
}

// 注：key的顺序无法确定
0 -> 3
1 -> 3
2 -> 3
3 -> 3
```

`for range` 循环的时候会创建每个元素的副本，而不是每个元素的引用，所以 `m[key] = &val` 取的都是变量val的地址，所以最后 `map` 中的所有元素的值都是变量 `val` 的地址，因为最后 `val` 被赋值为3，所有输出的都是3。



##  new() 与 make() 的区别

**解析：**

- `new(T)` 和 `make(T, args)` 是Go语言内建函数，用来分配内存，但适用的类型不用。
- `new(T)` 会为了 `T` 类型的新值分配已置零的内存空间，并返回地址（指针），即类型为 `*T` 的值。换句话说就是，返回一个指针，该指针指向新分配的、类型为 `T` 的零值。适用于值类型，如 `数组` 、 `结构体` 等。
- `make(T, args)` 返回初始化之后的T类型的值，也不是指针 `*T` ，是经过初始化之后的T的引用。 `make()` 只适用于 `slice` 、 `map` 和 `channel`
- 

## 下面这段代码能否通过编译，不能的话原因是什么；如果能，输出什么？

```
func main() {
    list := new([]int)
    list = append(list, 1)
    fmt.Println(list)
}
```

**答：不能通过**

**解析：**

不能通过编译， `new([]int)` 之后的 `list` 是一个 `*int[]` 类型的指针，不能对指针执行 `append` 操作。可以使用 `make()` 初始化之后再用。同样的， `map` 和 `channel` 建议使用 `make()` 或字面量的方式初始化，不要用 `new` 



## 下面这段代码能否通过编译，如果可以，输出什么？

```
var (
    size := 1024
    max_size = size * 2
)

func main() {
    fmt.Println(size, max_size)
}
```

**答：不能通过**

**解析：**

这道题的主要知识点是变量的简短模式，形如：x := 100 。但这种声明方式有限制：

1. 必须使用显示初始化；
2. 不能提供数据类型，编译器会自动推导；
3. 只能在函数内部使用简短模式；

## 下面这段代码能否通过编译？不能的话，原因是什么？如果通过，输出什么？

```
func main() {
    sn1 := struct {
        age  int
        name string
	}{age: 11, name: "qq"}
	sn2 := struct {
        age  int
        name string
	}{age: 11, name: "11"}

    if sn1 == sn2 {
        fmt.Println("sn1 == sn2")
    }

    sm1 := struct {
        age int
        m   map[string]string
    }{age: 11, m: map[string]string{"a": "1"}}
    sm2 := struct {
        age int
        m   map[string]string
    }{age: 11, m: map[string]string{"a": "1"}}

    if sm1 == sm2 {
        fmt.Println("sm1 == sm2")
    }
}
```

**答：不能通过,invalid operation: sm1 == sm2**

**解析：**

考点是结构体的比较，有几个需要注意的地方：

1. 结构体只能比较是否相等，但是不能比较大小；
2. 想同类型的结构体才能进行比较，结构体是否相同不但与属性类型有关，还与属性顺序和属性名称相关；
3. 如果struct的所有成员都可以比较，则该struct就可以通过==或!=进行比较是否相同，比较时逐个项进行比较，如果每一项都相等，则两个结构体才相等，否则不相等；

**那有什么是可以比较的呢？**

- 常见的有bool、数值型、字符、指针、数组等

**不能比较的有**

- slice、map、函数

## 通过指针变量p访问其成员变量name,有哪几种方式？

- A. p.name
- B. (&p).name
- C. (*p).name
- D. p->name

**答：A C**

## 下面这段代码能否通过编译？如果通过，输出什么？

```
package main

import "fmt"

type MyInt1 int
type MyInt2 = int

func main() {
    var i int = 0
    var i1 MyInt1 = i
    var i2 MyInt2 = i
    fmt.Println(i1, i2)
}
```

**答：不能通过**

**解析：**

这道题考的是 `类型别名` 与 `类型定义` 的区别 第5行代码是基于类型 `int` 创建了新类型 `MyInt1` ，第6行代码是创建了int的类型别名 `MyInt2` ，注意类型别名的定义是 `=` 。所以，第10行代码相当于是将int类型的变量赋值给MyInt1类型的变量，Go是强类型语言，编译当然不通过；而MyInt2只是int的别名，本质上还是int，可以赋值。 第10行代码的赋值可以使用强制类型转换 `var i1 MyInt1 = MyInt1(i)` 

## 以下代码输出什么？

```
func main() {
    a := []int{7, 8, 9}
    fmt.Printf("%+v\n", a)
    ap(a)
    fmt.Printf("%+v\n", a)
    app(a)
    fmt.Printf("%+v\n", a)
}

func ap(a []int) {
    a = append(a, 10)
}

func app(a []int) {
    a[0] = 1
}
```

**答：输出内容为：**

```
[7 8 9]
[7 8 9]
[1 8 9]
```

**解析：**

因为append导致底层数组重新分配内存了，append中的a这个alice的底层数组和外面不是一个，并没有改变外面的

## 关于字符串连接，下面语法正确的是？

- A. str := 'abc' + '123'
- B. str := "abc" + "123"
- C. str := '123' + "abc"
- D. fmt.Sprintf("abc%d", 123)

**答：B、D**

**解析：**

在Golang中字符串用双引号，字符用单引号 字符串连接除了以上两种连接方式，还有 `strings.Join()` 、 `buffer.WriteString()` 等

## 下面这段代码能否编译通过？如果可以，输出什么？

```
const (
    x = iota
    _
    y
    z = "zz"
    k
    p = iota
)

func main() {
    fmt.Println(x, y, z, k, p)
}
```

**答：编译通过，输出：**`**0 2 zz zz 5**` 

**解析：**

iota初始值为0，所以x为0，_表示不赋值，但是iota是从上往下加1的，所以y是2，z是“zz”,k和上面一个同值也是“zz”,p是iota,从上0开始数他是5

## 下面赋值正确的是（）

- A. var x = nil
- B. var x interface{} = nil
- C. var x string = nil
- D. var x error = nil

**答：B、D**

**解析：**

A错在没有写类型，C错在字符串的空值是 `""` 而不是nil。 知识点：nil只能赋值给指针、chan、func、interface、map、或slice、类型的变量。

## 关于init函数，下面说法正确的是（）

- A. 一个包中，可以包含多个init函数；
- B. 程序编译时，先执行依赖包的init函数，再执行main包内的init函数；
- C. main包中，不能有init函数；
- D. init函数可以被其他函数调用；

**答：A、B**

**解析：**

1. init()函数是用于程序执行前做包的初始化的函数，比如初始化包里的变量等；
2. 一个包可以出现多个init()函数，一个源文件也可以包含多个init()函数；
3. 同一个包中多个init()函数的执行顺序没有明确的定义，但是不同包的init函数是根据包导入的依赖关系决定的；
4. init函数在代码中不能被显示调用、不能被引用（赋值给函数变量），否则出现编译失败；
5. 一个包被引用多次，如A import B，C import B，A import C，B被引用多次，但B包只会初始化一次；
6. 引入包，不可出现死循环。即A import B，B import A，这种情况下编译失败；

![](C:\j\github\daily_note\go\image\68747470733a2f2f63646e2e6e6c61726b2e636f6d2f79757175652f302f323031392f706e672f3531373836392f313537343034303036383431332d63666363313763322d366638622d346331632d623039622d6436643239376339663734352e706e6723616c69676e3d6c6.png)