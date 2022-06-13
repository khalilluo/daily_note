binlog-do-db：在主库指定binlog日志记录哪一个db。
binlog-ignore-db：在主库指定binlog日志过滤哪一个db
``` shell
# 指定两个库写binlog
binlog-do-db=test  
binlog-do-db=xiaobin
```

replicate-do-db: 在从库上配置，指定slave要复制哪个库
replicate-ignore-db：在从库上配置，指定slave要过滤复制哪个库
``` shell
# 指定两个库写binlog
replicate-do-db=test  
replicate-do-db=xiaobin
```

*如在Master（主）服务器上设置 replicate_do_db=test（my.conf中设置）  
use mysql;  
update test.table1 set ......  
那么Slave（从）服务器上第二句将不会被执行

以上两个参数不建议使用，使用表级别过滤
- --replicate-do-table
- --replicate-wild-do-table
- --replicate-ignore-table
- --replicate-wild-ignore-table

https://www.cnblogs.com/itfenqing/p/4429436.html

***
log-slave-updates：从库从主库复制的数据是否写入log-bin。只有从库是其他库的主库时需要设置为true


relay_log：指定relay_log目录或者文件名称，不指定则默认在datadir下。通常不需要指定
relay_log_recovery：当slave从库宕机后，假如relay-log损坏了，导致一部分中继日志没有处理，则自动放弃所有未执行的relay-log，并且重新从master上获取日志，这样就保证了relay-log的完整性。默认情况下该功能是关闭的，将relay_log_recovery的值设置为 1时，可在slave从库上开启该功能，建议开启

https://blog.csdn.net/qwe123147369/article/details/108670385

server-id：如果配置数据库集群时，ID必须不一致。