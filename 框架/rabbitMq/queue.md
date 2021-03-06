###  临时队列

在`amqp`客户端中，当我们将队列名称作为空字符串提供时，我们创建一个具有生成名称的非持久队列：

```go
q, err := ch.QueueDeclare(
  "",    // name
  false, // durable
  false, // delete when usused
  true,  // exclusive
  false, // no-wait
  nil,   // arguments
)
```

该方法返回时，队列实例包含RabbitMQ生成的随机队列名称。例如，它可能看起来像`amq.gen-JzTY20BRgKO-HjmUJj0wLg`。 当声明它的连接关闭时，队列将被删除，因为它被声明为`exclusive`



### 参数说明

exclusive：排他队列，如果一个队列被声明为排他队列，该队列仅对首次申明它的连接可见，并在连接断开时自动删除。这里需要注意三点：

1. 排他队列是基于连接可见的，同一连接的不同信道是可以同时访问同一连接创建的排他队列；

2. “首次”，如果一个连接已经声明了一个排他队列，其他连接是不允许建立同名的排他队列的，这个与普通队列不同；

3. 即使该队列是持久化的，一旦连接关闭或者客户端退出，该排他队列都会被自动删除的，这种队列适用于一个客户端发送读取消息的应用场景。

   

autoDelete：自动删除，如果该队列没有任何订阅的消费者的话，该队列会被自动删除。这种队列适用于临时队列。

