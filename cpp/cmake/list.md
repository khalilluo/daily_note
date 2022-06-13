```cmake

set (list_test a b c d) # 创建列表变量"a;b;c;d"
list (LENGTH list_test length)

# 输出：LENGTH: 4
message (">>> LENGTH: ${length}")

# 添加
list (APPEND list_test 1 2 3 4)

```