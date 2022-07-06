### flutter

1. 在web目录下修改文件链接目录，包括icon/js目录
2. 编译 flutter build web --web-renderer html 不使用Canvaskit渲染，性能一般但不需要科学上网
3. 将整个web目录拷至gin运行目录下



### Gin

1. LoadHTMLFiles指定index.html文件路径
2. StaticFS指定静态文件夹目录，包括js/icon和字体文件目录
3. 可以自行修改文件目录结构，在第二部修改时注意添加对应的目录即可

