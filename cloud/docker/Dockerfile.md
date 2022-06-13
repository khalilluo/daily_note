```dtd
FROM golang:latest # 指定基础镜像（必须有的指令，并且必须是第一条指令）
WORKDIR $GOPATH/src/docker/emergency
COPY . $GOPATH/src/docker/emergency
RUN go build .
EXPOSE 8001
ENTRYPOINT ["./emergencyServer"]
```

**1、 FROM**

指定基础镜像（必须有的指令，并且必须是第一条指令）

**2、 WORKDIR**

格式为 `WORKDIR` <工作目录路径>

使用 `WORKDIR` 指令可以来**指定工作目录**（或者称为当前目录），以后各层的当前目录就被改为指定的目录，如果目录不存在，`WORKDIR` 会帮你建立目录

Dockerfile中其后的命令RUN、CMD、ENTRYPOINT、ADD、COPY 等命令都会在该目录下执行。在使用docker run运行容器时，可以通过-w参数覆盖构建时所设置的工作目录

**3、COPY**

格式：

```
COPY <源路径>... <目标路径>COPY ["<源路径1>",... "<目标路径>"]
```

`COPY` 指令将从构建上下文目录中 <源路径> 的文件/目录**复制**到新的一层的镜像内的 <目标路径> 位置

**4、RUN**

用于执行命令行命令

格式：`RUN` <命令>

run一次形成一行，建议合并运行。其他命令相同

```dockerfile
RUN cp /usr/local/aa.tar.gz /opt && \
       tar xvf /opt/aa.tar.gz && \
       rm -rf /opt/aa.tar.gz
```

**5、EXPOSE**

格式为 `EXPOSE` <端口1> [<端口2>…]

`EXPOSE` 指令是**声明运行时容器提供服务端口，这只是一个声明**，在运行时并不会因为这个声明应用就会开启这个端口的服务

在 Dockerfile 中写入这样的声明有两个好处

- 帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射
- 运行时使用随机端口映射时，也就是 `docker run -P` 时，会自动随机映射 `EXPOSE` 的端口

**6、ENTRYPOINT**

`ENTRYPOINT` 的格式和 `RUN` 指令格式一样，分为两种格式

- `exec` 格式：

  ```
  <ENTRYPOINT> "<CMD>"
  ```

- `shell` 格式：

  ```
  ENTRYPOINT [ "curl", "-s", "http://ip.cn" ]
  ```

`ENTRYPOINT` 指令是**指定容器启动程序及参数**