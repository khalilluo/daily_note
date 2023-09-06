

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
# -p: hostPort:co  ntainerPort
# -P: 将容器暴露的所有端口，都随机映射到宿主机上

```

```shell
docker exec -it kris-redis redis-cli // 后面是指定运行Redis的指令
sudo docker exec -it redis6380 /bin/bash // 
```



#### 导出导入

1. docker save保存的是镜像（image），docker export保存的是容器（container）；
2. docker load用来载入镜像包，docker import用来载入容器包，但两者都会恢复为镜像；
3. docker load不能对载入的镜像重命名，而docker import可以为镜像指定新名称。

```shell
docker save redis>/home/panocom/redis.tar
docker load < redis.tar
```
 


#### 映射目录

```shell
# -v指定挂载目录，前面是宿主机目录，后面是容器的目录。容器会自带创建目录，容器不可以使用相对目录
# 注意挂载目录跟当前用户的权限问题，通常挂载到当前用户目录下为佳
docker run -it --name ff -v /home/panocom/code:/home:rw mongo /bin/bash
# 实例中的rw为读写，ro为只读

# 映射相同文件夹会将之前ADD和COPY的数据清空 ？

# 查看
dokcer inspect container | grep ***


# --mount type=bind
docker run -it --mount type=bind,src=$(cd `dirname $0`; pwd)/data,dst=/var/lib/mysql
```



### 网络

```dockerfile
--network host # 与宿主机共享网络
--network bridge # 默认模式，使用-p指定导出端口
--network some-network # 使用指定some-network，使用docker network create创建。当有多个独立的container之间需要彼此访问时，推荐使用自建bridge网络
```



挂载的本地目录在容器中没有执行权限时，需要--privileged=true参数
