实体首部字段被包含在报文首部，而实体主体被包含在报文主体中

HTTP 报文的报文主体（message body）（如果存在的话）是用来运载请求或响应的有效载荷主体（payload body）的。除非应用了传输编码，报文主体等价于有效载荷主体

下面以分块传输编码（Chunked transfer encoding）的一个[示例](https://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%E5%88%86%E5%9D%97%E4%BC%A0%E8%BE%93%E7%BC%96%E7%A0%81%23.E7.BC.96.E7.A0.81.E7.9A.84.E5.BA.94.E7.AD.94)来解释

```http
HTTP/1.1 200 OK
Content-Type: text/plain
Transfer-Encoding: chunked

25
This is the data in the first chunk

1C
and this is the second one

3
con

8
sequence

0
```

示例中的有效载荷主体（payload body）为 This is the data in the first chunk、and this is the second one、con 和 sequence 这几行。而报文主体（message body）为第一个空行以后的所有部分，除了有效载荷主体之外，还包括了 25、1C 等行和几个空行（最后为“0/r/n/r/n”，此处显示有误）。



**max-age**
max-age是HTTP/1.1中,他是指我们的web中的文件被用户访问(请求)后的存活时间,是个相对的值,相对Request_time(请求时间).
例如:A.html 用户请求时间是18:00,max-age设置的是600的话,相当18:00+600秒过期,也就是相对18:00的时间后面600秒后过期.默认的max-age是由Expires算出来的

**Expires**
Expires是HTTP/1.0中的,它比max-age要麻烦点.Expires指定的时间分下面二种,这个主要考虑到apache中设置是A还是M.