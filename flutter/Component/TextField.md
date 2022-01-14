### 主要属性

- `controller`：编辑框的控制器，通过它可以设置/获取编辑框的内容、选择编辑内容、监听编辑文本改变事件。大多数情况下我们都需要显式提供一个`controller`来与文本框交互。如果没有提供`controller`，则`TextField`内部会自动创建一个。

- `focusNode`：用于控制`TextField`是否占有当前键盘的输入焦点。它是我们和键盘交互的一个句柄（handle）。

- `InputDecoration`：用于控制`TextField`的外观显示，如提示文本、背景颜色、边框等。

- `keyboardType`：用于设置该输入框默认的键盘输入类型，取值如下：

  | TextInputType枚举值 | 含义                                                |
  | ------------------- | --------------------------------------------------- |
  | text                | 文本输入键盘                                        |
  | multiline           | 多行文本，需和maxLines配合使用(设为null或大于1)     |
  | number              | 数字；会弹出数字键盘                                |
  | phone               | 优化后的电话号码输入键盘；会弹出数字键盘并显示“* #” |
  | datetime            | 优化后的日期输入键盘；Android上会显示“: -”          |
  | emailAddress        | 优化后的电子邮件地址；会显示“@ .”                   |
  | url                 | 优化后的url输入键盘； 会显示“/ .”                   |

- textInputAction`：键盘动作按钮图标(即回车键位图标)，它是一个枚举值，有多个可选值，全部的取值列表读者可以查看API文档，下面是当值为`TextInputAction.search`时，输入框右下角显示放大镜
- `style`：正在编辑的文本样式。
- `textAlign`: 输入框内编辑文本在水平方向的对齐方式。
- `autofocus`: 是否自动获取焦点。
- `obscureText`：是否隐藏正在编辑的文本，如用于输入密码的场景等，文本内容会用“•”替换。
- `maxLines`：输入框的最大行数，默认为1；如果为`null`，则无行数限制。
- `maxLength`和`maxLengthEnforcement` ：`maxLength`代表输入框文本的最大长度，设置后输入框右下角会显示输入的文本计数。`maxLengthEnforcement`决定当输入文本长度超过`maxLength`时如何处理，如截断、超出等。
- `toolbarOptions`：长按或鼠标右击时出现的菜单，包括 copy、cut、paste 以及 selectAll。
- `onChange`：输入框内容改变时的回调函数；注：内容改变事件也可以通过`controller`来监听。
- `onEditingComplete`和`onSubmitted`：这两个回调都是在输入框输入完成时触发，比如按了键盘的完成键（对号图标）或搜索键（🔍图标）。不同的是两个回调签名不同，`onSubmitted`回调是`ValueChanged<String>`类型，它接收当前输入内容做为参数，而`onEditingComplete`不接收参数。
- `inputFormatters`：用于指定输入格式；当用户输入内容改变时，会根据指定的格式来校验。
- `enable`：如果为`false`，则输入框会被禁用，禁用状态不接收输入和事件，同时显示禁用态样式（在其`decoration`中定义）。
- `cursorWidth`、`cursorRadius`和`cursorColor`：这三个属性是用于自定义输入框光标宽度、圆角和颜色的

##### 登录框

```dart
Column(
  children: <Widget>[
    TextField(
      autofocus: true,
      decoration: InputDecoration(
        labelText: "用户名",
        hintText: "用户名或邮箱",
        prefixIcon: Icon(Icons.person)
      ),
    ),
    TextField(
      decoration: InputDecoration(
        labelText: "密码",
        hintText: "您的登录密码",
        prefixIcon: Icon(Icons.lock)
      ),
      obscureText: true,
    ),
  ],
);
```

![](../image/3-25.18d09233.png)

##### 获取输入内容

1. 定义两个变量，用于保存用户名和密码，然后在`onChange`触发时，各自保存一下输入内容。
2. 通过`controller`直接获取。

```dart
// 方法2

// 定义一个controller
TextEditingController _unameController = TextEditingController();
// 设置输入框controller：
TextField(
    autofocus: true,
    controller: _unameController,
    ...
)
// 通过controller获取输入框内容
print(_unameController.text)
```

##### 监听文本变化

1. 设置`onChange`回调
2. 通过`controller`监听

```dart
// 方法2
@override
void initState() {
  //监听输入改变  
  _unameController.addListener((){
    print(_unameController.text);
  });
}

// 设置默认值，并从第三个字符开始选中后面的字符
_unameController.text="hello world!";
_unameController.selection=TextSelection(
    baseOffset: 2,
    extentOffset: _unameController.text.length
);
```

##### 控制焦点

焦点可以通过`FocusNode`和`FocusScopeNode`来控制，默认情况下，焦点由`FocusScope`来管理，它代表焦点控制范围，可以在这个范围内可以通过`FocusScopeNode`在输入框之间移动焦点、设置默认焦点等。我们可以通过`FocusScope.of(context)` 来获取Widget树中默认的`FocusScopeNode`。下面看一个示例，在此示例中创建两个`TextField`，第一个自动获取焦点，然后创建两个按钮：

- 点击第一个按钮可以将焦点从第一个`TextField`挪到第二个`TextField`。
- 点击第二个按钮可以关闭键盘。

![](../image/3-27.6ff2b58c.png)

```dart
class FocusTestRoute extends StatefulWidget {
  @override
  _FocusTestRouteState createState() => _FocusTestRouteState();
}

class _FocusTestRouteState extends State<FocusTestRoute> {
  FocusNode focusNode1 = FocusNode();
  FocusNode focusNode2 = FocusNode();
  FocusScopeNode? focusScopeNode;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(16.0),
      child: Column(
        children: <Widget>[
          TextField(
            autofocus: true, // 默认焦点
            focusNode: focusNode1,//关联focusNode1
            decoration: InputDecoration(
                labelText: "input1"
            ),
          ),
          TextField(
            focusNode: focusNode2,//关联focusNode2
            decoration: InputDecoration(
                labelText: "input2"
            ),
          ),
          Builder(builder: (ctx) {
            return Column(
              children: <Widget>[
                ElevatedButton(
                  child: Text("移动焦点"),
                  onPressed: () {
                    //将焦点从第一个TextField移到第二个TextField
                    // 这是一种写法 FocusScope.of(context).requestFocus(focusNode2);
                    // 这是第二种写法
                    if(null == focusScopeNode){
                      focusScopeNode = FocusScope.of(context);
                    }
                    focusScopeNode.requestFocus(focusNode2);
                  },
                ),
                ElevatedButton(
                  child: Text("隐藏键盘"),
                  onPressed: () {
                    // 当所有编辑框都失去焦点时键盘就会收起  
                    focusNode1.unfocus();
                    focusNode2.unfocus();
                  },
                ),
              ],
            );
          },
          ),
        ],
      ),
    );
  }

}
```



##### 监听焦点状态改变事件

`FocusNode`继承自`ChangeNotifier`，通过`FocusNode`可以监听焦点的改变事件，如：

```dart
...
// 创建 focusNode   
FocusNode focusNode = FocusNode();
...
// focusNode绑定输入框   
TextField(focusNode: focusNode);
...
// 监听焦点变化    
focusNode.addListener((){
   print(focusNode.hasFocus);
});
```

获得焦点时`focusNode.hasFocus`值为`true`，失去焦点时为`false`。

##### 自定义样式

我们可以通过`decoration`属性来定义输入框样式，下面以自定义输入框下划线颜色为例来介绍一下：

```dart
TextField(
  decoration: InputDecoration(
    labelText: "请输入用户名",
    prefixIcon: Icon(Icons.person),
    // 未获得焦点下划线设为灰色
    enabledBorder: UnderlineInputBorder(
      borderSide: BorderSide(color: Colors.grey),
    ),
    //获得焦点下划线设为蓝色
    focusedBorder: UnderlineInputBorder(
      borderSide: BorderSide(color: Colors.blue),
    ),
  ),
),
```

上面代码我们直接通过InputDecoration的enabledBorder和focusedBorder来分别设置了输入框在未获取焦点和获得焦点后的下划线颜色。另外，我们也可以通过主题来自定义输入框的样式，下面我们探索一下如何在不使用enabledBorder和focusedBorder的情况下来自定义下滑线颜色。

由于`TextField`在绘制下划线时使用的颜色是主题色里面的`hintColor`，但提示文本颜色也是用的`hintColor`， 如果我们直接修改`hintColor`，那么下划线和提示文本的颜色都会变。值得高兴的是`decoration`中可以设置`hintStyle`，它可以覆盖`hintColor`，并且主题中可以通过`inputDecorationTheme`来设置输入框默认的`decoration`。所以我们可以通过主题来自定义，代码如下：

```dart
Theme(
  data: Theme.of(context).copyWith(
      hintColor: Colors.grey[200], //定义下划线颜色
      inputDecorationTheme: InputDecorationTheme(
          labelStyle: TextStyle(color: Colors.grey),//定义label字体样式
          hintStyle: TextStyle(color: Colors.grey, fontSize: 14.0)//定义提示文本样式
      )
  ),
  child: Column(
    children: <Widget>[
      TextField(
        decoration: InputDecoration(
            labelText: "用户名",
            hintText: "用户名或邮箱",
            prefixIcon: Icon(Icons.person)
        ),
      ),
      TextField(
        decoration: InputDecoration(
            prefixIcon: Icon(Icons.lock),
            labelText: "密码",
            hintText: "您的登录密码",
            hintStyle: TextStyle(color: Colors.grey, fontSize: 13.0)
        ),
        obscureText: true,
      )
    ],
  )
)
```

运行效果如图3-28所示：

![图3-28](../image/3-28.b6b9c9b2.png)

我们成功的自定义了下划线颜色和提问文字样式，细心的读者可能已经发现，通过这种方式自定义后，输入框在获取焦点时，`labelText`不会高亮显示了，正如上图中的"用户名"本应该显示蓝色，但现在却显示为灰色，并且我们还是无法定义下划线宽度。另一种灵活的方式是直接隐藏掉`TextField`本身的下划线，然后通过`Container`去嵌套定义样式，如:

```dart
Container(
  child: TextField(
    keyboardType: TextInputType.emailAddress,
    decoration: InputDecoration(
        labelText: "Email",
        hintText: "电子邮件地址",
        prefixIcon: Icon(Icons.email),
        border: InputBorder.none //隐藏下划线
    )
  ),
  decoration: BoxDecoration(
      // 下滑线浅灰色，宽度1像素
      border: Border(bottom: BorderSide(color: Colors.grey[200], width: 1.0))
  ),
)
```

![](../image/image-20180904150511545.png)

通过这种组件组合的方式，也可以定义背景圆角等。一般来说，优先通过`decoration`来自定义样式，如果`decoration`实现不了，再用widget组合的方式。

> 思考题：在这个示例中，下划线颜色是固定的，所以获得焦点后颜色仍然为灰色，如何实现点击后下滑线也变色呢？