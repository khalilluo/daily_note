    
# ubuntu使用systemd-resolved
https://www.xiaoyuanjiu.com/108209.html


# 使用coredns
因为53端口可能被其他dns服务占用
如果在ubuntu上需要先关闭服务systemctl stop systemd-resolved后禁止systemctl disable systemd-resolved

### 搭建过程

　　在服务器上创建以下目录结构：
```
svc
 ├── docker-compose.yml
 └── svc-dns
     ├── Corefile
     └── hosts
```

其中 docker-compose.yml 的文件内容参考以下：
``` yaml
version: "3"

services:
  # DNS
  svc-dns:
    image: coredns/coredns:1.9.3
    container_name: svc-dns
    volumes:
      - ./svc-dns/hosts:/etc/hosts
      - ./svc-dns/Corefile:/Corefile
    ports:
      - "53:53/tcp"
      - "53:53/udp"
    restart: always
    networks:
      - default
networks:
  default:
    driver: bridge
    name: svc
```


Corefile 文件用于指示 DNS 的工作机制，可以参考以下内容。

``` shell
.:53 {
    hosts {
        fallthrough
    }
    # 本机无法解析的 DNS，交给 114.114.114.114 来解析
    forward . 114.114.114.114
    log
    errors
}
```




hosts 文件用于保存本地可以解析的域名。
``` shell
# 自定义解析
10.10.10.20 master.cluster.k8s
10.10.10.21 node1.cluster.k8s
10.10.10.22 node2.cluster.k8s
```

最后，通过 docker-compose 启动服务即可。

### 使用

在需要使用本地 DNS 的服务器或个人电脑上，添加上面搭建的 DNS 服务器地址即可。如 CentOS7 可以修改网络配置 /etc/sysconfig/network-scripts/ifcfg-ens192 文件：
``` shell

TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="none"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="ens192"
UUID="70f117ff-f250-4490-ab18-ff3600936c95"
DEVICE="ens192"
ONBOOT="yes"
IPADDR="10.10.10.20"
PREFIX="16"
GATEWAY="10.10.1.1"
# 指定 DNS 服务器
DNS1="10.10.10.10"
IPV6_PRIVACY="no"

```

然后就可以愉快地使用自定义域名访问服务器了。

``` shell
# 检测 DNS 服务器是否工作正常
$ nslookup node1.cluster.k8s 10.10.10.10
Server:		10.10.10.10
Address:	10.10.10.10#53

Name:	node1.cluster.k8s
Address: 10.10.10.12

$ ping node1.cluster.k8s
PING node1.cluster.k8s (10.10.10.21) 56(84) bytes of data.
64 bytes from node1.cluster.k8s (10.10.10.21): icmp_seq=1 ttl=64 time=0.860 ms
64 bytes from node1.cluster.k8s (10.10.10.21): icmp_seq=2 ttl=64 time=0.134 ms
64 bytes from node1.cluster.k8s (10.10.10.21): icmp_seq=3 ttl=64 time=0.481 ms
```


https://zhuanlan.zhihu.com/p/522918767


# 使用sameersbn/bind
支持网页配置，注意关闭防火墙
https://www.bilibili.com/read/cv17774491