docker中run和start的区别

docker run 后面指定的是一个镜像

而docker start指定的是一个容器

docker run是利用镜像生成容器，并启动容器，而docker start是启动一个之前生成过的容器





### **访问redis**

我们现在用容器部署成功了一个redis，但是和直接安装一个redis不一样，容器就像一台虚拟机一样，想要访问服务，要不就进入到里面，要不就通过暴露端口像远程访问一样来进行访问。

`-p <host-port>：<container-port>`选项可以在启动容器的时候绑定端口。

这个时候使用`-name <name>`来在启动容器的时候定义一个名称，以后查询以及查看日志都会比较方便。

因为redis默认占用6379端口，我们可以将端口6379映射到本地的6379

```shell
$ docker run -d  --name redisHostPort -p 6379:6379 redis:latest
# -i: 交互式操作。
# -t: 终端。
# -d：后台运行

```

```shell
docker exec -it kris-redis redis-cli // 后面是指定运行Redis的指令
sudo docker exec -it redis6380 /bin/bash // 
```



#### 导出

docker save redis>/home/panocom/redis.tar

#### 导入

docker load < redis.tar
