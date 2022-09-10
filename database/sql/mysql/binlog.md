### 开启
配置中添加log-bin=mysql-bin指定基础名称就是开启

```mysql
mysql> show binlog events;   #只查看第一个binlog文件的内容`

mysql> show binlog events` `in` `'mysql-bin.000002'``;#查看指定binlog文件的内容`

mysql> show binary logs;  #获取binlog文件列表`

mysql> show master status； #查看当前正在写入的binlog文件`
```

### 查看
```mysql

-- 查看binlog的目录
show global variables like “%log_bin%”;

-- 删除当前的binlog文件
reset master;

-- 删除slave的中继日志relay_log
reset slave;
```

### 写时机
对支持事务的引擎如InnoDB而言，必须要提交了事务才会记录binlog。binlog 什么时候刷新到磁盘跟参数 sync_binlog 相关。

- 如果设置为0，则表示MySQL不控制binlog的刷新，由文件系统去控制它缓存的刷新；
- 如果设置为不为0的值，则表示每 sync_binlog 次事务，MySQL调用文件系统的刷新操作刷新binlog到磁盘中。
- 设为1是最安全的，在系统故障时最多丢失一个事务的更新，但是会对性能有所影响。

如果 sync_binlog=0 或 sync_binlog大于1，当发生电源故障或操作系统崩溃时，可能有一部分已提交但其binlog未被同步到磁盘的事务会被丢失，恢复程序将无法恢复这部分事务。高版本（5.7.7）mysql默认1


### 格式binlog_format

**STATEMENT模式（SBR）**
每一条会修改数据的sql语句会记录到binlog中。优点是并不需要记录每一条sql语句和每一行的数据变化，减少了binlog日志量，节约IO，提高性能。缺点是在某些情况下会导致master-slave中的数据不一致(如sleep()函数， last_insert_id()，以及user-defined functions(udf)等会出现问题)

**ROW模式（RBR）**
不记录每条sql语句的上下文信息，仅需记录哪条数据被修改了，修改成什么样了。而且不会出现某些特定情况下的存储过程、或function、或trigger的调用和触发无法被正确复制的问题。缺点是会产生大量的日志，尤其是alter table的时候会让日志暴涨。

**MIXED模式（MBR）**
以上两种模式的混合使用，一般的复制使用STATEMENT模式保存binlog，对于STATEMENT模式无法复制的操作使用ROW模式保存binlog，MySQL会根据执行的SQL语句选择日志保存方式。

建议使用ROW，牺牲部分性能保证主从数据完整性

### 分析
``` mysql
mysqlbinlog -vv --base64-output=decode-rows --skip-gtids=true --database=dualmode mysql_bin.000006 > 06.log

a、提取指定的binlog日志  
# mysqlbinlog /opt/data/APP01bin.000001  
# mysqlbinlog /opt/data/APP01bin.000001|grep insert  
/*!40019 SET @@session.max_insert_delayed_threads=0*/;  
insert into tb values(2,'jack')  
  
b、提取指定position位置的binlog日志  
# mysqlbinlog --start-position="120" --stop-position="332" /opt/data/APP01bin.000001  
  
c、提取指定position位置的binlog日志并输出到压缩文件  
# mysqlbinlog --start-position="120" --stop-position="332" /opt/data/APP01bin.000001 |gzip >extra_01.sql.gz  
  
d、提取指定position位置的binlog日志导入数据库  
# mysqlbinlog --start-position="120" --stop-position="332" /opt/data/APP01bin.000001 | mysql -uroot -p  
  
e、提取指定开始时间的binlog并输出到日志文件  
# mysqlbinlog --start-datetime="2014-12-15 20:15:23" /opt/data/APP01bin.000002 --result-file=extra02.sql  
  
f、提取指定位置的多个binlog日志文件  
# mysqlbinlog --start-position="120" --stop-position="332" /opt/data/APP01bin.000001 /opt/data/APP01bin.000002|more  
  
g、提取指定数据库binlog并转换字符集到UTF8  
# mysqlbinlog --database=test --set-charset=utf8 /opt/data/APP01bin.000001 /opt/data/APP01bin.000002 >test.sql  
  
h、远程提取日志，指定结束时间   
# mysqlbinlog -urobin -p -h192.168.1.116 -P3306 --stop-datetime="2014-12-15 20:30:23" --read-from-remote-server mysql-bin.000033 |more  
  
i、远程提取使用row格式的binlog日志并输出到本地文件  
# mysqlbinlog -urobin -p -P3606 -h192.168.1.177 --read-from-remote-server -vv inst3606bin.000005 >row.sql
```


使用grep -i -B -A 再次过滤 
``` shell
mysqlbinlog -vv --base64-output=decode-rows --skip-gtids=true --database=dualmode | grep -A1 -B3 -i -E '^insert|^update|^delete|^replace|^alter' | grep -A1 -B3 mytable > log.log
```