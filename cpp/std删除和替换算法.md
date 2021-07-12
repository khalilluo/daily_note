- **copy**: 复制序列。

- **copy_backward**: 与copy相同，不过元素是以相反顺序被拷贝。

- **remove**: 删除指定范围内所有等于指定元素的元素。注意，该函数不是真正删除函数。内置函数不适合使用remove和remove_if函数。

- **remove_copy**: 将所有不匹配元素复制到一个制定容器，返回OutputIterator指向被拷贝的末元素的下一个位置。

- **remove_if**: 删除指定范围内输入操作结果为true的所有元素。

- **remove_copy_if**: 将所有不匹配元素拷贝到一个指定容器。

  

```cpp

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional> // 定义了greater<int>()

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
  int iarr1[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
  vector<int> iv1(iarr1, iarr1 + sizeof(iarr1) / sizeof(int));
  vector<int> iv2(9);

  /*** copy: 复制序列 ***/
  //  原型：_OutIt copy(_InIt _First, _InIt _Last,_OutIt _Dest)
  copy(iv1.begin(), iv1.end(), iv2.begin());
  cout << "copy(iv2): ";
  for_each(iv2.begin(), iv2.end(), display<int>());
  cout << endl;

  /*** copy_backward: 与copy相同，不过元素是以相反顺序被拷贝。***/
  //  原型：_BidIt2 copy_backward(_BidIt1 _First, _BidIt1 _Last,_BidIt2 _Dest)
  copy_backward(iv1.begin(), iv1.end(), iv2.rend());
  cout << "copy_backward(iv2): ";
  for_each(iv2.begin(), iv2.end(), display<int>());
  cout << endl;

  /*** remove: 删除指定范围内所有等于指定元素的元素。***/
  //  原型：_FwdIt remove(_FwdIt _First, _FwdIt _Last, const _Ty& _Val)
  remove(iv1.begin(), iv1.end(), 5); // 删除元素5
  cout << "remove(iv1): ";
  for_each(iv1.begin(), iv1.end(), display<int>());
  cout << endl;

  /*** remove_copy: 将所有不匹配元素复制到一个制定容器，返回OutputIterator指向被拷贝的末元素的下一个位置。***/
  //  原型：_OutIt remove_copy(_InIt _First, _InIt _Last,_OutIt _Dest, const _Ty& _Val)
  vector<int> iv3(8);
  remove_copy(iv1.begin(), iv1.end(), iv3.begin(), 4); // 去除4 然后将一个容器的元素复制到另一个容器
  cout << "remove_copy(iv3): ";
  for_each(iv3.begin(), iv3.end(), display<int>());
  cout << endl;

  /*** remove_if: 删除指定范围内输入操作结果为true的所有元素。***/
  //  原型：_FwdIt remove_if(_FwdIt _First, _FwdIt _Last, _Pr _Pred)
  remove_if(iv3.begin(), iv3.end(), bind2nd(less<int>(), 6)); //  将小于6的元素 "删除"
  cout << "remove_if(iv3): ";
  for_each(iv3.begin(), iv3.end(), display<int>());
  cout << endl;

  /*** remove_copy_if: 将所有不匹配元素拷贝到一个指定容器。***/
  // 原型：_OutIt remove_copy_if(_InIt _First, _InIt _Last,_OutIt _Dest, _Pr _Pred)
  //  将iv1中小于6的元素 "删除"后，剩下的元素再复制给iv3
  remove_copy_if(iv1.begin(), iv1.end(), iv2.begin(), bind2nd(less<int>(), 4));
  cout << "remove_if(iv2): ";
  for_each(iv2.begin(), iv2.end(), display<int>());
  cout << endl;

  return 0;
}

/*
copy(iv2): 0 1 2 3 4 5 6 7 8
copy_backward(iv2): 8 7 6 5 4 3 2 1 0
remove(iv1): 0 1 2 3 4 6 7 8 8
remove_copy(iv3): 0 1 2 3 6 7 8 8
remove_if(iv3): 6 7 8 8 6 7 8 8
remove_if(iv2): 4 6 7 8 8 3 2 1 0
*/
```

- **replace**: 将指定范围内所有等于vold的元素都用vnew代替。
- **replace_copy**: 与replace类似，不过将结果写入另一个容器。
- **replace_if**: 将指定范围内所有操作结果为true的元素用新值代替。
- **replace_copy_if**: 与replace_if，不过将结果写入另一个容器。
- **swap**: 交换存储在两个对象中的值。
- **swap_range**: 将指定范围内的元素与另一个序列元素值进行交换。
- **unique**: 清除序列中重复元素，和remove类似，它也不能真正删除元素。重载版本使用自定义比较操作。
- **unique_copy**: 与unique类似，不过把结果输出到另一个容器。

```cpp
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional> // 定义了greater<int>()

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
  int iarr[] = { 8, 10, 7, 8, 6, 6, 7, 8, 6, 7, 8 };
  vector<int> iv(iarr, iarr + sizeof(iarr) / sizeof(int));

  /*** replace: 将指定范围内所有等于vold的元素都用vnew代替。***/
  //  原型：void replace(_FwdIt _First, _FwdIt _Last, const _Ty& _Oldval, const _Ty& _Newval)
  // 将容器中6 替换为 3
  replace(iv.begin(), iv.end(), 6, 3);
  cout << "replace(iv): ";
  for_each(iv.begin(), iv.end(), display<int>()); // 由于_X是static 所以接着 增长
  cout << endl; // iv:8 10 7 8 3 3 7 8 3 7 8

  /*** replace_copy: 与replace类似，不过将结果写入另一个容器。***/
  //  原型：_OutIt replace_copy(_InIt _First, _InIt _Last, _OutIt _Dest, const _Ty& _Oldval, const _Ty& _Newval)
  vector<int> iv2(12);
  // 将容器中3 替换为 5，并将结果写入另一个容器。
  replace_copy(iv.begin(), iv.end(), iv2.begin(), 3, 5);
  cout << "replace_copy(iv2): ";
  for_each(iv2.begin(), iv2.end(), display<int>());
  cout << endl; // iv2:8 10 7 8 5 5 7 8 5 7 8 0（最后y一个残留元素）

  /*** replace_if: 将指定范围内所有操作结果为true的元素用新值代替。***/
  //  原型：void replace_if(_FwdIt _First, _FwdIt _Last, _Pr _Pred, const _Ty& _Val)
  // 将容器中小于 5 替换为 2
  replace_if(iv.begin(), iv.end(), bind2nd(less<int>(), 5), 2);
  cout << "replace_copy(iv): ";
  for_each(iv.begin(), iv.end(), display<int>());
  cout << endl; // iv:8 10 7 8 2 5 7 8 2 7 8

  /*** replace_copy_if: 与replace_if，不过将结果写入另一个容器。***/
  //  原型：_OutIt replace_copy_if(_InIt _First, _InIt _Last, _OutIt _Dest, _Pr _Pred, const _Ty& _Val)
  // 将容器中小于 5 替换为 2，并将结果写入另一个容器。
  replace_copy_if(iv.begin(), iv.end(), iv2.begin(), bind2nd(equal_to<int>(), 8), 9);
  cout << "replace_copy_if(iv2): ";
  for_each(iv2.begin(), iv2.end(), display<int>());
  cout << endl; // iv2:9 10 7 8 2 5 7 9 2 7 8 0(最后一个残留元素)

  int iarr3[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, };
  vector<int> iv3(iarr3, iarr3 + sizeof(iarr3) / sizeof(int));
  int iarr4[] = { 8, 10, 7, 8, 6, 6, 7, 8, 6, };
  vector<int> iv4(iarr4, iarr4 + sizeof(iarr4) / sizeof(int));

  /*** swap: 交换存储在两个对象中的值。***/
  //  原型：_OutIt replace_copy_if(_InIt _First, _InIt _Last, _OutIt _Dest, _Pr _Pred, const _Ty& _Val)
  // 将两个容器中的第一个元素交换
  swap(*iv3.begin(), *iv4.begin());
  cout << "swap(iv3): ";
  for_each(iv3.begin(), iv3.end(), display<int>());
  cout << endl;

  /*** swap_range: 将指定范围内的元素与另一个序列元素值进行交换。***/
  //  原型：_FwdIt2 swap_ranges(_FwdIt1 _First1, _FwdIt1 _Last1, _FwdIt2 _Dest)
  // 将两个容器中的全部元素进行交换
  swap_ranges(iv4.begin(), iv4.end(), iv3.begin());
  cout << "swap_range(iv3): ";
  for_each(iv3.begin(), iv3.end(), display<int>());
  cout << endl;

  /*** unique: 清除序列中相邻的重复元素，和remove类似，它也不能真正删除元素。***/
  //  原型：_FwdIt unique(_FwdIt _First, _FwdIt _Last, _Pr _Pred)
  unique(iv3.begin(), iv3.end());
  cout << "unique(iv3): ";
  for_each(iv3.begin(), iv3.end(), display<int>());
  cout << endl;

  /*** unique_copy: 与unique类似，不过把结果输出到另一个容器。***/
  //  原型：_OutIt unique_copy(_InIt _First, _InIt _Last, _OutIt _Dest, _Pr _Pred)
  unique_copy(iv3.begin(), iv3.end(), iv4.begin());
  cout << "unique_copy(iv4): ";
  for_each(iv4.begin(), iv4.end(), display<int>());
  cout << endl;

  return 0;
}

/*
replace(iv): 8 10 7 8 3 3 7 8 3 7 8
replace_copy(iv2): 8 10 7 8 5 5 7 8 5 7 8 0
replace_copy(iv): 8 10 7 8 2 2 7 8 2 7 8
replace_copy_if(iv2): 9 10 7 9 2 2 7 9 2 7 9 0
swap(iv3): 8 1 2 3 4 5 6 7 8
swap_range(iv3): 0 10 7 8 6 6 7 8 6
unique(iv3): 0 10 7 8 6 7 8 6 6
unique_copy(iv4): 0 10 7 8 6 7 8 6 8
*/
```

