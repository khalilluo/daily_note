### PRAGMA使用

```c
// 1、设置PAGE_SIZE: 需要在建表之前设置才能生效，默认是4k。设置大了能优化查询速度但增加内存使用
// 假设一条记录为3K,当PAGE_SIZE为1K时，完全查询这一条记录需要3次寻址（查找对应的PAGE）；而当PAGE_SIZE为4K，完全查询这一条记录仅需1次寻址。
"PRAGMA page_size = bytes"
    
// 2、插入数据后再建索引比先建索引再插入快
// 3、
```



### 数据库定义在内存中

除非有特殊用途，否则还是建议乖乖地定义在磁盘上

```c++
#define DATABASE ":memory:"
```

### synchronous模式

```sql
PRAGMA synchronous = FULL; (2) 
PRAGMA synchronous = NORMAL; (1) 
PRAGMA synchronous = OFF; (0)
```

当synchronous设置为FULL , SQLite 数据库引擎在紧急时刻会暂停以确定数据已经写入磁盘。这使 系统崩溃或电源出问题时能确保数据库在重起后不会损坏。FULL synchronous很安全但很慢。

当synchronous设置为NORMAL, SQLite数据库引擎在大部分紧急时刻会暂停，但不像FULL模式下那么频繁。 NORMAL模式下有很小的几率(但不是不存在)发生电源故障导致数据库损坏的情况。但实际上，在这种情况 下很可能你的硬盘已经不能使用，或者发生了其他的不可恢复的硬件错误。

设置为synchronous OFF (0)时，SQLite在传递数据给系统以后直接继续而不暂停。若运行SQLite的应用程序崩溃， 数据不会损伤，但在系统崩溃或写入数据时意外断电的情况下数据库可能会损坏。另一方面，在synchronous OFF时 一些操作可能会快50倍甚至更多。**在SQLite 2中，缺省值为NORMAL.而在3中修改为FULL。**

