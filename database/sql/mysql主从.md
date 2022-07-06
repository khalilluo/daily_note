### binlog_format

**① STATEMENT模式（SBR）**

每一条会修改数据的sql语句会记录到binlog中。优点是并不需要记录每一条sql语句和每一行的数据变化，减少了binlog日志量，节约IO，提高性能。缺点是在某些情况下会导致master-slave中的数据不一致(如sleep()函数， last_insert_id()，以及user-defined functions(udf)等会出现问题)

**② ROW模式（RBR）**

不记录每条sql语句的上下文信息，仅需记录哪条数据被修改了，修改成什么样了。而且不会出现某些特定情况下的存储过程、或function、或trigger的调用和触发无法被正确复制的问题。缺点是会产生大量的日志，尤其是alter table的时候会让日志暴涨。

**③ MIXED模式（MBR）**

以上两种模式的混合使用，一般的复制使用STATEMENT模式保存binlog，对于STATEMENT模式无法复制的操作使用ROW模式保存binlog，MySQL会根据执行的SQL语句选择日志保存方式。



### GTID配置

```sql
# 1、导出主数据库结构及数据到从数据库
# 2、主数据库的写，从数据库的slave；

# 3、停止已有slave
stop slave;

# 4、在新的从数据库加上配置skip-slave-start=0，避免读到binlog
skip-slave-start=0

# 5、然后配置数据
reset slave;
# 6、将删除日志索引文件中记录的所有binlog文件，创建一个新的日志文件 起始值从000001 开始
reset master;


```