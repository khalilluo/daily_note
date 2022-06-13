链接：https://zhuanlan.zhihu.com/p/103522811

**功能**

- 支持 JSON/TOML/YAML/HCL/envfile/Java properties 等多种格式的配置文件；
- 可以设置**监听配置文件**的修改，修改时自动加载新的配置；
- 从**环境变量**、**命令行**选项和`io.Reader`中读取配置；
- 从远程配置系统中读取和监听修改，如 etcd/Consul；
- 代码逻辑中显示设置键值。



**使用**

viper 的使用非常简单，它需要很少的设置。设置文件名（`SetConfigName`）、配置类型（`SetConfigType`）和搜索路径（`AddConfigPath`），然后调用`ReadInConfig`。viper会自动根据类型来读取配置。使用时调用`viper.Get`方法获取键值。

```go
  viper.SetConfigName("config")
  viper.SetConfigType("toml")
  viper.AddConfigPath(".")
  viper.SetDefault("redis.port", 6381)
  err := viper.ReadInConfig()
  if err != nil {
    log.Fatal("read config failed: %v", err)
  }

  fmt.Println(viper.Get("app_name"))
  fmt.Println(viper.Get("log_level"))

  fmt.Println("mysql ip: ", viper.Get("mysql.ip"))
```

toml文件

```toml
app_name = "awesome web"

# possible values: DEBUG, INFO, WARNING, ERROR, FATAL
log_level = "DEBUG"

[mysql]
ip = "127.0.0.1"
port = 3306
user = "dj"
password = 123456
database = "awesome"

[redis]
ip = "127.0.0.1"
port = 7381
```



**注意**

- 设置文件名时不要带后缀；
- 搜索路径可以设置多个，viper 会根据设置顺序依次查找；
- viper 获取值时使用`section.key`的形式，即传入嵌套的键名；
- 默认值可以调用`viper.SetDefault`设置。



**读取**

viper 提供了多种形式的读取方法。`Get`方法返回一个`interface{}`的值，使用有所不便。

`GetType`系列方法可以返回指定类型的值。其中，Type 可以为`Bool/Float64/Int/String/Time/Duration/IntSlice/StringSlice`。但是请注意，**如果指定的键不存在或类型不正确，`GetType`方法返回对应类型的零值**。

如果要判断某个键是否存在，使用`IsSet`方法。另外，`GetStringMap`和`GetStringMapString`直接以 map 返回某个键下面所有的键值对，前者返回`map[string]interface{}`，后者返回`map[string]string`。`AllSettings`以`map[string]interface{}`返回所有设置。

```go
  fmt.Println("protocols: ", viper.GetStringSlice("server.protocols"))
  fmt.Println("ports: ", viper.GetIntSlice("server.ports"))
  fmt.Println("timeout: ", viper.GetDuration("server.timeout"))

  fmt.Println("mysql ip: ", viper.GetString("mysql.ip"))
  fmt.Println("mysql port: ", viper.GetInt("mysql.port"))
```

viper.GetDuration只要是`time.ParseDuration`接受的格式都可以，例如`3s`、`2min`、`1min30s`等。