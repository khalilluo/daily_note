```go
person := map[int]string{
   1 : "Tom",
   2 : "Aaron",
   3 : "John",
   5 : "luo",
}

fmt.Printf("len=%d map=%v\n", len(person), person)

fmt.Println("")

//循环
for k, v := range person {
   fmt.Printf("person[%d]: %s\n", k, v)
}

fmt.Println("")

for i := range person {
   fmt.Printf("person[%d]: %s\n", i, person[i])
}

fmt.Println("")

// 此处slice和array可以正常遍历，map会出错
for i := 1; i <= len(person); i++ {
   fmt.Printf("person[%d]: %s\n", i, person[i])
}

fmt.Println("")

//使用空白符
for _, name := range person {
   fmt.Println("name :", name)
}
```

## goto

改变函数内代码执行顺序，**不能跨函数使用。**

```go

package main

import "fmt"

func main() {
	fmt.Println("begin")

	for i := 1; i <= 10; i++ {
		if i == 6 {
			goto END
		}
		fmt.Println("i =", i)
	}

	END :
		fmt.Println("end")
}
```

```go
package main

import "fmt"

func main() {
	i := 1
	fmt.Printf("当 i = %d 时：\n", i)

	switch i {
		case 1:
			fmt.Println("输出 i =", 1)
		case 2:
			fmt.Println("输出 i =", 2)
		case 3:
			fmt.Println("输出 i =", 3)
			fallthrough
		case 4,5,6:
			fmt.Println("输出 i =", "4 or 5 or 6")
		default:
			fmt.Println("输出 i =", "xxx")
	}
}


```

默认每个 case 带有 break
case 中可以有多个选项
**fallthrough** 不跳出，并执行下一个 case



```go
// 这个函数使用任意数目的 int 作为参数
func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0
    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}


	nums := []int{1, 2, 3, 4}
    sum(nums...) // 如果你的 slice 已经有了多个值，想把它们作为变参使用，你要这样调用 func(slice...)
```