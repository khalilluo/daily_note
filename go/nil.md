指针对象的方法来说，就算指针的值为`nil`也是可以调用的，但会引起panic，故在调用前需判断合法性





当一个变量被声明之后，系统自动赋予它该类型的零值：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil。记住，所有的内存在 Go 中都是经过初始化的

nil只能赋值给指针、chan、func、interface、map、或slice类型的变量。

## 
