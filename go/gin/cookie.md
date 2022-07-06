```go
import (
    "fmt"
    "github.com/gin-gonic/gin"
)
func main() {
    router := gin.Default()
    router.GET("/cookie", func(c *gin.Context) {
        // 獲取gin_cookie
        cookie, err := c.Cookie("gin_cookie")
        if err != nil {
            // 如果沒有則設置
            cookie = "NotSet"
            c.SetCookie("gin_cookie", "test", 3600, "/", "localhost", false, true)
        } else {
            // 如果有則刷新該cookie超時時間
            c.SetCookie("gin_cookie", cookie, 3600, "/", "localhost", false, true)
        }
        fmt.Printf("Cookie value: %s \n", cookie)
    })
    router.Run()
}
```

