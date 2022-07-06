- **next_permutation**: 取出当前范围内的排列，并重新排序为下一个字典序排列。重载版本使用自定义的比较操作。
- **prev_permutation**: 取出指定范围内的序列并将它重新排序为上一个字典序排列。如果不存在上一个序列则返回false。重载版本使用自定义的比较操作。

```cpp
#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>

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
	int iarr[] = { 12, 17, 20, 22, 23, 30, 33, 40 };
	vector<int> iv(iarr, iarr + sizeof(iarr) / sizeof(int));

	/*** next_permutation: 取出当前范围内的排列，并重新排序为下一个字典序排列。***/
	//  原型：bool next_permutation(_BidIt _First, _BidIt _Last)
	// 生成下一个排列组合（字典序）
	next_permutation(iv.begin(), iv.end());
	for_each(iv.begin(), iv.end(), display<int>());
	cout << endl;

	/*** prev_permutation: 取出指定范围内的序列并将它重新排序为上一个字典序排列。***/
	//  原型：bool prev_permutation(_BidIt _First, _BidIt _Last)
	prev_permutation(iv.begin(), iv.end());
	for_each(iv.begin(), iv.end(), display<int>());
	cout << endl;

	return 0;
}

/*
12 17 20 22 23 30 40 33
12 17 20 22 23 30 33 40
*/
```

