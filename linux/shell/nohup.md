## 结论
### 使用&后台运行程序：

结果会输出到终端
- 使用Ctrl + C发送SIGINT信号，程序免疫
- 关闭session发送SIGHUP信号，程序关闭


### 使用nohup运行程序：

结果默认会输出到nohup.out
- 使用Ctrl + C发送SIGINT信号，程序关闭
- 关闭session发送SIGHUP信号，程序免疫

### 日后使用
平日线上经常使用nohup和&配合来启动程序nohup ./test &：
- 同时免疫SIGINT和SIGHUP信号