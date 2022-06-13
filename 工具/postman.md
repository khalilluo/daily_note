使用raw数据时，json格式的key需要显式的用双引号标识



token使用：在Authorization标签下API Key和OAuth2.0都可以增加token





### 使用变量

```javascript
var temp = parseInt(postman.getGlobalVariable(“pageindex”));//postman.getGlobalVariable获取定义的全局变量
temp += 1;
postman.setGlobalVariable(“pageindex”, temp); 				//postman.setGlobalVariable设置定义的全局变量
```

