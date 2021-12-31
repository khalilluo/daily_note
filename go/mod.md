1、生成go mod：在项目根目录

```
go mod init proName, 
go mod tidy		// 下载依赖包 拉取缺少的模块，移除不用的模块。
go mod vendor	// 这个命令是将项目依赖的包，放到项目的 vendor 目录中
go mod download  // 下载依赖包。
go mod verify  // 检验依赖。
go mod graph   // 打印模块依赖图。

其他命令，可以执行 `go mod` ，查看即可。
```



2、添加依赖：require some_package，可能会有相关依赖

