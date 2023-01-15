### std::sort

不稳定排序，元素相同时会把顺序打乱
在Linux和Windows下判断数据是否大个数不同，Linux下通常是16。数据量小直接用插入排序，效率较高

数据量大时会综合使用排序方法，首先做条件判断，数据多用快速排序，数据少用插入排序，递归层次深用堆排序。自定义排序算法时数据相同返回法false否则可能崩溃，所以 __comp 函数两个参数的比较必须是 v1 > v2 或者 v1 < v2，不能 v1 >= v2 或者 v1 <= v2 这样的

Compare 是一些标准库函数针对用户提供的函数对象类型所期待的一组要求，其实就是要满足严格若排序关系，comp 需要下面三条要求：
- `对于任意元素a，需满足 comp(a, a) == false`
- `对于任意两个元素a和b，若 comp(a, b)==true 则要满足 comp(b, a)==false`
- `对于任意三个元素a、b和c，若 comp(a, b)==true 且 comp(b, c)==true 则需要满足 comp(a, c)==true`
https://blog.csdn.net/albertsh/article/details/119523587


``` markdown
对于STL的sort算法，数据量大的时候，采用QuickSort, 分段递归排序。
一旦分段后的数据量小于某个门槛，为避免QuickSort 的递归调用带来过大的额外负荷(overhead)，就改用InsertionSort。 
如果递归层次过深。还会改用HeapSort。

- QuickSort 快速排序 -- 不稳定
    + 算法描述，假设S代表将被处理的序列
        1）如果S的元素个数为0或1，结束
        2）取S中的任何一个元素，作为枢轴(pivot)v
        3）将S分割为L,R两段，使L内的每个元素均小于或等于v；使R段内的每一个元素大于或等于v
        4）对L、R递归执行QuickSort

- InsertionSort 插入排序-- 稳定
- HeapSort 堆排序-- 不稳定
```