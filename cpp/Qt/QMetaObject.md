

## CPP代码

```cpp
#ifndef OBJECT_H
#define OBJECT_H

#include <QObject>
#include <QString>
#include <QDebug>

class Object : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int age READ age  WRITE setAge NOTIFY ageChanged)
    Q_PROPERTY(int score READ score  WRITE setScore NOTIFY scoreChanged)
    Q_PROPERTY(Level level READ level WRITE setLevel)
    Q_CLASSINFO("Author", "Scorpio")
    Q_CLASSINFO("Version", "1.0")
public:
    enum Level
    {
        Basic = 1,
        Middle,
        Advanced,
        Master
    };
    Q_ENUMS(Level)
protected:
    QString m_name;
    Level m_level;
    int m_age;
    int m_score;
    void setLevel(const int& score)
    {
        if(score <= 60)
        {
            m_level = Basic;
        }
        else if(score < 100)
        {
            m_level = Middle;
        }
        else if(score < 150)
        {
            m_level = Advanced;
        }
        else
        {
            m_level = Master;
        }
    }
public:
    explicit Object(QString name, QObject *parent = 0):QObject(parent)
    {
        m_name = name;
        setObjectName(m_name);
        connect(this, SIGNAL(ageChanged(int)), this, SLOT(onAgeChanged(int)));
        connect(this, SIGNAL(scoreChanged(int)), this, SLOT(onScoreChanged(int)));
    }

    int age()const
    {
        return m_age;
    }

    void setAge(const int& age)
    {
        m_age = age;
        emit ageChanged(m_age);
    }

    int score()const
    {
        return m_score;
    }

    void setScore(const int& score)
    {
        m_score = score;
        setLevel(m_score);
        emit scoreChanged(m_score);
    }

    Level level()const
    {
        return m_level;
    }

    void setLevel(const Level& level)
    {
        m_level = level;
    }
signals:
    void ageChanged(int age);
    void scoreChanged(int score);
public slots:
     void onAgeChanged(int age)
     {
         qDebug() << "age changed:" << age;
     }
     void onScoreChanged(int score)
     {
         qDebug() << "score changed:" << score;
     }
};

#endif // OBJECT_H
```

## 内部对象简单说明

- d_ptr指向本对象的QObjectData对象，保持本对象的信息，包括父亲孩子，是否widget 等
- 如果添加了Q_OBJECT宏则会生成moc文件，重载metaObject函数返回的则是继承类的QMetaObejct对象，即文件中的staticMetaObject对象
- QMetaObject对象的数据(Qt5)包括父亲QMetaObject对象指针，qt_meta_stringdata_xxx_t和qt_static_metacall指针
- qobject_cast最后到特定对象的qt_metacast函数转换对象指针，使用的字符串对比，即qt_meta_stringdata_xxx_t的stringData0首部与对象名称对比
- qt_meta_data_xxx的content部分用于描述对象信息，比如版本类名称等。信号槽部分第一列描述的是qt_meta_stringdata_xxx_t对象中的索引，后续是参数权限等信息
- qt_static_metacall函数使用名称或者索引的方式调用信号/槽/可调用函数等，实现函数反射

## qt_meta_data_xxx

```PHP
static const uint qt_meta_data_Object[] = {

 // content:内容信息
       6,       // revision        MOC生成代码的版本号
       0,       // classname       类名，在qt_meta_stringdata_Object数组中索引为0
       2,   14, // classinfo       类信息，有2个cassinfo定义，
       4,   18, // methods         类有4个自定义方法，即信号与槽个数，
       3,   38, // properties      属性的位置信息，有3个自定义属性，
       1,   50, // enums/sets      枚举的位置信息，有一个自定义枚举，在qt_meta_stringdata_Object数组中索引为50
       0,    0, // constructors    构造函数的位置信息
       0,       // flags
       2,       // signalCount

 // classinfo: key, value           //类信息的存储在qt_meta_stringdata_Object数组中，
      15,    7,                     //第一个类信息，key的数组索引为15，即Author，value的数组索引为7，即Scorpio
      26,   22,                     //第二个类信息，key的数组索引为26，即Version，value的数组索引为22，即1.0

 // signals: signature, parameters, type, tag, flags
      39,   35,   34,   34, 0x05,   //第一个自定义信号的签名存储在qt_meta_stringdata_Object数组中，
                                    //索引是39，即ageChanged(int)
      61,   55,   34,   34, 0x05,   //第二个自定义信号的签名存储在qt_meta_stringdata_Object数组中，
                                    //索引是61，即scoreChanged(int)

 // slots: signature, parameters, type, tag, flags
      79,   35,   34,   34, 0x0a,   //第一个自定义槽函数的签名存储在qt_meta_stringdata_Object数组中，
                                    //索引是79，即onAgeChanged(int)
      97,   55,   34,   34, 0x0a,   //第二个自定义槽函数的签名存储在qt_meta_stringdata_Object数组中，
                                    //索引是79，即onScoreChanged(int)
 // properties: name, type, flags
      35,  117, 0x02495103,            // 第一个自定义属性的签名存储在qt_meta_stringdata_Object中,索引是35,即age
      55,  117, 0x02495103,            // 第二个自定义属性的签名存储在qt_meta_stringdata_Object中,索引是55,即score
     127,  121, 0x0009510b,            // 第三个自定义属性的签名存储在qt_meta_stringdata_Object中,索引是127,即level

 // properties: notify_signal_id    //属性关联的信号编号
       0,        
       1,
       0,

 // enums: name, flags, count, data
     121, 0x0,    4,   54,         //枚举的定义，存储在qt_meta_stringdata_Object中，索引是121，即Level，内含4个枚举常量

 // enum data: key, value          //枚举数据的键值对
     133, uint(Object::Basic),     //数组索引是133，即Basic
     139, uint(Object::Middle),    //数组索引是139，即Middle
     146, uint(Object::Advanced),  //数组索引是146，即Advanced
     155, uint(Object::Master),    //数组索引是155，即Master

       0        // eod   元数据结束标记
};
```

## qt_meta_stringdata_xxx

```cpp
static const char qt_meta_stringdata_Object[] = {
    "Object\0Scorpio\0Author\0""1.0\0Version\0\0"
    "age\0ageChanged(int)\0score\0scoreChanged(int)\0"
    "onAgeChanged(int)\0onScoreChanged(int)\0"
    "int\0Level\0level\0Basic\0Middle\0Advanced\0"
    "Master\0"
};
```

## qt_static_metacall

利用槽函数在qt_static_metacall 函数的索引位置来调用槽函数：

这个索引在内部被称为相对索引，不包含父对象的索引位

```cpp
void Object::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        Object *_t = static_cast<Object *>(_o);
        switch (_id) {
        case 0: _t->ageChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 1: _t->scoreChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 2: _t->onAgeChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->onScoreChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}
```



## 信号与槽的连接

开始连接时，Qt所要做的第一件事是找出所需要的信号和槽的索引。Qt会去查找元对象的字符串表来找出相应的索引。

然后，创建一个 QObjectPrivate::Connection 对象，将其添加到内部的链表中。

由于允许多个槽连接到同一个信号，需要为每一个信号添加一个已连接的槽的列表。每一个连接都必须包含接收对象和槽的索引。在接收对象销毁的时候，相应的连接也能够被自动销毁。所以每一个接收对象都需要知道谁连接到它自己，以便能够清理连接



即发送方需要保存接收方的槽/信号索引和指针，使用ConnectionList管理

https://blog.51cto.com/u_9291927/2070398



## 信号发射

信号调用QMetaObject::active，根据ConnectType处理

- 队列模式: 调用queued_activate
- 阻塞模式: 同一线程报错，不同线程则使用postEvent发送一个QMetaCallEvent时间，利用QSemaphore获取调用结果
- 直接调用模式：metacall->qt_metacall->qt_static_metacall