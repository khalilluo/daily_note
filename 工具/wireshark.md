### 抓取指定IP或者规则的数据包

在捕获前的规则OPTION中设置过滤规则，比如host 120.24.90.201 或者 ip.addr == 120.24.90.201 



常用

host 120.24.90.201

 ip.addr == 120.24.90.201 

 ip.src == 120.24.90.201 

tcp.port == 8888

rtp.p_type == 96   // h264的payloadtype



### 数据对应



![](./image/v2-c968840daa2b9440448a0fdb24349f52_720w (1).jpg)





### Tips

EDIT->FIND直接根据内容查找对应的包

EDIT->MARK标记包



rtp丢包分析 ：

telephony->rtp->stream analize



rtp.p_type 筛选payloadtype 比如H264是96

edit->Preferences->h264设置payloadtype96可以将显示页面的RTP数据显示为H264格式



telephone（电话）->RTP->RTP流分析可以看丢包率等流信息



列宽适应当前信息

view->resize all column