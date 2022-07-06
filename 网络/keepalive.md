##### KeepAlive的不足和局限性

其实，tcp自带的keepalive还是有些不足之处的。

**keepalive只能检测连接是否存活，不能检测连接是否可用。**例如，某一方发生了死锁，无法在连接上进行任何读写操作，但是操作系统仍然可以响应网络层keepalive包。

TCP keepalive 机制依赖于操作系统的实现,灵活性不够，默认关闭，且默认的 keepalive 心跳时间是 7200s, 时间较长。

代理(如socks proxy)、或者负载均衡器，会让tcp keep-alive失效





对于linux内核来说，应用程序若想使用TCP Keepalive，需要设置SO_KEEPALIVE套接字选项才能生效。

有三个重要的参数：

1.     tcp_keepalive_time，在TCP保活打开的情况下，最后一次数据交换到TCP发送第一个保活探测包的间隔，即允许的持续空闲时长，或者说每次正常发送心跳的周期，默认值为7200s（2h）。

2.     tcp_keepalive_probes 在tcp_keepalive_time之后，没有接收到对方确认，继续发送保活探测包次数，默认值为9（次）

3.     tcp_keepalive_intvl，在tcp_keepalive_time之后，没有接收到对方确认，继续发送保活探测包的发送频率，默认值为75s。

​	

TCP socket也有三个选项和内核对应，通过setsockopt系统调用针对单独的socket进行设置：

> - TCPKEEPCNT: 覆盖 tcpkeepaliveprobes
> - TCPKEEPIDLE: 覆盖 tcpkeepalivetime
> - TCPKEEPINTVL: 覆盖 tcpkeepalive_intvl





HTTP协议的Keep-Alive意图在于TCP连接复用，同一个连接上串行方式传递请求-响应数据；TCP的Keepalive机制意图在于探测连接的对端是否存活