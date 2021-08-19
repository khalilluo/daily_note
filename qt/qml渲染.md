裁剪会中断批次渲染。切勿在表格内的单元格，`delegate`或者类似的元素中使用裁剪。使用`省略`代替文本裁剪

默认渲染器不执行任何CPU端的视口裁剪或遮挡检测。如果某些内容不可见，则不应该显示，使用`Item::visible`将其设置
为false。不添加这样的逻辑的主要原因是，它增加了额外的成本，这也将损害那些表现良好的应用程序。

尽可能使用不透明图元(ITe)。不透明图元在渲染器中处理速度更快，在GPU上绘制速度更快。例如，即使每个像素都是不透明的，PNG
文件也会经常具有alpha通道。JPG文件始终是不透明的。当图像提供给`QQuickImageProvider`或者使用
`QQuickWindow::createTextureFromImage()`创建图像时，请尽可能使用`QImage::Format_RGB32`格式。

