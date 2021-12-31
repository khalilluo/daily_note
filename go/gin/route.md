

冒号`:`加上一个参数名组成路由参数。可以使用c.Params的方法读取其值。当然这个值是字串string。诸如`/user/rsj217`，和`/user/hello`都可以匹配，而`/user/`和`/user/rsj217/`不会被匹配

```go
  router.GET("/user/:name", func(c *gin.Context) {
        name := c.Param("name")
        c.String(http.StatusOK, "Hello %s", name)
    })
```

除了`:`，gin还提供了`*`号处理参数，`*`号能匹配的规则就更多。*可以匹配多个，但只能放到最后

```css
    
    // 此 handler 将匹配 /user/john/ 和 /user/john/send
    // 如果没有其他路由匹配 /user/john，它将重定向到 /user/john/
	router.GET("/user/:name/*action", func(c *gin.Context) {
        name := c.Param("name")
        action := c.Param("action")
        message := name + " is " + action
        c.String(http.StatusOK, message)
    })
```



```cpp
curl http://127.0.0.1:8000/welcome
Hello Guest %                                                                
curl http://127.0.0.1:8000/welcome\?firstname\=中国
Hello 中国 %                                                                  
curl http://127.0.0.1:8000/welcome\?firstname\=中国\&lastname\=天朝
Hello 中国 天朝%                                                             
curl http://127.0.0.1:8000/welcome\?firstname\=\&lastname\=天朝
Hello  天朝%
    ☁  ~  curl http://127.0.0.1:8000/welcome\?firstname\=%E4%B8%AD%E5%9B%BD
Hello 中国 %
```