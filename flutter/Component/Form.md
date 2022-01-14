#### Form

`Form`继承自`StatefulWidget`对象，它对应的状态类为`FormState`。我们先看看`Form`类的定义：

```dart
Form({
  required Widget child,
  bool autovalidate = false,
  WillPopCallback onWillPop,
  VoidCallback onChanged,
})
```

- `autovalidate`：是否自动校验输入内容；当为`true`时，每一个子 FormField 内容发生变化时都会自动校验合法性，并直接显示错误信息。否则，需要通过调用`FormState.validate()`来手动校验。
- `onWillPop`：决定`Form`所在的路由是否可以直接返回（如点击返回按钮），该回调返回一个`Future`对象，如果 Future 的最终结果是`false`，则当前路由不会返回；如果为`true`，则会返回到上一个路由。此属性通常用于拦截返回按钮。
- `onChanged`：`Form`的任意一个子`FormField`内容发生变化时会触发此回调。

#### FormField

`Form`的子孙元素必须是`FormField`类型，`FormField`是一个抽象类，定义几个属性，`FormState`内部通过它们来完成操作，`FormField`部分定义如下：

```dart
const FormField({
  ...
  FormFieldSetter<T> onSaved, //保存回调
  FormFieldValidator<T>  validator, //验证回调
  T initialValue, //初始值
  bool autovalidate = false, //是否自动校验。
})
```



为了方便使用，Flutter 提供了一个`TextFormField`组件，它继承自`FormField`类，也是`TextField`的一个包装类，所以除了`FormField`定义的属性之外，它还包括`TextField`的属性。

#### FormState

`FormState`为`Form`的`State`类，可以通过`Form.of()`或`GlobalKey`获得。我们可以通过它来对`Form`的子孙`FormField`进行统一操作。我们看看其常用的三个方法：

- `FormState.validate()`：调用此方法后，会调用`Form`子孙`FormField的validate`回调，如果有一个校验失败，则返回false，所有校验失败项都会返回用户返回的错误提示。
- `FormState.save()`：调用此方法后，会调用`Form`子孙`FormField`的`save`回调，用于保存表单内容
- `FormState.reset()`：调用此方法后，会将子孙`FormField`的内容清空。

#### 示例

我们修改一下上面用户登录的示例，在提交之前校验：

1. 用户名不能为空，如果为空则提示“用户名不能为空”。
2. 密码不能小于 6 位，如果小于 6 为则提示“密码不能少于 6 位”。

```dart
import 'package:flutter/material.dart';

class FormTestRoute extends StatefulWidget {
  @override
  _FormTestRouteState createState() => _FormTestRouteState();
}

class _FormTestRouteState extends State<FormTestRoute> {
  TextEditingController _unameController = TextEditingController();
  TextEditingController _pwdController = TextEditingController();
  GlobalKey _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey, //设置globalKey，用于后面获取FormState
      autovalidateMode: AutovalidateMode.onUserInteraction,
      child: Column(
        children: <Widget>[
          TextFormField(
            autofocus: true,
            controller: _unameController,
            decoration: InputDecoration(
              labelText: "用户名",
              hintText: "用户名或邮箱",
              icon: Icon(Icons.person),
            ),
            // 校验用户名
            validator: (v) {
              return v!.trim().length > 0 ? null : "用户名不能为空";
            },
          ),
          TextFormField(
            controller: _pwdController,
            decoration: InputDecoration(
              labelText: "密码",
              hintText: "您的登录密码",
              icon: Icon(Icons.lock),
            ),
            obscureText: true,
            //校验密码
            validator: (v) {
              return v!.trim().length > 5 ? null : "密码不能少于6位";
            },
          ),
          // 登录按钮
          Padding(
            padding: const EdgeInsets.only(top: 28.0),
            child: Row(
              children: <Widget>[
                Expanded(
                  child: ElevatedButton(
                    child: Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: Text("登录"),
                    ),
                    onPressed: () {
                      // 通过_formKey.currentState 获取FormState后，
                      // 调用validate()方法校验用户名密码是否合法，校验
                      // 通过后再提交数据。
                      if ((_formKey.currentState as FormState).validate()) {
                        //验证通过提交数据
                      }
                    },
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}
```

注意，登录按钮的`onPressed`方法中不能通过`Form.of(context)`来获取，原因是，此处的`context`为`FormTestRoute`的context，而`Form.of(context)`是根据所指定`context`向根去查找，而`FormState`是在`FormTestRoute`的子树中，所以不行。正确的做法是通过`Builder`来构建登录按钮，`Builder`会将`widget`节点的`context`作为回调参数：

```dart
Expanded(
 // 通过Builder来获取ElevatedButton所在widget树的真正context(Element) 
  child:Builder(builder: (context){
    return ElevatedButton(
      ...
      onPressed: () {
        //由于本widget也是Form的子代widget，所以可以通过下面方式获取FormState  
        if(Form.of(context).validate()){
          //验证通过提交数据
        }
      },
    );
  })
)
```

其实`context`正是操作Widget所对应的`Element`的一个接口，由于Widget树对应的`Element`都是不同的，所以`context`也都是不同的，有关`context`的更多内容会在后面高级部分详细讨论。Flutter中有很多“of(context)”这种方法，读者在使用时一定要注意`context`是否正确