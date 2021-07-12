- **accumulate**: iterator对标识的序列段元素之和，加到一个由val指定的初始值上。重载版本不再做加法，而是传进来的二元操作符被应用到元素上。
- **partial_sum**: 创建一个新序列，其中每个元素值代表指定范围内该位置前所有元素之和。重载版本使用自定义操作代替加法。
- **inner_product**: 对两个序列做内积(对应元素相乘，再求和)并将内积加到一个输入的初始值上。重载版本使用用户定义的操作。
- **adjacent_difference**: 创建一个新序列，新序列中每个新值代表当前元素与上一个元素的差。重载版本用指定二元操作计算相邻元素的差。

```cpp
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <numeric> // 数值算法
#include <iterator> // 定义了ostream_iterator

using namespace std;

int main(int argc, char* argv[])
{
  int arr[] = { 1, 2, 3, 4, 5 };
  vector<int> vec(arr, arr + 5);
  vector<int> vec2(arr, arr + 5);

  //  accumulate: iterator对标识的序列段元素之和，加到一个由val指定的初始值上。
  int temp;
  int val = 0;
  temp = accumulate(vec.begin(), vec.end(), val);
  cout << "accumulate(val = 0): " << temp << endl;
  val = 1;
  temp = accumulate(vec.begin(), vec.end(), val);
  cout << "accumulate(val = 1): " << temp << endl;

  // inner_product: 对两个序列做内积(对应元素相乘，再求和)并将内积加到一个输入的初始值上。
  // 这里是：1*1 + 2*2 + 3*3 + 4*4 + 5*5
  val = 0;
  temp = inner_product(vec.begin(), vec.end(), vec2.begin(), val);
  cout << "inner_product(val = 0): " << temp << endl;

  // partial_sum: 创建一个新序列，其中每个元素值代表指定范围内该位置前所有元素之和。
  // 第一次，1   第二次，1+2  第三次，1+2+3  第四次，1+2+3+4
  ostream_iterator<int> oit(cout, " "); // 迭代器绑定到cout上作为输出使用
  cout << "ostream_iterator: ";
  partial_sum(vec.begin(), vec.end(), oit);// 依次输出前n个数的和
  cout << endl;
  // 第一次，1   第二次，1-2  第三次，1-2-3  第四次，1-2-3-4
  cout << "ostream_iterator(minus): ";
  partial_sum(vec.begin(), vec.end(), oit, minus<int>());// 依次输出第一个数减去（除第一个数外到当前数的和）
  cout << endl;

  // adjacent_difference: 创建一个新序列，新序列中每个新值代表当前元素与上一个元素的差。
  // 第一次，1-0   第二次，2-1  第三次，3-2  第四次，4-3
  cout << "adjacent_difference: ";
  adjacent_difference(vec.begin(), vec.end(), oit); // 输出相邻元素差值 后面-前面
  cout << endl;
  // 第一次，1+0   第二次，2+1  第三次，3+2  第四次，4+3
  cout << "adjacent_difference(plus): ";
  adjacent_difference(vec.begin(), vec.end(), oit, plus<int>()); // 输出相邻元素差值 后面-前面
  cout << endl;

  return 0;
}

/*
accumulate(val = 0): 15
accumulate(val = 1): 16
inner_product(val = 0): 55
ostream_iterator: 1 3 6 10 15
ostream_iterator(minus): 1 -1 -4 -8 -13
adjacent_difference: 1 1 1 1 1
adjacent_difference(plus): 1 3 5 7 9
*/
```

​	