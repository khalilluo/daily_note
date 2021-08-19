- 查找算法共13个，包含在<algorithm>头文件中，用来提供元素排序策略，这里只列出一部分算法：
- adjacent_find: 在iterator对标识元素范围内，查找一对相邻重复元素，找到则返回指向这对元素的第一个元素的ForwardIterator。否则返回last。重载版本使用输入的二元操作符代替相等的判断。
- count: 利用等于操作符，把标志范围内的元素与输入值比较，返回相等元素个数。
- count_if: 利用输入的操作符，对标志范围内的元素进行操作，返回结果为true的个数。
- binary_search: 在有序序列中查找value，找到返回true。重载的版本实用指定的比较函数对象或函数指针来判断相等。
- equal_range: 功能类似equal，返回一对iterator，第一个表示lower_bound，第二个表示upper_bound。
- find: 利用底层元素的等于操作符，对指定范围内的元素与输入值进行比较。当匹配时，结束搜索，返回指向该元素的Iterator。
- find_if: 使用输入的函数代替等于操作符执行find。
- search: 给出两个范围，返回一个ForwardIterator，查找成功指向第一个范围内第一次出现子序列(第二个范围)的位置，查找失败指向last1。重载版本使用自定义的比较操作。
- search_n: 在指定范围内查找val出现n次的子序列。重载版本使用自定义的比较操作

```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>  

using namespace std;

int main(int argc, char* argv[])
{
  int iarr[] = { 0, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8 };
  vector<int> iv(iarr, iarr + sizeof(iarr) / sizeof(int));

  /*** adjacent_find: 在iterator对标识元素范围内，查找一对相邻重复元素 ***/
  // 原型：_FwdIt adjacent_find(_FwdIt _First, _FwdIt _Last)
  cout << "adjacent_find: ";
  cout << *adjacent_find(iv.begin(), iv.end()) << endl;

  /*** count: 利用等于操作符，把标志范围内的元素与输入值比较，返回相等元素个数。***/
  // 原型：count(_InIt _First, _InIt _Last, const _Ty& _Val)
  cout << "count(==7): ";
  cout << count(iv.begin(), iv.end(), 6) << endl;// 统计6的个数

  /*** count_if: 利用输入的操作符，对标志范围内的元素进行操作，返回结果为true的个数。***/
  // 原型：count_if(_InIt _First, _InIt _Last, _Pr _Pred)
  // 统计小于7的元素的个数 :9个
  cout << "count_if(<7): ";
  cout << count_if(iv.begin(), iv.end(), bind2nd(less<int>(), 7)) << endl;

  /*** binary_search: 在有序序列中查找value，找到返回true。***/
  // 原型：bool binary_search(_FwdIt _First, _FwdIt _Last, const _Ty& _Val)
  cout << "binary_search: ";
  cout << binary_search(iv.begin(), iv.end(), 4) << endl; // 找到返回true

  /*** equal_range: 功能类似equal，返回一对iterator，第一个表示lower_bound，第二个表示upper_bound。***/
  // 原型：equal_range(_FwdIt _First, _FwdIt _Last, const _Ty& _Val)
  pair<vector<int>::iterator, vector<int>::iterator> pairIte;  
  pairIte = equal_range(iv.begin(), iv.end(), 3);
  cout << "pairIte.first:" << *(pairIte.first) << endl;// lowerbound 3   
  cout << "pairIte.second:" << *(pairIte.second) << endl; // upperbound 4

  /*** find: 利用底层元素的等于操作符，对指定范围内的元素与输入值进行比较。***/
  // 原型：_InIt find(_InIt _First, _InIt _Last, const _Ty& _Val)
  cout << "find: ";
  cout << *find(iv.begin(), iv.end(), 4) << endl; // 返回元素为4的元素的下标位置

  /*** find_if: 使用输入的函数代替等于操作符执行find。***/
  // 原型：_InIt find_if(_InIt _First, _InIt _Last, _Pr _Pred)
  cout << "find_if: " << *find_if(iv.begin(), iv.end(), bind2nd(greater<int>(), 2)) << endl; // 返回大于2的第一个元素的位置：3 

  /*** search: 给出两个范围，返回一个ForwardIterator，查找成功指向第一个范围内第一次出现子序列的位置。***/
  // 原型：_FwdIt1 search(_FwdIt1 _First1, _FwdIt1 _Last1, _FwdIt2 _First2, _FwdIt2 _Last2)
  // 在iv中查找 子序列 2 3 第一次出现的位置的元素   
  int iarr3[3] = { 2, 3 };
  vector<int> iv3(iarr3, iarr3 + 2);
  cout << "search: " << *search(iv.begin(), iv.end(), iv3.begin(), iv3.end()) << endl;

  /*** search_n: 在指定范围内查找val出现n次的子序列。***/
  // 原型：_FwdIt1 search_n(_FwdIt1 _First1, _FwdIt1 _Last1, _Diff2 _Count, const _Ty& _Val)
  // 在iv中查找 2个6 出现的第一个位置的元素   
  cout << "search_n: " << *search_n(iv.begin(), iv.end(), 2, 6) << endl;  

  return 0;
}

/*
adjacent_find: 6
count(==7): 3
count_if(<7): 9
binary_search: 1
pairIte.first:3
pairIte.second:4
find: 4
find_if: 3
search: 2
search_n: 6
*/
```

