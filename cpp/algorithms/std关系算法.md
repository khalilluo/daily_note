关系算法共8个，包含在<algorithm>头文件中，这里只列出一部分算法：

- **equal**: 如果两个序列在标志范围内元素都相等，返回true。重载版本使用输入的操作符代替默认的等于操作符。
- **includes**: 判断第一个指定范围内的所有元素是否都被第二个范围包含，使用底层元素的<操作符，成功返回true。重载版本使用用户输入的函数。
- **max**: 返回两个元素中较大一个。重载版本使用自定义比较操作。
- **min**: 返回两个元素中较小一个。重载版本使用自定义比较操作。
- **max_element**: 返回一个ForwardIterator，指出序列中最大的元素。重载版本使用自定义比较操作。
- **min_element**: 返回一个ForwardIterator，指出序列中最小的元素。重载版本使用自定义比较操作。
- **mismatch**: 并行比较两个序列，指出第一个不匹配的位置，返回一对iterator，标志第一个不匹配元素位置。如果都匹配，返回每个容器的last。重载版本使用自定义的比较操作。

 

```cpp
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
  int iarr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
  vector<int> iv1(iarr, iarr + 5);
  vector<int> iv2(iarr, iarr + 9);

  //  equal: 如果两个序列在标志范围内元素都相等，返回true。
  cout <<"equal: " << equal(iv1.begin(), iv1.end(), iv2.begin()) << endl;//  1 表示相等，因为只比较跟 iv1长度大小的数组

  // includes: 判断第一个指定范围内的所有元素是否都被第二个范围包含，使用底层元素的<操作符，成功返回true。
  // 判断判断iv2中元素是否都出现在iv1中
  cout << "includes: " << includes(iv1.begin(), iv1.end(), iv2.begin(), iv2.end()) << endl;

  // max: 返回两个元素中较大一个。
  cout << "max: " << max(iv1[0],iv1[1]) << endl;
  // min: 返回两个元素中较小一个。
  cout << "min: " << min(iv1[0], iv1[1]) << endl;

  // max_element: 返回一个ForwardIterator，指出序列中最大的元素。
  cout << "max_element: " << *max_element(iv1.begin(), iv1.end()) << endl;
  // min_element: 返回一个ForwardIterator，指出序列中最小的元素。
  cout << "min_element: " << *min_element(iv1.begin(), iv1.end()) << endl;

  //  mismatch: 并行比较两个序列，指出第一个不匹配的位置，返回一对iterator，标志第一个不匹配元素位置。如果都匹配，返回每个容器的last。
  pair<vector<int>::iterator, vector<int>::iterator> pa;
  pa = mismatch(iv1.begin(), iv1.end(), iv2.begin());
  if (pa.first == iv1.end()) //  true 表示相等，因为只比较跟iv1长度大小的数组
    cout << "第一个向量与第二个向量匹配" << endl;
  else
  {
    cout << "两个向量不同点--第一个向量点:" << *(pa.first) << endl; // 这样写很危险，应该判断是否到达end
    cout << "两个向量不同点--第二个向量点:" << *(pa.second) << endl;
  }

  return 0;
}

/*
equal: 1
includes: 0
max: 2
min: 1
max_element: 5
min_element: 1
第一个向量与第二个向量匹配
*/
```

