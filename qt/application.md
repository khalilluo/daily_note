## QCoreApplication(core) ->  QGuiApplication(gui) -> QApplication(widgets)



QCoreApplication定义在core模块中，为应用程序提供了一个非gui的事件循环；

QGuiApplication定义在gui模块中，提供了额外的gui相关的设置，比如桌面设置，风格，字体，调色板，剪切板，光标；

QApplication定义在widgets模块中，是QWidget相关的，能设置双击间隔，按键间隔，拖拽距离和时间，滚轮滚动行数等，能获取桌面，激活的窗口，模式控件，弹跳控件等。



## 应用场景：

如果你的应用程序是无界面的，直接使用QCoreApplication即可，如果是gui相关，但没有使用widgets模块的就使用QGuiApplication，否则使用QApplication。



ChartView组件必须使用QApplication才能加载