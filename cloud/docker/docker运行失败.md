尝试运行以下命令
setenforece 0或者修改/etc/selinux/config的SELINUX为disabled
systemctl stop firewalld.service或者service firewalld stop
service docker restart
