### 生成jwt token

```go
package Middlewares

github.com/dgrijalva/jwt-go


type MyClaims struct {
   Username string `json:"username"`	// 可以多個自定義
   jwt.StandardClaims	// 必須有的成員
}

const TokenExpireDuration = time.Hour * 24 //设置过期时间

var Secret = []byte("secret") //密码自行设定
var jwtSecret = []byte(os.Getenv("JWT_SECRET")) // 也可以使用這個

func GenToken(username string) (string, error) {
    // 这里使用的是自定义结构体的方式床架claims，也可以使用jwt.MapClaims结构体
	/*
		claims := jwt.MapClaims{} // 其实就是个map
		claims["uid"] = userId
	*/
    
   // 创建一个我们自己的声明
   c := MyClaims{
      username, // 自定义字段
      jwt.StandardClaims{
         ExpiresAt: time.Now().Add(TokenExpireDuration).Unix(), // 过期时间
         Issuer:    "superxon",                                 // 签发人
      },
   }
   // 使用指定的签名方法创建签名对象
   token := jwt.NewWithClaims(jwt.SigningMethodHS256, c)
   // 使用指定的secret签名并获得完整的编码后的字符串token
   return token.SignedString(Secret)
}

```

### 验证用户密码并把生成的jwt token返回给客户端保存

```go
type Profile struct {
   Username    string `db:"username"`
   Password    string `db:"password"`
}

func AuthLoginHandler(c *gin.Context) {
   // 用户发送用户名和密码过来
   var user User.Profile
   err := c.ShouldBindJSON(&user)
   if err != nil {
      c.JSON(http.StatusBadRequest, gin.H{
         "code": 2001,
         "msg":  "无效的参数",
      })
      return
   }
    
   // 校验用户名和密码是否正确
   _, err := getProfile(user.Username)
   if err != nil {
       c.JSON(http.StatusNotFound, gin.H{
          "code": 2003,
          "msg":  "用户不存在",
       })
       return
   }

   tokenString, _ := Middlewares.GenToken(user.Username)
   c.JSON(http.StatusOK, gin.H{
       "code":     2000,
       "msg":      "success",
       "Token":    tokenString,
       "username": profile.Username,
   })
}

```

### 接收请求（Headers中放入`authorization`=jwt token） JWT验证的中间件

```go
// ParseToken 解析JWT
func ParseToken(tokenString string) (*MyClaims, error) {
   // 解析token
   token, err := jwt.ParseWithClaims(tokenString, &MyClaims{}, func(token *jwt.Token) (i interface{}, err error) {
      return Secret, nil	// 這個Secret就是全局的密碼
   })
   if err != nil {
      return nil, err
   }
   if claims, ok := token.Claims.(*MyClaims); ok && token.Valid { // 校验token
      return claims, nil
   }
   return nil, errors.New("invalid token")
}

```

### 驗證中間件

```go
// JWTAuthMiddleware 基于JWT的认证中间件--验证用户是否登录
func JWTAuthMiddleware() func(c *gin.Context) {
   return func(c *gin.Context) {
      
      authHeader := c.Request.Header.Get("authorization") //authHeader := c.GetHeader("Authorization")
      if authHeader == "" {
         c.JSON(http.StatusUnauthorized, gin.H{
            "code": 2003,
            "msg":  "请求头中auth为空",
         })
         c.Abort()
         return
      }
      // 按空格分割
      parts := strings.Split(authHeader, ".")
      if len(parts) != 3 {
         c.JSON(http.StatusUnauthorized, gin.H{
            "code": 2004,
            "msg":  "请求头中auth格式有误",
         })
         c.Abort()
         return
      }
      mc, ok := ParseToken(authHeader, Secret)	// 第二個參數是密碼
      if ok == false {
         c.JSON(http.StatusUnauthorized, gin.H{
            "code": 2005,
            "msg":  "无效的Token",
         })
         c.Abort()
         return
      }
      m := mc.(jwt.MapClaims)
      // 将当前请求的username信息保存到请求的上下文c上
      c.Set("username", m["username"])
      c.Next() // 后续的处理函数可以用过c.Get("username")来获取当前请求的用户信息
   }
}

```

