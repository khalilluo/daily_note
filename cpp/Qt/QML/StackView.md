### 布局
子元素会自动填充铺满StackView的页面，不需要自己加anchor。因为需要支持动画效果

push进栈的时候构建，还存在内部的控件在pop之前不会析构

pop(item)一直pop找到item为止，如果item是null或者不存在则直接到最顶层



### item所有权
StackView只接受它自己创建的项目的所有权。这意味着任何推送到StackView的项目将永远不会被StackView销毁;只有StackView从组件或url创建的项目才会被StackView销毁。为了说明这一点，下面例子中的消息只会在StackView被销毁时打印，而不是在项目弹出堆栈时打印:

```javascript
Component {
    id: itemComponent

    Item {
        Component.onDestruction: print("Destroying second item")
    }
}

StackView {
    initialItem: Item {
        Component.onDestruction: print("Destroying initial item")
    }

    Component.onCompleted: push(itemComponent.createObject(window))
}
```

然而，在下面的例子中，从URL和组件中创建的两个项目都将在弹出时被StackView销毁:

```javascript
Component {
    id: itemComponent

    Item {
        Component.onDestruction: print("Destroying second item")
    }
}

StackView {
    initialItem: "Item1.qml"

    Component.onCompleted: push(itemComponent)
}
```