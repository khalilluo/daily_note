- **merge**: 合并两个有序序列，存放到另一个序列。重载版本使用自定义的比较。
- **random_shuffle**: 对指定范围内的元素随机调整次序。重载版本输入一个随机数产生操作。
- **nth_element**: 将范围内的序列重新排序，使所有小于第n个元素的元素都出现在它前面，而大于它的都出现在后面。重载版本使用自定义的比较操作。
- **reverse**: 将指定范围内元素重新反序排序。
- **sort**: 以升序重新排列指定范围内的元素。重载版本使用自定义的比较操作。
- stable_sort: 与sort类似，不过保留相等元素之间的顺序关系。

```cpp
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional> // 定义了greater<int>()

using namespace std;

// 要注意的技巧
template <class T>
struct display
{
  void operator()(const T&x) const
{
    cout << x << " ";
  }
};

// 如果想从大到小排序，可以采用先排序后反转的方式，也可以采用下面方法:
// 自定义从大到小的比较器，用来改变排序方式
bool Comp(const int& a, const int& b) {
  return a > b;
}

int main(int argc, char* argv[])
{
  int iarr1[] = { 0, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8 };
  vector<int> iv1(iarr1, iarr1 + sizeof(iarr1) / sizeof(int));
  vector<int> iv2(iarr1 + 4, iarr1 + 8); // 4 5 6 6
  vector<int> iv3(15);

  /*** merge: 合并两个有序序列，存放到另一个序列 ***/
  // iv1和iv2合并到iv3中（合并后会自动排序）
  merge(iv1.begin(), iv1.end(), iv2.begin(), iv2.end(), iv3.begin());
  cout << "merge合并后: ";
  for_each(iv3.begin(), iv3.end(), display<int>());
  cout << endl;

  /*** random_shuffle: 对指定范围内的元素随机调整次序。***/
  int iarr2[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
  vector<int> iv4(iarr2, iarr2 + sizeof(iarr2) / sizeof(int));
  // 打乱顺序  
  random_shuffle(iv4.begin(), iv4.end());
  cout << "random_shuffle打乱后: ";
  for_each(iv4.begin(), iv4.end(), display<int>());
  cout << endl;

  /*** nth_element: 将范围内的序列重新排序。***/
  // 将小于iv.begin+5的放到左边   
  nth_element(iv4.begin(), iv4.begin() + 5, iv4.end());
  cout << "nth_element重新排序后: ";
  for_each(iv4.begin(), iv4.end(), display<int>());
  cout << endl;

  /*** reverse: 将指定范围内元素重新反序排序。***/
  reverse(iv4.begin(), iv4.begin());
  cout << "reverse翻转后: ";
  for_each(iv4.begin(), iv4.end(), display<int>());
  cout << endl;

  /*** sort: 以升序重新排列指定范围内的元素。***/
  // sort(iv4.begin(), iv4.end(), Comp); // 也可以使用自定义Comp()函数
  sort(iv4.begin(), iv4.end(), greater<int>());
  cout << "sort排序（倒序）: ";
  for_each(iv4.begin(), iv4.end(), display<int>());
  cout << endl;

  /*** stable_sort: 与sort类似，不过保留相等元素之间的顺序关系。***/
  int iarr3[] = { 0, 1, 2, 3, 3, 4, 4, 5, 6 };
  vector<int> iv5(iarr3, iarr3 + sizeof(iarr3) / sizeof(int));
  stable_sort(iv5.begin(), iv5.end(), greater<int>());
  cout << "stable_sort排序（倒序）: ";
  for_each(iv5.begin(), iv5.end(), display<int>());
  cout << endl;

  return 0;
}

/*
merge合并后: 0 1 2 3 4 4 5 5 6 6 6 6 6 7 8
random_shuffle打乱后: 8 1 6 2 0 5 7 3 4
nth_element重新排序后: 0 1 2 3 4 5 6 7 8
reverse翻转后: 0 1 2 3 4 5 6 7 8
sort排序（倒序）: 8 7 6 5 4 3 2 1 0
stable_sort排序（倒序）: 6 5 4 4 3 3 2 1 0
*/
```

