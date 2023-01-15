自动计算时间差 ^844884
```sql
# 建表的时候，建立虚拟列（只有表元数据而没有保存到磁盘，具体内容是在查表时计算所得）
generated always as(sec_to_time(timestampdiff(second, 'begint','end'))) virtual
```

^48ed60
