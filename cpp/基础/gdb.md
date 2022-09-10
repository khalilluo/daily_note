### 线程
```shell
# 查看是否有相关的栈信息，并且进入trace模式
gdb  pstack 进程ID

# 查看当前进程的线程信息
info thread

# 切换到线程 5 的输出
thread  5

# 查看所有线程的back trace信息
thread apply all bt 

	# 查看该锁被哪个线程所拥有 
p lockName
```

###  查看数据

```shell
# 查看代码
list (l)

```

### 断点
```shell

```

https://blog.csdn.net/Yan__Ran/article/details/123692242

https://blog.csdn.net/weixin_46120107/article/details/123695020

https://zhuanlan.zhihu.com/p/29468840