声明队列是幂等的——只有在它不存在的情况下才会创建它

```go
q, err := ch.QueueDeclare(
  "hello", // name
  false,   // durable
  false,   // delete when unused
  false,   // exclusive
  false,   // no-wait
  nil,     // arguments
)
```



amqp消息必须确认，如果是true手动确认需要在拿到消息后调用Ack,否则服务端当做这条消息未处理会重发

```go
msgs, err := ch.Consume(
  q.Name, // queue
  "",     // consumer
  false,  // auto-ack  自动消息确认 
  false,  // exclusive
  false,  // no-local
  false,  // no-wait
  nil,    // args
)
```





我们可以设置预取计数值为1。告诉RabbitMQ一次只向一个worker发送一条消息。换句话说，在处理并确认前一个消息之前，不要向工作人员发送新消息。

```go
err = ch.Qos(
  1,     // prefetch count 需注意worker工作不及时可能填满服务队列
  0,     // prefetch size
  false, // global
)
failOnError(err, "Failed to set QoS")
```