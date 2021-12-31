## 中间件


```go
//自定义中间件第1种定义方式
func CustomRouterMiddle1(c *gin.Context)  {
	t := time.Now()
	fmt.Println("我是自定义中间件第1种定义方式---请求之前")
	//在gin上下文中定义一个变量
	c.Set("example", "CustomRouterMiddle1")
	//请求之前
	c.Next()
	fmt.Println("我是自定义中间件第1种定义方式---请求之后")
	//请求之后
	//计算整个请求过程耗时
	t2 := time.Since(t)
	log.Println(t2)

}

//自定义中间件第2种定义方式
func CustomRouterMiddle2() gin.HandlerFunc{
	return func(c *gin.Context) {
		t := time.Now()
		fmt.Println("我是自定义中间件第2种定义方式---请求之前")
		//在gin上下文中定义一个变量
		c.Set("example", "CustomRouterMiddle2")
		//请求之前
		c.Next()
		fmt.Println("我是自定义中间件第2种定义方式---请求之后")
		//请求之后
		//计算整个请求过程耗时
		t2 := time.Since(t)
		log.Println(t2)
	}
}

func MiddleMain(ctx *gin.Context){
	fmt.Println("Main Middleware")
}

func main() {
	r := gin.New()
	
    // 可注册多个全局中间件，按注册顺序调用
    // r.Use(MiddleMain) // 放开注释全部都会进到这个中间件内，都打印"Main Middleware"?
	//测试时下面两个中间件选择一个，注释一个
	r.Use(CustomRouterMiddle1)  // 全局
	//r.Use(CustomRouterMiddle2())

    // 输入 http://localhost:8080/test
 	
	r.GET("/test", func(c *gin.Context) {
		example := c.MustGet("example").(string)
		//
		log.Println("/test", example)
	})

	// 监听本地8080端口
	r.Run(":8080")
}

/* 输出
# 因为调用表示next执行下个handler 
我是自定义中间件第1种定义方式---请求之前
2021/12/23 17:03:15 /test CustomRouterMiddle1 # 这一条跟下一条在不同的地方打印，先先抢到时间片则先打印谁
我是自定义中间件第1种定义方式---请求之后

# 如果注释next的话
我是自定义中间件第1种定义方式---请求之前
我是自定义中间件第1种定义方式---请求之后
2021/12/23 17:03:15 /test CustomRouterMiddle1

# 如果在next那改为abort的话，则不进入下个handler
我是自定义中间件第1种定义方式---请求之前
我是自定义中间件第1种定义方式---请求之后
*/
```

## 路由中间件

```go
func GroupRouterGoodsMiddle1(c *gin.Context)  {
	fmt.Println("我是goods路由组中间件1")
}

func GroupRouterGoodsMiddle2(c *gin.Context) {
	fmt.Println("我是goods路由组中间件2")
}

func GroupRouterOrderMiddle1(c *gin.Context) {
	fmt.Println("我是order路由组中间件1")
}

func GroupRouterOrderMiddle2(c *gin.Context) {
	fmt.Println("我是order路由组中间件2")
}

func main() {
	//创建一个无中间件路由
	router := gin.New()
	router.Use(gin.Logger())

	//第1种路由组使用方式 可以添加多个处理函数
	router.Group("/goods", GroupRouterGoodsMiddle1, GroupRouterGoodsMiddle2)
	router.GET("/goods/add", func(context *gin.Context) {
		fmt.Println("/goods/add")
	})


    // 
	//第2种路由组使用方式
	orderGroup := router.Group("/order", func(context *gin.Context) {
		fmt.Println("order 中间件")
	})
    // 和上面的直接添加中间件的方式一样	
	orderGroup.Use(GroupRouterOrderMiddle1, GroupRouterOrderMiddle2)
    
	{
        fmt.Println("注册 order 中间件")
		orderGroup.GET("/add", func(context *gin.Context) {
			fmt.Println("/order/add")

		})

		orderGroup.GET("/del", func(context *gin.Context) {
			fmt.Println("/order/del")

		})

		//orderGroup下再嵌套一个testGroup
		testGroup:=orderGroup.Group("/test", func(context *gin.Context) {
			fmt.Println("order/test下的中间件")
		})

		testGroup.GET("/test1", func(context *gin.Context) {
			fmt.Println("order/test/test1的函数")
		})
	}

	router.Run()
}

/* 	
输入前已有打印 注册 order 中间件，后面只是一个语句块
输入 http://localhost:8001/order/test/test1
输出
	
	order 中间件
	我是order路由组中间件1
	我是order路由组中间件2
	
	order/test下的中间件
	order/test/test1的函数

```



**结论1:** 填写正确的路由组和路由，中间件先执行，并按照传入函数的顺序执行。
**结论2:** 填写正确的路由组，错误的路由，中间件不执行，并返回404错误。即输入http://localhost:8001/order/test/ff不会有任何输出
**结论3:** 路由组中还可以嵌套路由组
**结论4：** 全局中间件 > 路由组中间件 > 路由中间件

```go
func main() {
    // 新建一个没有任何默认中间件的路由
    r := gin.New()
    // 全局中间件
    // Logger 中间件将日志写入 gin.DefaultWriter，即使你将 GIN_MODE 设置为 release。
    // By default gin.DefaultWriter = os.Stdout
    r.Use(gin.Logger())
    // Recovery 中间件会 recover 任何 panic。如果有 panic 的话，会写入 500。
    r.Use(gin.Recovery())
    // 你可以为每个路由添加任意数量的中间件。
    r.GET("/benchmark", MyBenchLogger(), benchEndpoint)
    // 认证路由组
    // authorized := r.Group("/", AuthRequired())
    // 和使用以下两行代码的效果完全一样:
    authorized := r.Group("/")
    // 路由组中间件! 在此例中，我们在 "authorized" 路由组中使用自定义创建的 
    // AuthRequired() 中间件
    authorized.Use(AuthRequired())
    {
        authorized.POST("/login", loginEndpoint)
        authorized.POST("/submit", submitEndpoint)
        authorized.POST("/read", readEndpoint)
        // 嵌套路由组
        testing := authorized.Group("testing")
        testing.GET("/analytics", analyticsEndpoint)
    }
    // 监听并在 0.0.0.0:8080 上启动服务
    r.Run(":8080")
}
```



## 在中间件中使用 Goroutine

当在中间件或 handler 中启动新的 Goroutine 时，**不能**使用原始的上下文，必须使用只读副本

```go
func main() {
    r := gin.Default()
    r.GET("/long_async", func(c *gin.Context) {
        // 创建在 goroutine 中使用的副本
        cCp := c.Copy()
        go func() {
            // 用 time.Sleep() 模拟一个长任务。
            time.Sleep(5 * time.Second)
            // 请注意您使用的是复制的上下文 "cCp"，这一点很重要
            log.Println("Done! in path " + cCp.Request.URL.Path)
            cCp.String(http.StatusOK, "gorou") // 此處引起panic
        }()
    })
    r.GET("/long_sync", func(c *gin.Context) {
        // 用 time.Sleep() 模拟一个长任务。
        time.Sleep(5 * time.Second)
        // 因为没有使用 goroutine，不需要拷贝上下文
        log.Println("Done! in path " + c.Request.URL.Path)
    })
    // 监听并在 0.0.0.0:8080 上启动服务
    r.Run(":8080")
}
```

