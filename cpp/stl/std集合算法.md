  集合算法共4个，包含在<algorithm>头文件中，这里全部列出：

- **set_union**: 构造一个有序序列，包含两个序列中所有的不重复元素。重载版本使用自定义的比较操作。
- **set_intersection**: 构造一个有序序列，其中元素在两个序列中都存在。重载版本使用自定义的比较操作。
- **set_difference**: 构造一个有序序列，该序列仅保留第一个序列中存在的而第二个中不存在的元素。重载版本使用自定义的比较操作。
- **set_symmetric_difference**: 构造一个有序序列，该序列取两个序列的对称差集(并集-交集)

```cpp
#include "stdafx.h"
#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

template <class T>
struct display
{
  void operator()(const T&x) const
{
    cout << x << " ";
  }
};

int main(int argc, char* argv[])
{
  int iarr1[] = { 1, 3, 5, 7, 9, 11 };
  int iarr2[] = { 1, 1, 2, 3, 5, 8, 13 };

  multiset<int> s1(iarr1, iarr1 + 6);
  multiset<int> s2(iarr2, iarr2 + 7);
  cout << "s1: ";
  for_each(s1.begin(), s1.end(), display<int>());
  cout << endl;
  cout << "s2: ";
  for_each(s2.begin(), s2.end(), display<int>());
  cout << endl;

  /*** set_union: 构造一个有序序列，包含两个序列中所有的不重复元素。***/
  //  原型：_OutIt set_union(_InIt1 _First1, _InIt1 _Last1, _InIt2 _First2, _InIt2 _Last2, _OutIt _Dest)
  cout << "union of s1 and s2: ";
  // 两个集合合并，相同元素个数取 max(m,n)。
  set_union(s1.begin(), s1.end(), s2.begin(), s2.end(), ostream_iterator<int>(cout, " "));
  cout << endl;

  /*** set_intersection: 构造一个有序序列，其中元素在两个序列中都存在。***/
  //  原型：_OutIt set_union(_InIt1 _First1, _InIt1 _Last1, _InIt2 _First2, _InIt2 _Last2, _OutIt _Dest)
  cout << "Intersection of s1 and s2: ";
  // 两个集合交集，相同元素个数取 min(m,n).
  set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), ostream_iterator<int>(cout, " "));
  cout << endl;

  /*** set_difference: 构造一个有序序列，该序列仅保留第一个序列中存在的而第二个中不存在的元素。***/
  //  原型：_OutIt set_union(_InIt1 _First1, _InIt1 _Last1, _InIt2 _First2, _InIt2 _Last2, _OutIt _Dest)
  cout << "Intersection of s1 and s2: ";
  // 两个集合差集 就是去掉S1中 的s2
  set_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), ostream_iterator<int>(cout, " "));
  cout << endl;

  /*** set_symmetric_difference: 构造一个有序序列，该序列取两个序列的对称差集(并集-交集)。***/
  //  原型：_OutIt set_union(_InIt1 _First1, _InIt1 _Last1, _InIt2 _First2, _InIt2 _Last2, _OutIt _Dest)
  cout << "Intersection of s1 and s2: ";
  // 两个集合对称差集：就是取两个集合互相没有的元素 。两个排序区间，元素相等指针后移，不等输出小的并前进
  // 相同元素的个数 abs(m-n)
  set_symmetric_difference(s1.begin(), s1.end(), s2.begin(), s2.end(), ostream_iterator<int>(cout, " "));
  cout << endl;

  return 0;
}

/*
s1: 1 3 5 7 9 11
s2: 1 1 2 3 5 8 13
union of s1 and s2: 1 1 2 3 5 7 8 9 11 13
Intersection of s1 and s2: 1 3 5
Intersection of s1 and s2: 7 9 11
Intersection of s1 and s2: 1 2 7 8 9 11 13
*/
```

