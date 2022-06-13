# 原理

Unix Domain Sockets，简称UDS，又叫IPC Socket，可以使同一机器上两个或者多个进程进行数据通信，跟传统的TCP/IP socket有所不同。不需要经过网络协议栈，不需要打包拆包、计算校验和、维护序号和应答等，只是将应用层数据从一个进程拷贝到另一个进程。这是因为，IPC 机制本质上是可靠的通讯，而网络协议是为不可靠的通讯设计的

| 维度 | UDS | TCP/IP socket |
|:-------:|:-------:|:--------:|
| 标识 | 一个文件名，例如：/var/lib/example/example.socket |  单元格  |
|  包处理过程      |     将应用层数据从一个进程拷贝到另一个进程   |        需要经过网络协议栈，打包拆包、计算校验和、维护序号和应答等  |
| 使用场景 | 同一台机器上两个或多个进程间通信，速度更快 |  跨网络通信  |


UDS通信可以用下面的模型描述：
[![qXzeUI.png](https://s1.ax1x.com/2022/04/06/qXzeUI.png)](https://imgtu.com/i/qXzeUI)


# 代码
我们接下以golang为例来看看代码，代码分服务端和客户端

### 服务端
#### 设计
- 监听socket文件
- 等待下一个连接
- 处理连接
  1. 生成一个UUID，将该UUID回应给客户端，作为该连接的标识
  2. 接收下一条消息
  3. 将连接标识回应客户端
  4. 重复2、3
  5. 关闭连接
- 重复2、3
  
```go
package main
 
import (
	"context"
	"fmt"
	"net"
	"os"
	"os/signal"
	"syscall"
 
	"github.com/google/uuid"
)
 
func connHandler(ctx context.Context, conn *net.UnixConn, id string) {
	defer conn.Close()
 
	_, err := conn.Write([]byte(id))
	if err != nil {
		fmt.Println("send id failed: ", err)
		return
	}
 
	var buf [1024]byte
 
	for {
		select {
		case <-ctx.Done():
			return
		default:
			n, err := conn.Read(buf[:])
			if err != nil {
				fmt.Println("connection read error: ", err)
				return
			}
			fmt.Printf("%s: %s\n", id, string(buf[:n]))
			_, err = conn.Write([]byte(id))
			if err != nil {
				fmt.Println("response failed: ", err)
				return
			}
		}
	}
}
 
func main() {
	udsFile := "/tmp/unixdomain"
    // three types
    // unix: SOCK_STREAM
    // unixdomain: SOCK_DGRAM
    // unixpacket: SOCK_SEQPACKET
    // ListenUnix when type is unix or unixpacket
    // ListenUnixgram when type is unixgram
	l, err := net.ListenUnix("unix", &net.UnixAddr{Name: udsFile, Net: "unix"})
	if err != nil {
		panic(err)
	}
	defer os.Remove(udsFile)
 
	ch := make(chan os.Signal, 1)
	signal.Notify(ch, os.Interrupt, os.Kill, syscall.SIGTERM)
 
	ctx, cancle := context.WithCancel(context.Background())
 
	for {
		select {
		case sig := <-ch:
			fmt.Println("server stop: ", sig)
			cancle()
			return
		default:
			conn, err := l.AcceptUnix()
			if err != nil {
				panic(err)
			}
			go connHandler(ctx, conn, uuid.New().String())
		}
	}
}
```


### 客户端
#### 设计
1. 连接socket文件
2. 处理连接
   1. 接收服务端分配的ID
   2. 将ID作为消息内容发送给服务端
   3. 接收服务端的回应
   4. 重复2、3
3. 关闭连接

```go
package main
 
import (
	"fmt"
	"net"
	"os"
	"os/signal"
	"syscall"
	"time"
)
 
func main() {
	t := "unix" // or "unixgram" or "unixpacket"
	conn, err := net.DialUnix(t, nil, &net.UnixAddr{"/tmp/unixdomain", t})
	if err != nil {
		panic(err)
	}
	defer conn.Close()
 
	ch := make(chan os.Signal, 1)
	signal.Notify(ch, os.Interrupt, os.Kill, syscall.SIGTERM)
 
	var buf [1024]byte
	n, err := conn.Read(buf[:])
	if err != nil {
		fmt.Println("read id failed: ", err)
		return
	}
	id := string(buf[:n])
	fmt.Println("server response me with id: ", id)
 
	for {
		select {
		case sig := <-ch:
			fmt.Println("server stop: ", sig)
			return
		default:
			_, err = conn.Write([]byte(id))
			if err != nil {
				panic(err)
			}
 
			n, err = conn.Read(buf[:])
			if err != nil {
				fmt.Println("read response failed: ", err)
				return
			}
			fmt.Println("server response: ", string(buf[:n]))
 
			time.Sleep(time.Second)
		}
	}
}
```

其他参考https://blog.csdn.net/z2066411585/article/details/78966434/