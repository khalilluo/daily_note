互斥锁`std::mutex`是一种最常见的线程间同步的手段，但是在有些情况下不太高效。

假设想实现一个简单的消费者生产者模型，一个线程往队列中放入数据，一个线程往队列中取数据，取数据前需要判断一下队列中确实有数据，由于这个队列是线程间共享的，所以，需要使用互斥锁进行保护，一个线程在往队列添加数据的时候，另一个线程不能取，反之亦然。

可以看到，互斥锁其实可以完成这个任务，但是却存在着性能问题。**两个线程可能存在很多空跑的情况**，导致CPU占用过高，解决方法就是使用条件变量

`c++11`中提供了`#include <condition_variable>`头文件，其中的`std::condition_variable`可以和`std::mutex`结合一起使用，其中有两个重要的接口，`notify_one()`和`wait()`，`wait()`可以让线程陷入**休眠状态**，在消费者生产者模型中，如果生产者发现队列中没有东西，就可以让自己休眠，但是不能一直不干活啊，`notify_one()`就是**唤醒**处于`wait`中的**其中一个条件变量**（可能当时有很多条件变量都处于`wait`状态）。那什么时刻使用`notify_one()`比较好呢，当然是在生产者往队列中放数据的时候了，队列中有数据，就可以赶紧叫醒等待中的线程起来干活了。

使用条件变量修改后如下：



```cpp
#include <iostream>
#include <deque>
#include <thread>
#include <mutex>
#include <condition_variable>

std::deque<int> q;
std::mutex mu;
std::condition_variable cond;

void function_1() {
    int count = 10;
    while (count > 0) {
        std::unique_lock<std::mutex> locker(mu);
        q.push_front(count);
        locker.unlock();
        cond.notify_one();  // Notify one waiting thread, if there is one.
        std::this_thread::sleep_for(std::chrono::seconds(1));
        count--;
    }
}

void function_2() {
    int data = 0;
    while ( data != 1) {
        std::unique_lock<std::mutex> locker(mu);
        while(q.empty())
            cond.wait(locker); // Unlock mu and wait to be notified
        data = q.back();
        q.pop_back();
        locker.unlock();
        std::cout << "t2 got a value from t1: " << data << std::endl;
    }
}
int main() {
    std::thread t1(function_1);
    std::thread t2(function_2);
    t1.join();
    t2.join();
    return 0;
}
```

上面的代码有三个注意事项：

1. 在`function_2`中，在判断队列是否为空的时候，**使用的是`while(q.empty())`，而不是`if(q.empty())`**，这是因为`wait()`从阻塞到返回，不一定就是由于`notify_one()`函数造成的，还有可能由于系统的不确定原因唤醒（可能和条件变量的实现机制有关），这个的时机和频率都是不确定的，被称作**伪唤醒**，如果在错误的时候被唤醒了，执行后面的语句就会错误，所以需要再次判断队列是否为空，如果还是为空，就继续`wait()`阻塞。
2. 在管理互斥锁的时候，使用的是`std::unique_lock`而不是`std::lock_guard`，而且事实上也不能使用`std::lock_guard`，这需要先解释下`wait()`函数所做的事情。可以看到，在`wait()`函数之前，使用互斥锁保护了，如果`wait`的时候什么都没做，岂不是一直持有互斥锁？那生产者也会一直卡住，不能够将数据放入队列中了。所以，**`wait()`函数会先调用互斥锁的`unlock()`函数，然后再将自己睡眠，在被唤醒后，又会继续持有锁，保护后面的队列操作。**而`lock_guard`没有`lock`和`unlock`接口，而`unique_lock`提供了。这就是必须使用`unique_lock`的原因。
3. 使用细粒度锁，尽量减小锁的范围，**在`notify_one()`的时候，不需要处于互斥锁的保护范围内**，所以在唤醒条件变量之前可以将锁`unlock()`。

**还可以将`cond.wait(locker);`换一种写法**，`wait()`的第二个参数可以传入一个函数表示检查条件，这里使用`lambda`函数最为简单，如果这个函数返回的是`true`，`wait()`函数不会阻塞会直接返回，如果这个函数返回的是`false`，`wait()`函数就会阻塞着等待唤醒，如果被伪唤醒，会继续判断函数返回值。



```cpp
void function_2() {
    int data = 0;
    while ( data != 1) {
        std::unique_lock<std::mutex> locker(mu);
        cond.wait(locker, [](){ return !q.empty();} );  // Unlock mu and wait to be notified
        data = q.back();
        q.pop_back();
        locker.unlock();
        std::cout << "t2 got a value from t1: " << data << std::endl;
    }
}
```

除了`notify_one()`函数，`c++`还提供了`notify_all()`函数，可以同时唤醒所有处于`wait`状态的条件变量。

