RabbitMQ消息模型的核心理念是：发布者（producer）不会直接发送任何消息给队列。事实上，发布者（producer）甚至不知道消息是否已经被投递到队列。

发布者（producer）只需要把消息发送给一个交换机（exchange）。交换机非常简单，它一边从发布者方接收消息，一边把消息推送到队列。交换机必须知道如何处理它接收到的消息，是应该推送到指定的队列还是是多个队列，或者是直接忽略消息。这些规则是通过交换机类型（exchange type）来定义的。

![](./image/exchanges.png)

### 类型

有几个可供选择的交换器类型：`direct`, `topic`, `headers`和`fanout`

```go
err = ch.ExchangeDeclare(
  "logs",   // name
  "fanout", // type
  true,     // durable
  false,    // auto-deleted
  false,    // internal
  false,    // no-wait
  nil,      // arguments
)
```

####  匿名的交换器

前面的教程中我们对交换机一无所知，但仍然能够发送消息到队列中。因为我们使用了命名为空字符串("")的匿名交换机。 回想我们之前是如何发布一则消息：

```go
 err = ch.Publish(
  "",     // exchange
  q.Name, // routing key
  false,  // mandatory
  false,  // immediate
  amqp.Publishing{
    ContentType: "text/plain",
    Body:        []byte(body),
})
```

exchange参数就是交换机的名称。空字符串代表默认或者匿名交换机，消息将会根据指定的`routing_key`分发到指定的队列。



### Topic

发送到`topic`交换机的消息不可以携带随意`routing_key`，它的routing_key必须是一个由`.`分隔开的词语列表

binding key也必须拥有同样的格式。`topic`交换机背后的逻辑跟`direct`交换机很相似 —— 一个携带着特定routing_key的消息会被topic交换机投递给绑定键与之想匹配的队列。但是它的binding key和routing_key有两个特殊应用方式：

- `*` (星号) 用来表示一个单词.
- `#` (井号) 用来表示任意数量（零个或多个）单词。

- 如果我们违反约定，发送了一个携带有一个单词或者四个单词（`"orange"` or `"quick.orange.male.rabbit"`）的消息时，发送的消息不会投递给任何一个队列，而且会丢失掉
- 当一个队列的binding key为 "#"（井号） 的时候，这个队列将会无视消息的routing key，接收所有的消息
- 如果队列匹配key多次，publish一次消息队列也只会接收一次





注意 publish 的routing key 和 Binding 的routing key（也可以成为binding key）





###  绑定（Bindings）

前面的例子，我们已经创建过绑定（bindings），代码如下：

```go
err = ch.QueueBind(
  q.Name, // queue name
  "",     // routing key
  "logs", // exchange
  false,
  nil)
```

绑定（binding）是指交换机（exchange）和队列（queue）的关系。可以简单理解为：这个队列（queue）对这个交换机（exchange）的消息感兴趣

```go
err = ch.QueueBind(
  q.Name,    // queue name
  "black",   // routing key
  "logs",    // exchange
  false,
  nil)
```

绑定键的意义取决于交换机（exchange）的类型。我们之前使用过`fanout` 交换机会忽略这个值



publish的routing key





