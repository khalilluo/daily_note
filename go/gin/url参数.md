- URL参数可以通过DefaultQuery()或Query()方法获取
- DefaultQuery()若参数不村则，返回默认值，Query()若不存在，返回空串
- API ? name=zs

```go
package main

import (
    "fmt"
    "net/http"

    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()
    r.GET("/user", func(c *gin.Context) {
        //指定默认值
        //http://localhost:8080/user 才会打印出来默认的值
        name := c.DefaultQuery("name", "枯藤")
        // name := c.Query("name") // 参数为空的话返回空字符串
        c.String(http.StatusOK, fmt.Sprintf("hello %s", name))
    })
    r.Run()
}

// 輸入 localhost:8080/user 返回hello枯藤
// 輸入 localhost:8080/user?name="輸入參數" 返回hello 輸入參數

```

### 多個參數

用&拼接第二個開始的參數

http://localhost:8001/download?fileName=mainctrl.h&id=cppClient&type=text