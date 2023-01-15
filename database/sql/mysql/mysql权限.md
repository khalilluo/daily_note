mysqldump 导出

mysql进入数据库后，source导出的文件导入数据库

### 权限

```SQL
# mysql8.0之前的版本能够使用grant在受权的时候隐式的建立用户，mysql8.0之后已经不支持，因此必须先建立用户，而后再受权，命令以下mysql

mysql> CREATE USER 'root'@'%' IDENTIFIED BY '你的密码';
Query OK, 0 rows affected (0.48 sec)

mysql> grant all privileges on *.* to 'root'@'%';
Query OK, 0 rows affected (0.48 sec)



-- mysql8部署执行语句
-- 修改数据库密码认证方式（不修改密码则不执行）    
-- 注意大小写？
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
-- root用户设置为可远程连接（注意：需要在mysql数据库下执行）
update user set host='%' where user='root';
-- 给用户授权
grant all privileges on *.* to 'root'@'%' with grant option
-- 创建角色
create role 'role_all'
-- 给角色授权
grant all privileges on *.* to role_all;
-- 给用户添加角色
grant role_all to 'root'@'%';
-- 刷新权限
flush privileges;
```

^1df794



