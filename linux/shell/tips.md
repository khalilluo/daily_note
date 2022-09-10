### 查看进程线程数
```shell
# 打印所有进程及其线程
pstree -p 
# 打印某个进程的线程数，需要+1 wc未统计到主线程
pstree -p {pid} | wc -l

ls /proc/{pid}/task | wc -l

# 进程状态中有线程信息
cat /proc/{pid}/status | grep thread

```

### 获取当前目录

```shell
CUR=$(cd `dirname $0`; pwd)
# 获取上级目录
PARENT=$(cd $CUR/..; pwd)
```