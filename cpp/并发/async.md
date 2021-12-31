## async

std::async()做如下的事情
·自动创建一个线程(或从内部线程池中挑选)和一个promise对象。
·然后将std::promise对象传递给线程函数，并返回相关的std::future对象
·当我们传递参数的函数退出时，它的值将被设置在这个promise对象中，所以最终的返回值将在std::future对象中可用

```cpp

#include "pch.h"
#include <iostream>
#include <string>
#include <chrono>
#include <thread>
#include <future>
 
using namespace std::chrono;
 
// 也可以是lambda函数
std::string fetchDataFromDB(std::string recvData) {
 
	std::cout << "fetchDataFromDB start" << std::this_thread::get_id() << std::endl;
	std::this_thread::sleep_for(seconds(5));
	return "DB_" + recvData;
}
 
 
int main() {
 
	std::cout << "main start" << std::this_thread::get_id() << std::endl;
 
	//获取开始时间
	system_clock::time_point start = system_clock::now();
 
    /*
    std::async中的第一个参数是启动策略，它控制std::async的异步行为，我们可以用三种不同的启动策略来创建
	·std::launch::async
	保证异步行为，即传递函数将在单独的线程中执行
	·std::launch::deferred
	当其他线程调用get()来访问共享状态时，将调用非异步行为
	·std::launch::async | std::launch::deferred
	默认行为。有了这个启动策略，它可以异步运行或不运行，这取决于系统的负载，但我们无法控制它。
	*/
	std::future<std::string> resultFromDB = std::async(std::launch::async, fetchDataFromDB, "Data");
 
	std::future_status status;
	std::string dbData;
	do
	{
		status = resultFromDB.wait_for(std::chrono::seconds(1));
 
		switch (status)
		{
		case std::future_status::ready:	// 完成
			std::cout << "Ready..." << std::endl;
			//获取结果
			dbData = resultFromDB.get();
			std::cout << dbData << std::endl;
			break;
		case std::future_status::timeout:	// 超时
			std::cout << "timeout..." << std::endl;
			break;
		case std::future_status::deferred:	// 未开始
			std::cout << "deferred..." << std::endl;
			break;
		default:
			break;
		}
 
	} while (status != std::future_status::ready);
 
	
	//获取结束时间
	auto end = system_clock::now();
 
	auto diff = duration_cast<std::chrono::seconds>(end - start).count();
	std::cout << "Total Time taken= " << diff << "Seconds" << std::endl;
 
	return 0;
}
```

