## 搜索排序
--- 
### QSortFilterProxyModel
搜索：
- setFilterKeyColumn：设置过滤列，如果同时设置两行需要同时满足
- setFilterRegExp：设置过滤器，可以是字符串和QRegExp
- setFilterRole：设置过滤的role，需要自己在data里面返回正确的数据
- setRecursiveFilteringEnabled：子项满足时祖先节点也可见
- filterAcceptsRow：需要重载，根据返回值判断该行是否显示。如果过滤方式改变了,比如从过滤第1列变成了过滤第2列,需要调用invalidateFilter()函数

排序：
- lessthan：需要重载，如果重写了lessThan(),那么就不会再调用model的sort方法了