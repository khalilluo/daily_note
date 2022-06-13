Dart中常用的集合类型：`List`、`Set`、`Map`。
 其中`List`、`Set`实现了`Iterable`类的接口。
 `Map`内部使用了不同的数据结构。但使用`Map`的`entry`或`values`属性，也可以将`Map`的元素读取为`Iterable`对象。

##### 关于`Iterable`。

`Iterable`是一个可被有序访问的元素的集合。Dart中`Iterable`是抽象类，是不能被实例化的。但是可以通过`List`、`Set`创建`Iterable`。

```dart
Iterable<int> iterable = [1,2,3];
print(iterable.toSet());
print(iterable.toList());
```

`Iterable`与`List`的不同之处在于，`Iterable`没有`[]`操作符，因此不能使用如下方式读取特定索引的元素：

```csharp
var value = iterable[0];//会报错，提示没有[]操作符
```

但是我们可以用另一种方式来获取：

```csharp
var value = iterable.elementAt(0);
```

实现了`Iterable`的类，都是可以使用`for-in`循环进行遍历的。`for-in`通过`Iterator`(迭代器)，遍历`Iterable`对象。

##### 使用示例：

**1. `first`和`last`**

```dart
Iterable<int> iterable = [1,2,3];
iterable.first;
iterable.last;
```

> 使用`Iterable`的`last`属性会比较慢，因为它需要遍历所有的元素。对一个空的`Iterable`对象使用`first`和`last`会报`StateError`。说明顺序遍历？

```dart
var iterable = [];
print('The first element is ${iterable.first}');
print('The last element is ${iterable.last}');
//提示：Uncaught Error: Bad state: No element
```

**2.`firstWhere`：**
 从`Iterable`的对象中，获取满足条件的第一个元素。

```dart
Iterable<int> iterable = {-1,0,1,2};
//找到返回，找不到返回orElse的值。orElse可选参数。
int negtive = iterable.firstWhere((item)=> item < 0,orElse: ()=>99);
print(negtive);//-1
```

> 如果`firstWhere`没有找到，并且`orElse`参数被忽略，则会抛出`StateError`。

**3.`singleWhere`:**
 从`Iterable`的对象中，获取满足条件的一个元素，但它只期望只有一个元素满足条件。如果超过一个或没有元素满足条件，则会抛`StateError`。用法与`firstWhere`一致。

> `singleWhere()`单步执行`Iterable`对象直到最后一个元素，如果`Iterable`无限或包含大量元素，可能会导致问题。

**4.条件检查**
 使用`Iterable`，有时需要校验集合中的元素是否满足一些条件，可以不使用`for-in`。
 Dart提供了`every`方法：
 来判断是否所有的元素都满足某个条件

```dart
 Iterable<int> iterable = {-1,0,1,2};
bool satisfy = iterable.every((item)=> item > 2);//是否所有元素都满足>2
```

Dart提供了`any`方法：
 来判断是否至少有一个元素满足某个条件。

```dart
Iterable<int> iterable = {-1,0,1,2};
//是否至少有一个元素满足>=2
bool satisfy = iterable.any((item)=> item >= 2);
```

**5.`where`:**
 返回满足条件的所有元素集合。

```tsx
Iterable<int> iterable = {-1,0,1,2};
var evenNumbers = iterable.where((number) => number.isEven);
```

> 使用`where`未过滤到满足条件的集合时，会返回空的`Iterable`对象，不会像`firstWhere`和`singleWhere`抛`StateError`异常。

**6.`takeWhile`与`skipWhile`**：

`takeWhile`会从`Iterable`对象中获取所有满足条件的元素，直到不满足时，会跳出迭代。

```dart
Iterable<int> iterable = {-2,-1,0,1,2};
//类似do While 满足时获取，不满足停止迭代
var  value = iterable.takeWhile((item)=>item.isNegative);
print(value);//输出(-2, -1)
```

`skipWhile`会从`Iterable`对象中跳过所有满足条件的元素，直到不满足时，会获取。

```dart
Iterable<int> iterable = {-2,-1,0,1,2};
//类似do While 满足时跳过，不满足时获取
var  value = iterable.skipWhile((item)=>item.isNegative);
print(value);//输出(0, 1, 2)
```

**7. `map`:**
 `Iterable`对象可以使用`map`方法，对集合中的每个元素进行操作或替换，最终返回一个新的集合。

```tsx
//操作
Iterable<int> output = numbers.map((number) => number * 10);
//替换
Iterable<String> output = numbers.map((number) => number.toString());
```