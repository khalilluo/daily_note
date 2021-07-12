Deffer

## 闭包

```go
func main() {

	var a = 1
	var b = 2

	defer fmt.Println(a + b)

	a = 2

	fmt.Println("main")
}
```

输出：

main
3

稍微修改一下，再看看：

```go
func main() {
	var a = 1
	var b = 2

	defer func() {
		fmt.Println(a + b)
	}()

	a = 2

	fmt.Println("main")
}
```

输出：

main
4

结论：闭包获取变量相当于引用传递，而非值传递。

稍微再修改一下，再看看：

```go
func main() {
	var a = 1
	var b = 2

	defer func(a int, b int) {
		fmt.Println(a + b)
	}(a, b)

	a = 2

	fmt.Println("main")
}
```

输出：

main
3

结论：传参是值复制。

还可以理解为：defer 调用的函数，参数的值在 defer 定义时就确定了，看下代码

`defer fmt.Println(a + b)`，在这时，参数的值已经确定了。

而 defer 函数内部所使用的变量的值需要在这个函数运行时才确定，看下代码

`defer func() { fmt.Println(a + b) }()`，a 和 b 的值在函数运行时，才能确定



 

```go
// 返回值具名，退栈时返回值加1，返回2
func t2() (a int) {
   defer func() {
      a++
   }()
   return 1
}
```





```go
func calc(index string, a, b int) int {
	ret := a + b
	fmt.Println(index, a, b, ret)
	return ret
}

func main() {
	x := 1
	y := 2
	defer calc("A", x, calc("B", x, y))
	x = 3
	defer calc("C", x, calc("D", x, y))
	y = 4
}

```

其实上面代码可以拆解为：

```go
func calc(index string, a, b int) int {
	ret := a + b
	fmt.Println(index, a, b, ret)
	return ret
}

func main() {
	x := 1
	y := 2
	tmp1 := calc("B", x, y)
	defer calc("A", x, tmp1)
	x = 3
	tmp2 := calc("D", x, y)
	defer calc("C", x, tmp2)
	y = 4
}
```

所以顺序就是：B D C A。

执行到 tmp1 时，输出：B 1 2 3。

执行到 tmp2 时，输出：D 3 2 5。

根据 defer 执行顺序原则，先声明的后执行，所以下一个该执行 C 了。

又因为传参是值赋值，所以在 A 的时候，无法用到 `x = 3` 和 `y = 4`，在 C 的时候，无法用到 `y = 4`。

执行到 C 时，输出：C 3 5 8

执行到 A 时，输出：A 1 3 4



- defer 函数定义的顺序 与 实际执的行顺序是相反的，也就是最先声明的最后才执行
- 当`os.Exit()`方法退出程序时，defer不会被执行
- defer 只对当前协程有效。