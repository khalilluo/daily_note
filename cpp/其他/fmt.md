### fmtlib基础用法

```cpp

// 保留2位小数
std::string s = fmt::format("The answer is {:.2f}", 1.12345678);
// s == "The answer is 1.12"

// 使用位置参数
std::string s = fmt::format("I'd rather be {1} than {0}.", "right", "happy");
// s == "I'd rather be happy than right."

// 使用别名参数
fmt::print("Hello, {name}! The answer is {number}. Goodbye, {name}.",
           fmt::arg("name", "World"), fmt::arg("number", 42));

// 格式化时间
#include <fmt/chrono.h>
using namespace std::literals::chrono_literals;
fmt::print("Default format: {} {}\n", 42s, 100ms);
fmt::print("strftime-like format: {:%H:%M:%S}\n", 3h + 15min + 30s);

// 打印容器
std::vector<int> v = {1, 2, 3};
fmt::print("{}\n", v);

// 输出到文件
auto out = fmt::output_file("guide.txt");
out.print("Don't {}", "Panic");

// 输出16进制数据
  std::string s = fmt::format("The answer is  {:X}.", 32);

  fmt::print("{}", s);
```

  