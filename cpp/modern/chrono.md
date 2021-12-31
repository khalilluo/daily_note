chrono是一个模版库，使用简单，功能强大，只需要理解三个概念：duration、time_point、clock

#### 1.Durations

`std::chrono::duration` 表示一段时间，比如两个小时，12.88秒，半个时辰等等，只要能换算成秒即可。

**默认值就是秒，根据模板第二个参数变为其他单位**

```cpp
template <class Rep, class Period = ratio<1> > class duration;
```

其中：
Rep表示一种数值类型，用来表示Period的数量，比如int、float、double
Period是ratio类型，用来表示【用秒表示的时间单位】比如second、milisecond
常用的duration<Rep,Period>已经定义好了，在std::chrono::duration下：

ratio<3600, 1> hours
ratio<60, 1> minutes
ratio<1, 1> seconds
ratio<1, 1000> microseconds
ratio<1, 1000000> microseconds
ratio<1, 1000000000> nanosecons

这里需要说明一下ratio这个类模版的原型：

```cpp
template <intmax_t N, intmax_t D = 1> class ratio;
```

N代表分子，D代表分母，所以ratio表示一个分数值。
注意，我们自己可以定义Period，比如ratio<1, -2>表示单位时间是-0.5秒。

由于各种duration表示不同，chrono库提供了duration_cast类型转换函数。

就是把模板生成的不同duration值相互转换

```cpp
template <class ToDuration, class Rep, class Period> constexpr ToDuration duration_cast (const duration<Rep,Period>& dtn);
```

一段时间的典型用法：

```cpp
// duration constructor
#include <iostream>
#include <ratio>
#include <chrono>

int main ()
{
  typedef std::chrono::duration<int> seconds_type;
  typedef std::chrono::duration<int,std::milli> milliseconds_type;
  typedef std::chrono::duration<int,std::ratio<60*60>> hours_type;

  hours_type h_oneday (24);                  // 24h
  seconds_type s_oneday (60*60*24);          // 86400s
  milliseconds_type ms_oneday (s_oneday);    // 86400000ms

  seconds_type s_onehour (60*60);            // 3600s
//hours_type h_onehour (s_onehour);          // NOT VALID (type truncates), use:
  hours_type h_onehour (std::chrono::duration_cast<hours_type>(s_onehour));
  milliseconds_type ms_onehour (s_onehour);  // 3600000ms (ok, no type truncation)

  std::cout << ms_onehour.count() << "ms in 1h" << std::endl;

  return 0;
}
123456789101112131415161718192021222324


    // 根据时间差求标准时间值
    std::chrono::milliseconds t(3731000);
    t.count();
    int s = std::chrono::duration_cast<std::chrono::seconds>(t).count() % 60;
    int m = std::chrono::duration_cast<std::chrono::minutes>(t).count() % 60;
    int h = std::chrono::duration_cast<std::chrono::hours>(t).count();
	
	std::cout<<h<<":"<<m<<":"<<s<<std::endl;// 输出1：2：11
```

duration还有一个成员函数count()**返回Rep类型的Period数量**，看代码：

即这个单位下的数量（时，分，秒）

```javascript
// duration::count
#include <iostream>     // std::cout
#include <chrono>       // std::chrono::seconds, std::chrono::milliseconds
                        // std::chrono::duration_cast
using namespace std::chrono;
int main ()
{
  // std::chrono::milliseconds is an instatiation of std::chrono::duration:
  milliseconds foo (1000); // 1 second
  foo*=60;

  std::cout << "duration (in periods): ";
  std::cout << foo.count() << " milliseconds.\n";

  std::cout << "duration (in seconds): ";
  std::cout << foo.count() * milliseconds::period::num / milliseconds::period::den;
  std::cout << " seconds.\n";

  return 0;
}
1234567891011121314151617181920
```

#### 2.Time points

std::chrono::time_point 表示一个具体时间，如上个世纪80年代、你的生日、今天下午、火车出发时间等，只要它能用计算机时钟表示。鉴于我们使用时间的情景不同，**这个time point具体到什么程度，由选用的单位决定。一个time point必须有一个clock计时**。

```javascript
    // get current time，系统时间
    std::chrono::time_point<std::chrono::system_clock> nowTime = std::chrono::system_clock::now();
    std::time_t tmNowTime = std::chrono::system_clock::to_time_t(nowTime);
    std::cout << "nowTime\t" << std::put_time(std::localtime(&tmNowTime), "%F %T") << std::endl;

    // default_value
    std::chrono::time_point<std::chrono::system_clock> startTime;// 1970-1-1 8:0:0;
    std::time_t tmStartTime = std::chrono::system_clock::to_time_t(startTime);
    std::cout << "startTime\t" << std::put_time(std::localtime(&tmStartTime), "%F %T") << std::endl;

    // use timestamp
    // 2020-01-08 15:05:50(1578466970)
    std::chrono::time_point<std::chrono::system_clock> stampTime(std::chrono::seconds(1578466970));
    std::time_t tmStampTime = std::chrono::system_clock::to_time_t(stampTime);
    std::cout << "stampTime\t" << std::put_time(std::localtime(&tmStampTime), "%F %T") << std::endl;

    // some hours ago
	// 时间可以直接加减
    std::time_t tmSomeTimeAgo = std::chrono::system_clock::to_time_t(nowTime - std::chrono::hours(22) 
        - std::chrono::minutes(30));
    std::cout << "22 hours 30 minutes ago\t" << std::put_time(std::localtime(&tmSomeTimeAgo), "%F %T") << std::endl;

    // get time from string
    // use "std::get_time()"
    std::tm aTime;
    std::string strTime("2008-08-08 10:0:0");
    std::stringstream ssTime(strTime);
    ssTime.imbue(std::locale("de_DE.utf-8"));
    ssTime >> std::get_time(&aTime, "%Y-%m-%d %H:%M:%S");
    std::chrono::time_point<std::chrono::system_clock> tp = std::chrono::system_clock::from_time_t(std::mktime(&aTime));
    std::time_t aTestTime = std::chrono::system_clock::to_time_t(tp);
    std::cout << "aTime\t" << std::put_time(std::localtime(&aTestTime), "%F %T") << std::endl;

    std::cout << "compare: nowTime >= aTime ?\t" << (nowTime >= tp ? "true" : "false") << std::endl;

    // end time
    std::chrono::time_point<std::chrono::system_clock> endTime = std::chrono::system_clock::now();
    std::time_t tmEndTime = std::chrono::system_clock::to_time_t(endTime);
    std::cout << "endTime\t" << std::put_time(std::localtime(&tmEndTime), "%F %T") << std::endl;
    std::cout << "the program used\t" << std::chrono::duration_cast<std::chrono::microseconds>
        (endTime - nowTime).count() << "us.\n";
```

**time_point有一个函数time_from_eproch()用来获得1970年1月1日到time_point时间经过的duration。**
**举个例子，如果timepoint以天为单位，函数返回的duration就以天为单位。**

由于各种time_point表示方式不同，chrono也提供了相应的转换函数 time_point_cast。

```javascript
template <class ToDuration, class Clock, class Duration>
time_point<Clock,ToDuration> time_point_cast (const time_point<Clock,Duration>& tp);
12
```

比如计算

```javascript
// time_point_cast
#include <iostream>
#include <ratio>
#include <chrono>
using namespace std::chrono;

int main ()
{
    //
  // typedef duration<int,std::ratio<60*60*24>> days_type; 多余，标准库已有
  time_point<system_clock,days_type> today = time_point_cast<std::chrono::days>(system_clock::now());
  std::cout << today.time_since_epoch().count() << " days since epoch" << std::endl;

  return 0;
}

```

#### 3.Clocks

std::chrono::system_clock 它表示当前的系统时钟，系统中运行的所有进程使用now()得到的时间是一致的。
每一个clock类中都有确定的time_point, duration, Rep, Period类型。
操作有：
now() 当前时间time_point
to_time_t() time_point转换成time_t秒
from_time_t() 从time_t转换成time_point
典型的应用是计算时间日期：

```javascript
// system_clock example
#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>

int main ()
{
  using std::chrono::system_clock;

  std::chrono::duration<int,std::ratio<60*60*24> > one_day (1);

  system_clock::time_point today = system_clock::now();
  system_clock::time_point tomorrow = today + one_day;

  std::time_t tt;

  tt = system_clock::to_time_t ( today );
  std::cout << "today is: " << ctime(&tt);

  tt = system_clock::to_time_t ( tomorrow );
  std::cout << "tomorrow will be: " << ctime(&tt);

  return 0;
}
12345678910111213141516171819202122232425
```

std::chrono::steady_clock 为了表示稳定的时间间隔，后一次调用now()得到的时间总是比前一次的值大（这句话的意思其实是，如果中途修改了系统时间，也不影响now()的结果），每次tick都保证过了稳定的时间间隔。
操作有：
now() 获取当前时钟
典型的应用是给算法计时：

```javascript
// steady_clock example
#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>

int main ()
{
  using namespace std::chrono;

  steady_clock::time_point t1 = steady_clock::now();

  std::cout << "printing out 1000 stars...\n";
  for (int i=0; i<1000; ++i) std::cout << "*";
  std::cout << std::endl;

  steady_clock::time_point t2 = steady_clock::now();

  duration<double> time_span = duration_cast<duration<double>>(t2 - t1);

  std::cout << "It took me " << time_span.count() << " seconds.";
  std::cout << std::endl;

  return 0;
}
```

最后一个时钟，std::chrono::high_resolution_clock 顾名思义，这是系统可用的最高精度的时钟。实际上high_resolution_clock只不过是system_clock或者steady_clock的typedef。
操作有：
now() 获取当前时钟。