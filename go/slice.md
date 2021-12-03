

## 切片

切片是一种动态数组，比数组操作灵活，长度不是固定的，可以进行追加和删除。

`len()` 和 `cap()` 返回结果可相同和不同 （不指定长度就是切片？）

切片在内存中的组织方式实际上是一个有 3 个域的结构体：指向相关数组的指针，切片长度以及切片容量

#### 数组->切片

切片的初始化格式是：`var slice1 []type = arr1[start:end]`。

这表示 slice1 是由数组 arr1 从 start 索引到 `end-1` 索引之间的元素构成的子集（切分数组，start:end 被称为 slice 表达式）。所以 `slice1[0]` 就等于 `arr1[start]`。这可以在 arr1 被填充前就定义好。

如果某个人写：`var slice1 []type = arr1[:]` 那么 slice1 就等于完整的 arr1 数组（所以这种表示方式是 `arr1[0:len(arr1)]` 的一种缩写）。

关联后两个对象的元素相同



- **注意** 绝对不要用指针指向 slice。切片本身已经是一个引用类型，所以它本身就是一个指针!!

- `s2 := s[:]` 是用切片组成的切片，拥有相同的元素，但是仍然指向相同的相关数组。

下图给出了一个长度为 2，容量为 4 的切片y。

- `y[0] = 3` 且 `y[1] = 5`。
- 切片 `y[0:4]` 由 元素 3，5，7 和 11 组成。**(超过切片长度的取值？会引起panic)**

![](/home/panocom/node/daily_note/go/image/7.2_fig7.2.png)

```go
	var sli_1 [] int      //nil 切片
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_1),cap(sli_1),sli_1)

	var sli_2 = [] int {} //空切片
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_1),cap(sli_2),sli_2)

	var sli_3 = [] int {1, 2, 3, 4, 5}
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_3),cap(sli_3),sli_3)

	sli_4 := [] int {1, 2, 3, 4, 5}
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_4),cap(sli_4),sli_4)

	var sli_5 [] int = make([] int, 5, 8)
	// var sli_5e [] int = new([] int, 5, 8)  // 切片无法new?
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_5),cap(sli_5),sli_5)

	sli_6 := make([] int, 5, 9)
	fmt.Printf("len=%d cap=%d slice=%v\n",len(sli_6),cap(sli_6),sli_6)


	// 输出
	// len=0 cap=0 slice=[]
	// len=0 cap=0 slice=[]
	// len=5 cap=5 slice=[1 2 3 4 5]
	// len=5 cap=5 slice=[1 2 3 4 5]
	// len=5 cap=8 slice=[0 0 0 0 0]
    // len=5 cap=9 slice=[0 0 0 0 0]
```

切片的操作是右闭区间

切片append可以添加多个元素，且需要赋值给其他对象，否则编译不通过

使用copy可以复制切片（一维是深拷贝，不影响原切片，二维？）

Slice 可以组成多维数据结构。内部的 slice 长度可以不同，这和多位数组不同。

```go
	// 数组-
	var twoD [2][3]int
    for i := 0; i < 2; i++ {
        for j := 0; j < 3; j++ {
            twoD[i][j] = i + j
        }
    }
    fmt.Println("2d: ", twoD)	
	// 输出 2d:  [[0 1 2] [1 2 3]]

	// 切片
	twoD := make([][]int, 3)
    for i := 0; i < 3; i++ {
        innerLen := i + 1
        // 内层的切片必须单独分配（通过 make 函数）。
        twoD[i] = make([]int, innerLen)
        for j := 0; j < innerLen; j++ {
            twoD[i][j] = i + j
        }
    }
    fmt.Println("2d: ", twoD)

	// 输出 2d:  [[0] [1 2] [2 3 4]]
```



**多维切片下的 for-range：**

通过计算行数和矩阵值可以很方便的写出如（参考第 7.1.3 节）的 for 循环来，例如（参考第 7.5 节的例子 multidim_array.go）：

```go
for row := range screen {
	for column := range screen[row] {
		screen[row][column] = 1
	}
}
```



**以下代码输出什么？**

```go
func main() {
    a := []int{7, 8, 9}
    fmt.Printf("%+v\n", a)
    ap(a)
    fmt.Printf("%+v\n", a)
    app(a)
    fmt.Printf("%+v\n", a)
}

// 函数内append导致地产数组重新分配内存，函数外的切片没有改变
func ap(a []int) {
    a = append(a, 10)
}

func app(a []int) {
    a[0] = 1
}
```

**答：输出内容为：**

```
[7 8 9]
[7 8 9]
[1 8 9]
```

**解析：**

因为append导致底层数组重新分配内存了，append中的a这个alice的底层数组和外面不是一个，并没有改变外面的
