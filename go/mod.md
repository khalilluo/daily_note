1、生成go mod：在项目根目录

```
go mod init proName, 
go mod tidy		// 下载依赖包
go mod vendor	// 这个命令是将项目依赖的包，放到项目的 vendor 目录中
```





2、添加依赖：require some_package，可能会有相关依赖

