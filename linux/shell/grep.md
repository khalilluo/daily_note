-A  -B -C(大写)    后面都跟阿拉伯数字   
-A是显示匹配后和它后面的n行。after   
-B是显示匹配行和它前面的n行。 before  
-C是匹配行和它前后各n行。 context


```shell
# -A  -B -C(大写)    后面都跟阿拉伯数字   
# -A是显示匹配后和它后面的n行。after   
# -B是显示匹配行和它前面的n行。 before  
# -C是匹配行和它前后各n行。 context

# 显示该行和后面的1行
grep -A 1 hello test.txt
# 显示该行和前面的1行
grep -B 1 hello test.txt
# 显示该行和前后1行
grep -C 1 hello test.txt

# -v 反查
ps -ef | grep abc | grep -v grep

# -c 统计关键字的个数
grep -c keyword filename1
ps -ef | grep -c root

```
