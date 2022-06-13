#### 作用
返回一个类型的右值引用，不管是否有没有默认构造函数或该类型不可以创建对象。（可以用于抽象基类）;

它不会对 expr 真正求值。所以你不必在 expr 处产生任何临时对象，也不会因为表达式很复杂而发生真实的计算

[C++11中的decltype和declval表示什么意思，它们是如何使用的，会在什么时候使用？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/447107869/answer/1757635568)

[理解 std::declval 和 decltype_算法_hedzr_InfoQ写作平台](https://xie.infoq.cn/article/474e0616cb4b051096ade44ed)

[谈 C++17 里的 Builder 模式 | hzSomthing (hedzr.com)](https://hedzr.com/c++/algorithm/cxx17-builder-pattern/#crtp)