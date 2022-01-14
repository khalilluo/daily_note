`TextStyle`用于指定文本显示的样式如颜色、字体、粗细、背景等。我们看一个示例：

```dart
Text("Hello world",
  style: TextStyle(
    color: Colors.blue,
    fontSize: 18.0,
    height: 1.2,  
    fontFamily: "Courier",
    background: Paint()..color=Colors.yellow,
    decoration:TextDecoration.underline,
    decorationStyle: TextDecorationStyle.dashed
  ),
);
```

此示例只展示了 TextStyle 的部分属性，它还有一些其它属性，属性名基本都是自解释的.值得注意的是：

- `height`：该属性用于指定行高，但它并不是一个绝对值，而是一个因子，具体的行高等于`fontSize`*`height`。
- `fontFamily` ：由于不同平台默认支持的字体集不同，所以在手动指定字体时一定要先在不同平台测试一下。
- `fontSize`：该属性和 Text 的`textScaleFactor`都用于控制字体大小。但是有两个主要区别：
  - `fontSize`可以精确指定字体大小，而`textScaleFactor`只能通过缩放比例来控制。
  - `textScaleFactor`主要是用于系统字体大小设置改变时对 Flutter 应用字体进行全局调整，而`fontSize`通常用于单个文本，字体大小不会跟随系统字体大小变化

### TextSpan

![](../image/3-8.cc415da2.png)

```dart
Text.rich(TextSpan(
    children: [
     TextSpan(
       text: "Home: "
     ),
     TextSpan(
       text: "https://flutterchina.club",
       style: TextStyle(
         color: Colors.blue
       ),  
       recognizer: _tapRecognizer
     ),
    ]
))
```

- 上面代码中，我们通过 TextSpan 实现了一个基础文本片段和一个链接片段，然后通过`Text.rich` 方法将`TextSpan` 添加到 Text 中，之所以可以这样做，是因为 Text 其实就是 RichText 的一个包装，而RichText 是可以显示多种样式(富文本)的 widget。
- `_tapRecognizer`，它是点击链接后的一个处理器（代码已省略），关于手势识别的更多内容我们将在后面单独介绍。

### DefaultTextStyle

在 Widget 树中，文本的样式默认是可以被继承的（子类文本类组件未指定具体样式时可以使用 Widget 树中父级设置的默认样式），因此，如果在 Widget 树的某一个节点处设置一个默认的文本样式，那么该节点的子树中所有文本都会默认使用这个样式，而`DefaultTextStyle`正是用于设置默认文本样式的

```dart
DefaultTextStyle(
  //1.设置文本默认样式  
  style: TextStyle(
    color:Colors.red,
    fontSize: 20.0,
  ),
  textAlign: TextAlign.start,
  child: Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: <Widget>[
      Text("hello world"),
      Text("I am Jack"),
      Text("I am Jack",
        style: TextStyle(
          inherit: false, //2.不继承默认样式,按自己的style显示
          color: Colors.grey
        ),
      ),
    ],
  ),
);

// 以下方式也可以配置样式

// 声明文本样式
const textStyle = const TextStyle(
  fontFamily: 'Raleway',
);

// 使用文本样式
var buttonText = const Text(
  "Use the font for this text",
  style: textStyle,
);
```

