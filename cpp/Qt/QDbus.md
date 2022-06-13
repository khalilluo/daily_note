1、信号的发射端要想信号发射到DBus上去，在对象的构造函数中必须，注册对象自己，必须使用this指针。例如：

   ```cpp
   // 类中的所有的信号都可以直接用emit发射到DBus总线上，一个路径只能注册一个对象，需要使用unregisterObject注销
   connection.registerobject(“/com/dbus/path”,this);
   ```

2、绑定信号

```c++
// 创建接口时，接口的头两个参数必须为空？
org::example::chat *iface = new org::example::chat(QString(), QString(), QDBusConnection::sessionBus(), this);

// 以下两种连接方式效果相同，都可以将接口的message信号绑定到槽上，第一种方式的对象需继承QDBusAbstractInterface
// 当使用QDBus的绑定时，不论前两个参数是否为空，都可以正常的接受到信号?
connect(iface, SIGNAL(message(QString,QString)), this, SLOT(messageSlot(QString,QString)));
QDBusConnection::sessionBus().connect(QString(), QString(), "org.example.chat", "message", \
                                      this, SLOT(messageSlot(QString,QString)));

```

3、只有注册到DBus上去对象才能接受到DBus上的信号，其他的对象要接受DBus上的信号必须通过这个注册的对象将信号转发出来

```c++
// 接收信号的对象可以不继承第一种方式的对象需继承QDBusAbstractInterface
QObject::connect(myInterface,SIGNAL(queryReply(int)),this,SIGNAL(queryResult(int)));
```

4、发送消息

```c++
    // 方式1、发送绑定对象的信号
	emit message(m_nickname, messageLineEdit->text());

	// 使用QDBusConnection发送QDBusMessage消息对象
    QDBusMessage msg = QDBusMessage::createSignal("/", "org.example.chat", "message");
    msg << m_nickname << messageLineEdit->text();
    QDBusConnection::sessionBus().send(msg);
    messageLineEdit->setText(QString());
```



#### C++中应用
[[dbus]]