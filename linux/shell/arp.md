```shell
# 查看指定IP对应的mac地址
arping -f 192.168.10.16 -I ens33

# 查看局域网内主机mac地址，等同查看/proc/net/arp
arp -n
# 单独查看指定IP
arp -n 192.168.20.160
```