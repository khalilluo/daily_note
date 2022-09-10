### 说明
获取或设置资源使用限制，linux下每种资源都有相关的软硬限制，软限制是内核强加给相应资源的限制值，硬限制是软限制的最大值。非授权调用的进程只能将其软限制指定为0~硬限制范围中的某个值，同时能不可逆转地降低其硬限制。授权进程可以任意改变其软硬限制。RLIM_INFINITY:表示不对资源限制。

#### 用法

``` c
#include <sys/resource.h>

/*
成功执行时，返回0。失败返回-1，errno被设为以下的某个值
EFAULT：rlim指针指向的空间不可访问
EINVAL：参数无效
EPERM：增加资源限制值时，权能不允许
*/
int getrlimit(int resource, struct rlimit *rlim);
int setrlimit(int resource, const struct rlimit *rlim);

struct rlimit {
　　rlim_t rlim_cur;
　　rlim_t rlim_max;
};

```

resource：

```c
 
RLIMIT_AS //进程的最大虚内存空间，字节为单位。
RLIMIT_CORE //内核转存文件的最大长度。
RLIMIT_CPU //最大允许的CPU使用时间，秒为单位。当进程达到软限制，内核将给其发送SIGXCPU信号，这一信号的默认行为是终止进程的执行。然而，可以捕捉信号，处理句柄可将控制返回给主程序。如果进程继续耗费CPU时间，核心会以每秒一次的频率给其发送SIGXCPU信号，直到达到硬限制，那时将给进程发送 SIGKILL信号终止其执行。
RLIMIT_DATA //进程数据段的最大值。
RLIMIT_FSIZE //进程可建立的文件的最大长度。如果进程试图超出这一限制时，核心会给其发送SIGXFSZ信号，默认情况下将终止进程的执行。
RLIMIT_LOCKS //进程可建立的锁和租赁的最大值。
RLIMIT_MEMLOCK //进程可锁定在内存中的最大数据量，字节为单位。
RLIMIT_MSGQUEUE //进程可为POSIX消息队列分配的最大字节数。
RLIMIT_NICE //进程可通过setpriority() 或 nice()调用设置的最大完美值。
RLIMIT_NOFILE //指定比进程可打开的最大文件描述词大一的值，超出此值，将会产生EMFILE错误。
RLIMIT_NPROC //用户可拥有的最大进程数。
RLIMIT_RTPRIO //进程可通过sched_setscheduler 和 sched_setparam设置的最大实时优先级。
RLIMIT_SIGPENDING //用户可拥有的最大挂起信号数。
RLIMIT_STACK //最大的进程堆栈，以字节为单位。



```

```c++
#include <sys/resource.h>
void init_core_dump()
{
    struct rlimit limit;
 
    memset(&limit, 0, sizeof(limit));
    limit.rlim_cur = RLIM_INFINITY; //软限制，表示对资源没有限制
    limit.rlim_max = RLIM_INFINITY; //硬限制，这个参数表示对资源没有限制，一定要大于等于rlim_cur值
    setrlimit(RLIMIT_CORE, &limit);
}
 
int main(void)
{
    init_core_dump();
 
    return 0;
}

```


#### 修改 task 进程资源上限值（ulimit 和 setrlimit）

1）soft limit 是指内核所能支持的资源上限。比如对于 RLIMIT_NOFILE(一个进程能打开的最大文件数，内核默认是 1024)，soft limit 最大也只能达到 1024。对于 RLIMIT_CORE(core 文件的大小，内核不做限制)，soft limit 最大能是 unlimited。  
2）hard limit 在资源中只是作为 soft limit 的上限。当你设置 hard limit 后，你以后设置的 soft limit 只能小于 hard limit。要说明的是，hard limit 只针对非特权进程，也就是进程的有效用户 ID(effective user ID) 不是 0 的进程。具有特权级别的进程 (具有属性 CAP_SYS_RESOURCE)，soft limit 则只有内核上限。

ubuntu 下 ulimit 指令对比
```shell
ulimit -c -n -s  # 软限制   
ulimit -c -n -s -H # 硬限制
```

![](https://img-blog.csdnimg.cn/20200622110250424.png)

备注：
- unlimited 表示 no limit, 即内核的最大值
- 当不指定 limit 的时候，该命令显示当前值。这里要注意的是，当你要修改 limit 的时候，如果不指定 - S 或者 - H，默认是同时设置 soft limit 和 hard limit。也就是之后设置时只能减不能增。所以，建议使用 ulimit 设置 limit 参数是加上 - S。


注意：
在使用 setrlimit，需要检查是否成功来判断新值有没有超过 hard limit。如下例 Linux 系统中在应用程序运行过程中经常会遇到程序突然崩溃，提示：Segmentation fault，这是因为应用程序收到了 SIGSEGV 信号。这个信号提示当进程发生了无效的存储访问，当接收到这个信号时，缺省动作是：终止 w/core。终止 w/core 的含义是：在进程当前目录生成 core 文件，并将进程的内存映象复制到 core 文件中，core 文件的默认名称就是 “core”（这是 Unix 类系统的一个由来已久的功能）。 
事实上，并不是只有 SIGSEGV 信号产生 coredump，还有下面一些信号也产生 coredump：SIGABRT（异常终止）、SIGBUS（硬件故障）、SIGEMT（硬件故障）、SIGFPE（算术异常）、SIGILL（非法硬件指令）、SIGIOT（硬件故障），SIGQUIT，SIGSYS（无效系统调用），SIGTRAP（硬件故障）等。

