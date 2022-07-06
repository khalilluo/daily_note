```CMAKE
# 变量 var1 被设置成 13
# 如果 var1 在cache中已经存在，该命令不会overwrite cache中的值
SET(var1 13)

# 如果cache存在该变量，使用cache中变量
# 如果cache中不存在，将该值写入cache
SET(var1 13 ... CACHE ...)

# 不论cache中是否存在，始终使用该值
SET(var1 13 ... CACHE ... FORCE)

```

如果设置了变量无法删除，则可以删除CMakeCache.txt文件

