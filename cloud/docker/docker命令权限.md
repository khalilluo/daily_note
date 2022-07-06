### Linux
docker守护进程启动的时候，会默认赋予名为docker的用户组读写Unix socket的权限，因此只要创建docker用户组，并将当前用户加入到docker用户组中，那么当前用户就有权限访问Unix socket了，进而也就可以执行docker相关命令

```shell
sudo groupadd docker   #添加docker用户组`
sudo gpasswd -a $USER docker   #将登陆用户加入到docker用户组中`
newgrp docker   #更新用户组`
```