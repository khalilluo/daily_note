发现无效的条件及早返回，减少嵌套但不要过度



参数解构：

```javascript
printValue({type, name} = {}){
	// 1、专注关心的属性，减少嵌套判断
    // 2、不需要判断完对象后再判断属性 if(!obj || obj.attr)
    // 3、注意需要添加默认参数
    if (!type || !name) return 
    
    
	console.log(`type ${type} name${name}`)
}
```



**对 Null、Undefined、Empty 这些值的检查**

我们创建一个新变量，有时候需要检查是否为 Null 或 Undefined。JavaScript 本身就有一种缩写法能实现这种功能。

```js
if (test1 !== null || test1 !== undefined || test1 !== '') {
    let test2 = test1;
}
// Shorthand
let test2 = test1 || '';
```

**给多个变量赋值**

我们可以使用数组解构来在一行中给多个变量赋值。

```js
let a, b, c; 
a = 5; 
b = 8; 
c = 12;

//Shorthand 
let [a, b, c] = [5, 8, 12];
```

**赋默认值**

我们可以使用 OR(||) 短路运算来给一个变量赋默认值，如果预期值不正确的情况下。

```js
//Longhand 
let imagePath; 
let path = getImagePath(); 
if(path !== null && path !== undefined && path !== '') { 
  imagePath = path; 
} else { 
  imagePath = 'default.jpg'; 
} 
//Shorthand 
let imagePath = getImagePath() || 'default.jpg';
```



**交换两个变量**

为了交换两个变量，我们通常使用第三个变量。我们可以使用数组解构赋值来交换两个变量。

```js
let x = 'Hello', y = 55; 
//Longhand 
const temp = x; 
x = y; 
y = temp; 
//Shorthand 
[x, y] = [y, x];
```


### JavaScript 中 ?? 与 || 的区别
总的来说，`??`更加适合在不知道变量是否有值时使用

##### 相同点
用法相同，都是前后是值，中间用符号连接。根据前面的值来判断最终返回前面的值还是后面的值。
`值1 ?? 值2`
`值1 || 值2`

##### 不同点
判断方式不同：
使用 ?? 时，只有当值1为null或undefined时才返回值2；
使用 || 时，值1会转换为布尔值判断，为true返回值1，false 返回值2

```js
// ??
undefined ?? 2	// 2
null ?? 2		// 2
0 ?? 2			// 0
"" ?? 2			// ""
true ?? 2		// true
false ?? 2		// false

// ||
undefined || 2	// 2
null || 2		// 2
0 || 2			// 2
"" || 2			// 2
true || 2		// true
false || 2		// 2

```