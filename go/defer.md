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



 先defer再退栈，下面的返回值具名？

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



**`defer` 和函数绑定。** 两个理解，`defer` 只会和 `defer` 语句所在的特定函数绑定在一起，作用域也只在这个函数。从语法上来讲，`defer` 语句也一定要在函数内，否则会报告语法错误。

```go
package main

func main() {
 func() {
  defer println("--- defer ---")
 }()
 println("--- ending ---")
}
```

如上，`defer` 处于一个匿名函数中，就 main 函数本身来讲，匿名函数 `fun(){}()` 先调用且返回，然后再调用 `println("--- ending ---")` ，所以程序输出自然是：

```
--- defer ---
--- ending ---
```

## 异常场景

这个是个非常重要的特性：`panic` 也能执行。Golang 不鼓励异常的编程模式，但是却也留了 `panic-recover` 这个异常和捕捉异常的机制。所以 `defer` 机制就显得尤为重要，甚至可以说是必不可少的。因为你没有一个无视异常，永保调用的 `defer` 机制，很有可能就会发生各种资源泄露，死锁等场景。为什么？因为发生了 `panic` 却不代表进程一定会挂掉，很有可能被外层 `recover` 住。

```go
package main

func main() {
 defer func() {
  if e := recover(); e != nil {
   println("--- defer ---")
  }
 }()
 panic("throw panic")
}
```

如上，`main` 函数注册一个 defer ，且稍后主动触发 `panic`，`main` 函数退出之际就会调用 `defer` 注册的匿名函数。再提一点，这里其实有两个要点：

1. `defer` 在 `panic` 异常场景也能确保调用；
2. `recover` 必须和 `defer` 结合才有意义

## 并发同步

以下的例子对两个并发的协程做了下同步控制，常规操作。

```go
var wg sync.WaitGroup

for i := 0; i < 2; i++ {
    wg.Add(1)
    go func() {
        defer wg.Done()
        // 程序逻辑
    }()
}
wg.Wait()
```



## 锁场景

加锁解锁必须配套，在 Golang 有了 `defer` 之后，你就可以写了 `lock` 之后，立马就写 `unlock` ，这样就永远不会忘了。

```go
 mu.RLock()
 defer mu.RUnlock()
```

但是请注意，`lock` 以下的代码都会在锁内。所以下面的代码要足够精简和快速才行，如果说下面的逻辑很复杂，那么可能就需要手动控制 `unlock` 防止的位置了。



## 资源释放

某些资源是临时创建的，作用域只存在于现场函数中，用完之后需要销毁，这种场景也适用 `defer` 来释放。**释放就在创建的下一行**，这是个非常好的编程体验，这种编程方式能极大的避免资源泄漏。因为写了创建立马就可以写释放了，再也不会忘记了。

```go
    // new 一个客户端 client；
    cli, err := clientv3.New(clientv3.Config{Endpoints: endpoints})
    if err != nil {
        log.Fatal(err)
    }
    // 释放该 client ，也就是说该 client 的声明周期就只在该函数中；
    defer cli.Close()
```

## panic-recover

recover 必须和 defer 结合才行，使用姿势一般如下：

```go
 defer func() {
  if v := recover(); v != nil {
   _ = fmt.Errorf("PANIC=%v", v)
  }
 }()
```



总结



1. `defer` 其实并不是 Golang 独创，是多种高级语言的共同选择；
2. `defer` 最重要的一个特点就是无视异常可执行，这个是 Golang 在提供了 `panic-recover` 机制之后必须做的补偿机制；
3. `defer` 的作用域存在于函数，`defer` 也只有和函数结合才有意义；
4. `defer` 允许你把配套的两个行为代码放在最近相邻的两行，比如创建&释放、加锁&放锁、前置&后置，使得代码更易读，编程体验优秀；