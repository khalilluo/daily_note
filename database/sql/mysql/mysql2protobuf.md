```shell
# 安装
go install github.com/Mikaelemmmm/sql2pb@latest

# 查看帮助
sql2pb -h

sql2pb -go_package ./pb -host localhost -package pb -password root -port 3306 -schema usercenter -service_name usersrv -user root > usersrv.proto
```