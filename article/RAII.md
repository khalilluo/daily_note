**什么是RAII？**

RAII是Resource Acquisition Is Initialization（wiki上面翻译成 “资源获取就是初始化”）的简称，是C++语言的一种管理资源、避免泄漏的惯用法。利用的就是C++构造的对象最终会被销毁的原则



##### 为什么要使用RAII？

上面说到RAII是用来管理资源、避免资源泄漏的方法。在计算机系统中，资源是数量有限且对系统正常运行具有一定作用的元素。比如：网络套接字、互斥锁、文件句柄和内存等等，它们属于系统资源。我们在编程使用系统资源时，都必须遵循一个步骤：
1 申请资源；
2 使用资源；
3 释放资源。
第一步和第三步缺一不可，因为资源必须要申请才能使用的，使用完成以后，必须要释放，如果不释放的话，就会造成资源泄漏





智能指针（std::shared_ptr和std::unique_ptr）即RAII最具代表的实现



```c++
template<class... _Mutexes>
	class lock_guard
	{	// class with destructor that unlocks mutexes
public:
	explicit lock_guard(_Mutexes&... _Mtxes)
		: _MyMutexes(_Mtxes...)
		{	// construct and lock
		_STD lock(_Mtxes...);
		}

	lock_guard(_Mutexes&... _Mtxes, adopt_lock_t)
		: _MyMutexes(_Mtxes...)
		{	// construct but don't lock
		}
	 
	~lock_guard() _NOEXCEPT
		{	// unlock all
		_For_each_tuple_element(
			_MyMutexes,
			[](auto& _Mutex) _NOEXCEPT { _Mutex.unlock(); });
		}
	 
	lock_guard(const lock_guard&) = delete;
	lock_guard& operator=(const lock_guard&) = delete;

private:
	tuple<_Mutexes&...> _MyMutexes;
	};

```

