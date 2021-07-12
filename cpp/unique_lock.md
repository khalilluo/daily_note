互斥锁保证了线程间的同步，但是却将并行操作变成了串行操作，这对性能有很大的影响，所以我们要尽可能的**减小锁定的区域**，也就是使用**细粒度锁**。

这一点`lock_guard`做的不好，不够灵活，`lock_guard`只能保证在析构的时候执行解锁操作，`lock_guard`本身并没有提供加锁和解锁的接口，但是有些时候会有这种需求。看下面的例子。



```cpp
class LogFile {
    std::mutex _mu;
    ofstream f;
public:
    LogFile() {
        f.open("log.txt");
    }
    ~LogFile() {
        f.close();
    }
    void shared_print(string msg, int id) {
        {
            std::lock_guard<std::mutex> guard(_mu);
            //do something 1
        }
        //do something 2
        {
            std::lock_guard<std::mutex> guard(_mu);
            // do something 3
            f << msg << id << endl;
            cout << msg << id << endl;
        }
    }

};
```

上面的代码中，一个函数内部有两段代码需要进行保护，这个时候使用`lock_guard`就需要创建两个局部对象来管理同一个互斥锁（其实也可以只创建一个，但是锁的力度太大，效率不行），修改方法是使用`unique_lock`。它提供了`lock()`和`unlock()`接口，能记录现在处于上锁还是没上锁状态，在析构的时候，会根据当前状态来决定是否要进行解锁（`lock_guard`就一定会解锁）。上面的代码修改如下：



```cpp
class LogFile {
    std::mutex _mu;
    ofstream f;
public:
    LogFile() {
        f.open("log.txt");
    }
    ~LogFile() {
        f.close();
    }
    void shared_print(string msg, int id) {

        std::unique_lock<std::mutex> guard(_mu);
        //do something 1
        guard.unlock(); //临时解锁

        //do something 2

        guard.lock(); //继续上锁
        // do something 3
        f << msg << id << endl;
        cout << msg << id << endl;
        // 结束时析构guard会临时解锁
        // 这句话可要可不要，不写，析构的时候也会自动执行
        // guard.ulock();
    }

};
```

上面的代码可以看到，在无需加锁的操作时，可以先临时释放锁，然后需要继续保护的时候，可以继续上锁，这样就无需重复的实例化`lock_guard`对象，还能减少锁的区域。同样，可以使用`std::defer_lock`设置初始化的时候不进行默认的上锁操作：



```cpp
void shared_print(string msg, int id) {
    std::unique_lock<std::mutex> guard(_mu, std::defer_lock);
    //do something 1

    guard.lock();
    // do something protected
    guard.unlock(); //临时解锁

    //do something 2

    guard.lock(); //继续上锁
    // do something 3
    f << msg << id << endl;
    cout << msg << id << endl;
    // 结束时析构guard会临时解锁
}
```

这样使用起来就比`lock_guard`更加灵活！然后这也是有代价的，因为它内部需要维护锁的状态，所以效率要比`lock_guard`低一点，在`lock_guard`能解决问题的时候，就是用`lock_guard`，反之，使用`unique_lock`。

后面在学习条件变量的时候，还会有`unique_lock`的用武之地。

另外，请注意，`unique_lock`和`lock_guard`都不能复制，`lock_guard`不能移动，但是`unique_lock`可以！



```cpp
// unique_lock 可以移动，不能复制
std::unique_lock<std::mutex> guard1(_mu);
std::unique_lock<std::mutex> guard2 = guard1;  // error
std::unique_lock<std::mutex> guard2 = std::move(guard1); // ok

// lock_guard 不能移动，不能复制
std::lock_guard<std::mutex> guard1(_mu);
std::lock_guard<std::mutex> guard2 = guard1;  // error
std::lock_guard<std::mutex> guard2 = std::move(guard1); // error
```

