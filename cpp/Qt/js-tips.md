#### 空值合并运算符

空值合并运算符（`??`）是一种逻辑运算符，当其左侧操作数为`null`或`undefined`时，将返回其右侧操作数，否则将返回其左侧操作数。

```javascript
var tmp = null
var foo = tmp ?? "default string"
console.log(foo) // 输出：default string

tmp = "hello"
foo = tmp ?? "default string"
console.log(foo) // 输出：hello
```

#### 扩展运算符

扩展运算符用`...`表示。可以用于数组合并：

```js
let arr = ["Qt", "qml"]
let newArr = [...arr, "js"] // 输出：[Qt,qml,js]
```

还可以用于函数的不定参数：

```js
function sum(...args){
    var value = 0
    for (var i = 0; i < args.length; i++) {
        value += args[i]
    }
    return value
}
```

### 数组的解构赋值

从`ES6`开始，支持下面这种写法，达到的效果是一样的：

```js
var [a, b, c, d] = [1, 2, 3, 4]
```

下面是一个交换两个变量的简单示例：

```js
var [a, b] = [1, 2];
console.log("a = %1, b = %2".arg(a).arg(b)) // 输出：a = 1, b = 2
var [a, b] = [b, a];
console.log("a = %1, b = %2".arg(a).arg(b)) // 输出：a = 2, b = 1
```

数组在解构赋值时还允许使用默认值：

```js
[a, b = 2] = [1]
console.log(a) // 输出：1
console.log(b) // 输出：2
```

### 对象的解构赋值

对象的解构赋值与数组的解构赋值不同，它与对象属性的位置没有关系，而是约定变量名必须与属性名相同，然后根据名称相应赋值：

```js
const { name, age } = { name: 'avatar', age: 25 }
console.log(name) // 输出：avatar
console.log(age) // 输出：25
```

对象在解构赋值时也允许使用默认值：

```js
const { name, age = 25 } = { name: 'avatar' }
console.log(name) // 输出：avatar
console.log(age) // 输出：25
```

### 函数与解构赋值

可以把数组或者对象作为函数的参数，在解析参数时即可使用解构赋值：

```js
function add([a, b]) {
    return a + b
}
```

还可以把数组或者对象作为函数的返回值，用于返回多个值：

```js
function point() {
    return [1, 2]
}

var [x, y] = point()
```