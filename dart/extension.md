dart的extension方法可以给已经存在的类添加新的函数，通过extension我们可以封装一些常用方法

```dart
/// 字符串扩展方法
extension StringExtension on String{
  /// 是否是电话号码
  bool get isMobileNumber {
    if(this?.isNotEmpty != true) return false;
    return RegExp(r'^((13[0-9])|(14[5,7,9])|(15[^4])|(18[0-9])|(17[0,1,3,5,6,7,8])|(19)[0-9])\d{8}$').hasMatch(this);
  }
}

void test(){
  bool isMobileNumber= "电话号码".isMobileNumber;
}


// iconfont中的图标有偏下的问题，添加一个iconCenter方法，使icon居中
extension WidgetExt on Widget {
  Widget iconCenter(double size) {
    return Baseline(
      baselineType: TextBaseline.ideographic,
      baseline: size * 0.84,
      child: this,
    );
  }
}

Icon(KIconData.trash, size: 16.w, color: Colors.black).iconCenter(16.w),


// 
extension TimeExt on num {
  String get publishTime {
    var now = new DateTime.now();
    var longTime = this.toString().length < 13 ? this * 1000 : this;
    var time = new DateTime.fromMillisecondsSinceEpoch(longTime);
    var difference = now.difference(time);
    int days = difference.inDays;
    int hours = difference.inHours;
    int minutes = difference.inMinutes;
    String result = '';
    if (days > 3) {
      bool isNowYear = now.year == time.year;
      var pattern = isNowYear ? 'MM-dd' : 'yyyy-MM-dd';
      result = new DateFormat(pattern).format(time);
    } else if (days > 0) {
      result = '$days天前';
    } else if (hours > 0) {
      result = '$hours小时前';
    } else if (minutes > 0) {
      result = '$minutes分钟前';
    } else {
      result = '刚刚';
    }
    return result;
  }
}

1607260860000.publishTime();
```

### 扩展在 Widget 控件中的应用

我们会经常有类似控件

```dart
     
	// 我们会经常有类似控件
	Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Container(
            margin: EdgeInsets.all(10),
            alignment: Alignment.center,
            child: Text("ZL"),
          ),
          Container(
            margin: EdgeInsets.all(10),
            alignment: Alignment.center,
            child: Text("ZL"),
          ),
          Container(
            margin: EdgeInsets.all(10),
            alignment: Alignment.center,
            child: Text("ZL"),
          ),
        ],
      )

      // 好多重复的 Container()是不是？我们可以扩展 一下：
      extension HclWidget on Widget {
        Widget marginAll(double margin) {
          return Container(
            alignment: Alignment.center,
            margin: EdgeInsets.all(margin),
            child: this,
          );
        }
      }

	// 之后我们就可以改成这样：
      Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text("ZL").marginAll(10),
          Text("ZL").marginAll(10),
          Text("ZL").marginAll(10),
        ],
      )
```

