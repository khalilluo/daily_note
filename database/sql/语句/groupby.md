```sql
-- 统计各版本Version对应的行数
select count(1) As 行数, Version from testTable group by Version
```