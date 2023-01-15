

### 图片缩放

- 为了获得更好的显示效果,当缩放图片时推荐使用已缩放的图片来替代,过量的放大可能会导致图片模糊不清。当你在缩放图片时你最好考虑使用smooth:true来提高图片显示质量

  

### 定位器 （column/row/grid/flow）

- 通常Repeater(重复元素)与定位器一起使用。它的工作方式就像for循环与迭代器的模式一样;
- 当有一小部分的静态数据需要显示时,使用重复元素是最好的方式
- 内部元素可以跟定位器锚定对齐



### 锚定

- 如果某个方向被锚定的话是无法拖拽的，锚定 > xy轴和宽高属性
- 如果没有设置width/height系统就会默认使用implicitWidth/Height。可以认为implicitWidth是组件推荐大小



### 焦点切换

- 设置focus和KeyNavigation可以改变焦
- 如果是自定义组件，内部组件接收到焦点不一定会转移到子控件上，需要使用FocusScrope转移焦点
- 焦点区域(focus scope)如果接收到焦点,它将会把焦点传递给最后申请焦点的子元素



### 按键

- 元素直接添加Keys附加属性获取按键，需在获取焦点时生效



### 动画

- 动画也可以单独定义组件，供项目多处使用

- PropertyAction可以指定属性在动画前/期间/后立即生效，用于指定某些不能动画显示的属性

- ScriptAction可以在动画期间运行指定的动作

- target属性是一个对象数组

  

### 动画应用
- 属性动画 - 在元素完整加载后自动运行 

  ```html
  PropertyAnimation on x { to: 100 }
  ```

- 属性动作 - 当属性值改变时自动运行

  ```
  Behavior on x {
      NumberAnimation {
          id: bouncebehavior
          easing {
              type: Easing.OutElastic
              amplitude: 1.0
              period: 0.5
          }
      }
  }
  ```

  

- 独立运行动画 - 使用start()函数明确指定运行或者running属性被设置为动画(Animations)

  ```
  MouseArea {
      anchors.fill: parent
      onClicked: {
      	animateOpacity.start()
      }
  }
  
  NumberAnimation {
      id: animateOpacity
      target: flashingblob
      properties: "opacity"
      from: 0.99
      to: 1.0
      loops: Animation.Infinite
      easing {type: Easing.OutBack; overshoot: 500}
  }
  ```





### State及Transition

- 状态切换方式除了直接赋值也可以使用when绑定
- State变化只是改变对应元素的属性，动画需要在Transition中定义
- 元素的states和transitions都是数组





### 绑定属性方式

- Binding可以用when指定生效时机，可以绑定到C++属性上



### 模型-视图

- 使用JS数组时使用modelData获取对应数据

- 使用model时可以直接引用属性或者model.属性，推荐后者且避免model属性与元素属性重名

- QML视图为每个代理绑定了两个信号,onAdd和onRemove。使用动画连接它们,可以方便创建识别哪些内容被添加或删除的动画为了完成这个操作,PropertyAction元素需要在动画前设置GridView.delayRemove属性为true,并在动画后设置为false。这样确保了动画在代理项移除前完成

  ```
  GridView.onRemove: SequentialAnimation {
      PropertyAction { target: wrapper; property: "GridView.delayRemove"; value:true
      NumberAnimation { target: wrapper; property: "scale"; to
      PropertyAction { target: wrapper; property: "GridView.delayRemove"; value:false
  }
  ```

  

### 高亮

- 视图高亮默认跟随currentItem，需要手动设置currentItem，使用Focus可以使用键盘控制
- 如果要详细控制高亮通常将highlightFollowCurrentItem设置为false，高亮的xy跟随ListView.view.currentItem的xy; 或者默认highlightFollowCurrentItem为true, 手动设置currentIndex



### ListView

- 属性header和footer可以设置页眉和页脚



### 视图性能

- 使用cacheBuffer预加载项可以增加滚动的流畅
- 在代理内部减少Javascript，可以放到外面 

