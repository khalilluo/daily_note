### qxorm
#### 导出
MySQL升级到8后数据库编码默认使用utf8mb4，连接MySQL8会有连接异常问题。当前是曲线救国的方式
1. MySQL8导出数据库[[mysql权限#^061bff]]
2. 编辑导出文件，将utf8mb4_0900_ai_ci改为utf8_general_ci，将utf8mb4改为utf8
3. MySQL5导入数据库后再用QxEntityEditor连接生成代码