### 列说明
- type： 此列表示关联类型或访问类型。也就是MySQL决定如何查找表中的行。依次从最优到最差分别为：system > const > eq_ref > ref > range > index > all
- possible_keys：  此列显示在查询中可能用到的索引。如果该列为NULL，则表示没有相关索引，可以通过检查where子句看是否可以添加一个适当的索引来提高性能
- key：此列显示MySQL在查询时实际用到的索引。在执行计划中可能出现possible_keys列有值，而key列为null，这种情况可能是表中数据不多，MySQL认为索引对当前查询帮助不大而选择了全表查询。如果想强制MySQL使用或忽视possible_keys列中的索引，在查询时可使用force index、ignore index
- key_len：  此列显示MySQL在索引里使用的字节数，通过此列可以算出具体使用了索引中的那些列。索引最大长度为768字节，当长度过大时，MySQL会做一个类似最左前缀处理，将前半部分字符提取出做索引。当字段可以为null时，还需要1个字节去记录
- rows：  此列是MySQL在查询中估计要读取的行数。*注意这里不是结果集的行数*
- filtered：这个字段表示存储引擎返回的数据在server层过滤后，剩下多少满足查询的记录数量的比例
- Extra：常见值：
    1.  Using index：使用覆盖索引（如果select后面查询的字段都可以从这个索引的树中获取，不需要通过辅助索引树找到主键，再通过主键去主键索引树里获取其它字段值，这种情况一般可以说是用到了覆盖索引）。
    2.  Using where：使用 where 语句来处理结果，并且查询的列未被索引覆盖。
    3.  Using index condition：查询的列不完全被索引覆盖，where条件中是一个查询的范围。
    4.  Using temporary：MySQL需要创建一张临时表来处理查询。出现这种情况一般是要进行优化的。
    5. Using filesort：将使用外部排序而不是索引排序，数据较小时从内存排序，否则需要在磁盘完成排序。
    6. Select tables optimized away：使用某些聚合函数（比如 max、min）来访问存在索引的某个字段时。


key_len计算规则如下：
-   字符串
-   char(n)：n字节长度
-   varchar(n)：2字节存储字符串长度，如果是utf-8，则长度 3n + 2

-   数值类型
-   tinyint：1字节
-   smallint：2字节
-   int：4字节
-   bigint：8字节　　

-   时间类型　
-   date：3字节
-   timestamp：4字节
-   datetime：8字节
如果字段允许为 NULL，需要1字节记录是否为 NULL