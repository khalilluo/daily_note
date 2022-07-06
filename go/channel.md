## 并行并发

首先，我们清楚 Go 语言的线程是并发机制，不是并行机制。

那么，什么是并发，什么是并行？

并发是不同的代码块交替执行，也就是交替可以做不同的事情。

并行是不同的代码块同时执行，也就是同时可以做不同的事情。

举个生活化场景的例子：

你正在家看书，忽然电话来了，然后你接电话，通话完成后继续看书，这就是并发，看书和接电话交替做。

如果电话来了，你一边看书一遍接电话，这就是并行，看书和接电话一起做

## 声明 chan

```go
// 声明不带缓冲的通道
ch1 := make(chan string)

// 声明带10个缓冲的通道
ch2 := make(chan string, 10)

// 声明只读通道
ch3 := make(<-chan string)

// 声明只写通道
ch4 := make(chan<- string)
```

注意：

不带缓冲的通道，进和出都会阻塞。=

- close 以后不能再写入，写入会出现 panic
- 重复 close 会出现 panic
- 只读的 chan 不能 close
- close 以后还可以读取数据





## 生产消费者

```go
// package awesomeProject
package main

import (
   "fmt"
   "time"
)

func producer(ch chan string) {
   fmt.Println("producer start")
   ch <- "a"
   ch <- "b"
   ch <- "c"
   ch <- "d"
   fmt.Println("producer end")
}

func customer(ch chan string) {
   for {
      msg := <- ch
      fmt.Println(msg)
   }
}

func main(){
   fmt.Println("main start")
   ch := make(chan string, 3)
   go producer(ch)
   go customer(ch)

   time.Sleep(1 * time.Second)
   fmt.Println("main end")
}
```