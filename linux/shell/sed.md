```shell
# 替换IP，双引号才能使用变量
sed -ri "s/([0-9]{1,3}\.){3}[0-9]{1,3}/${newip}/g" /etc/keepalived/keepalived.conf 

# 替换有state的整行，注意/c的位置
sed -rin "/state/cstate ${KA_STATE}" /etc/keepalived/keepalived.conf
```