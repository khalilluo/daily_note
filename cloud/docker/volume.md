```shell
# 创建一个容器可以使用和存储数据的卷 docker volume create [OPTIONS] [VOLUME]
docker volume create my_volume

# 查看容器卷
docker volume list

# 查看指定容器卷详细信息，包括容器卷保存的目录
docker volume inspect my_volume
```