## console控制台

在生成后事件命令行中添加以下命令运行过程会有终端输出
editbin /SUBSYSTEM:CONSOLE $(OUTDIR)\$(ProjectName).exe

链接器》系统选择/subsystem:windows，高级将入口点设置为mainCRTStartup(入口点为main函数)