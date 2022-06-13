```c++
// 对数组去重
std::vector<int> vec;
vec = {1, 2, 4, 5, 1, 6, 1, 2};
std::set<int> s(vec.begin(), vec.end());
vec.assign(s.begin(), s.end());
```