编译：

go build -o libgoloader.so -buildmode=c-shared . 生成头文件和动态库CPP可以直接链接使用



需要在导出函数前添加//export func_name



可以在接口函数内调用goroutines

