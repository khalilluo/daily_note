

## Loader

加载元素项(loader)作为一个占位符用于被加载项的加载。它的大小基于被加载项的大小而定,反之亦然。如果加载元素定义了大小,或者通过锚定(anchoring)定义了宽度和高度,被加载项将会被设置为加载元素项的大小。如果加载元素项没有设置大小,它将会根据被加载项的大小而定



### 加载后绑定属性(间接绑定)

因为元素是动态加载的，无法直接绑定需要关联的属性。解决方案如下：

- 使用Binding

```
Loader{
	id：loader
	...
	onLoaded:{
		binder.target = loader.item;
	}
}

Binding{
	id:binder
	...
}
```



### 获取被加载项信号(间接连接)

- 使用Connection





## 动态加载

1. Qt.createComponent生成组件后再使用createObject生成对象
2. Qt.createQmlObject从文本生成对象

