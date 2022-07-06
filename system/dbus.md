### DBus分为两种类型：

-   system bus(系统总线)，用于系统(Linux)和用户程序之间进行通信和消息的传递；
-   session bus(回话总线)，用于桌面(GNOME, KDE等)用户程序之间进行通信。

**DBus进程间通信主要有三层架构**：

1. 底层接口层：主要是通过libdbus这个函数库，给予系统使用DBus的能力。 
2. 总线层：主 要Message bus daemon这个总线守护进程提供的，在Linux系统启动时运行，负责进程间的消息路由和传递，其中包括Linux内核和Linux桌面环境的消息传 递。总线守护进程可同时与多个应用程序相连，**并能把来自一个应用程序的消息路由到0或者多个其他程序**。 
3. 应用封装层：通过一系列基于特定应用程序框架将DBus的底层接口封装成友好的Wrapper库，供不同开发人员使用。比如libdbus-glib, libdbus-python.

**DBus的三大优点**：

- **低延迟**：DBus一开始就是用来设计成避免来回传递和允许异步操作的。因此虽然在Application和Daemon之间是通过socket实现的，但是又去掉了socket的循环等待，保证了操作的实时高效。

- **低开销**：**DBus使用一个二进制的协议**。因为DBus是主要用来机器内部的IPC,而不是为了网络上的IPC机制而准备的.

- ***高可用性**：DBus是基于消息机制而不是字节流机制

**Bus Name**

按字面理解为总线名称貌似不是很贴切，应该是一个**连接名称**，主要是用来标识一个应用和消息总线的连接。从上图可以看出来，总线名称主要分为两类

"org.kde.StatusNotifierWatcher"这种形式的称为**公共名**（well-knownname）

":1.3"这种形式的称为**唯一名**（Unique Name）

**公共名**提供众所周知的服务。**其他应用通过这个名称来使用名称对应的服务**。可能有多个连接要求提供同个公共名的服 务，即多个应用连接到消息总线，要求提供同个公共名的服务。**消息总线会把这些连接排在链表中**，并选择一个连接提供公共名代表的服务。可以说这个提供服务的 连接拥有了这个公共名。如果这个连接退出了，消息总线会从链表中选择下一个连接提供服务。

**唯一名**以“:”开头，“:”后面通常是圆点分隔的两个数字，例如“:1.0”。每个连接都有一个唯一名。在一个 消息总线的生命期内，不会有两个连接有相同的唯一名。拥有公众名的连接同样有唯一名

**每个连接都有一个唯一名，但不一定有公共名。**

只有唯一名而没有公共名叫做**私有连接**，因为它们没有提供可以通过公共名访问的服务

**Object Paths**

“org.kde.StatusNotifierWatcher”这个连接中有三个Object Paths，标识这个连接中提供了三个不同的服务，每个Object Paths表示一个服务。这个路径在连接中是唯一的。

**Interfaces**

在每个Object Paths下都包含有多个接口（Interfaces），举例如下接口：

org.freedesktop.DBus.Introspectable

org.freedesktop.DBus.Properties

org.kde.StatusNotifierWatcher

红色的两个是消息总线提供的标准接口，而剩下的一个是需要具体的应用去实现的。

**Methods和Signals**

Methods表示可以被具体调用的方法

Signals则表示的是信号，此信号可以被广播，而连接了这个信号的对象在接收到信号时就可以进行相应的处理。和Qt中的信号应该是一个意思。

**Native Objects and Object Paths**
在不同的编程语言中，都定义了一些“对象”，如java中的 java.lang.Object，GLIB中的GObject，QT中的QObject等 等。D-BUS的底层接口，和libdbus API相关，是没有这些对象的概念的，**它提供的是一种叫对象路径（object path）**，用于让高层接口绑定到各个对象中去，允许远端应用程序指向它们。object path就像是一个文件路径，可以叫做/org/kde/kspread/sheets/3/cells/4/5等。

**Proxies**
代理对象用于模拟在另外的进程中的远端对象，代理对象像是一个正常的普通对象。d-bus的底层接口必须手动创建方法调用的 消息，然后发送，同时必须手动 接受和处理返回的消息。**高层接口可以使用代理来替换这些，当调用代理对象的方法时，代理内部会转换成dbus的方法调用，等待消息返回，对返回结果解包， 返回给相应的方法**。可以看看下面的例子，使用dbus底层接口编写的代码：

```c++
Message message = new Message("/remote/object/path", "MethodName", arg1, arg2);
Connection connection = getBusConnection();
connection.send(message);
Message reply = connection.waitForReply(message);
if (reply.isError()) {`

} else {undefined
	Object returnValue = reply.getReturnValue();
}
```

使用代理对象编写的代码：

```c++
Proxy proxy = new Proxy(getBusConnection(), "/remote/object/path");
Object returnValue = proxy.MethodName(arg1, arg2);
```

客户端代码减少很多。

Bus Names
当一个应用程序连接上bus daemon时，daemon会分配一个唯一的名字给它。以冒号（:）开始，这些名字在daemon的生命周期中是不会改变的，可以认为这些名字就是一个 IP地址。当这个名字映射到应用程序的连接上时，应用程序可以说拥有这个名字。同时应用可以声明额外的容易理解的名字，比如可以取一个名字 com.mycompany.TextEditor，可以认为这些名字就是一个域名。**其他应用程序可以往这个名字发送消息，执行各种方法**。

名字还有第二个重要的用途，可以用于跟踪应用程序的生命周期。当**应用退出（或者崩溃）时，与bus的连接将被OS**内核关掉，bus将会发送通知，告诉剩余的应用程序，该程序已经丢失了它的名字。**名字还可以检测应用是否已经启动，这往往用于只能启动一个实例的应用**。

Addresses
**使用d-bus的应用程序既可以是server也可以是client**，server监听到来的连接，client连接到 server，一旦连接建立，消息 就可以流转。**如果使用dbus daemon，所有的应用程序都是client**，daemon监听所有的连接，应用程序初始化连接到daemon。

**dbus地址指明server将要监听的地方，client将要连接的地方**，例如，地址：unix:path=/tmp/abcdef表明 server将在/tmp/abcdef路径下监听unix域的socket，client也将连接到这个socket。一个地址也可以指明是 TCP/IP的socket，或者是其他的。

当使用bus daemon时，libdbus会从环境变量中（DBUS_SESSION_BUS_ADDRESS）自动认识“会话daemon”的地址。如果是系统 daemon，它会检查指定的socket路径获得地址，也可以使用环境变量（DBUS_SESSION_BUS_ADDRESS）进行设定。

**当dbus中不使用daemon时，需要定义哪一个应用是server，哪一个应用是client，同时要指明server的地址，这不是很通常的做法。**
