

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