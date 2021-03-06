NAT的实现方式有三种，即静态转换Static Nat、动态转换Dynamic Nat和端口多路复用OverLoad。

### 静态转换

是指将内部网络的私有IP地址转换为公有IP地址，IP地址对是一对一的，是一成不变的，某个私有IP地址只转换为某个公有IP地址。借助于[静态](https://baike.baidu.com/item/静态)转换，可以实现外部网络对内部网络中某些特定设备（如服务器）的访问。

### 动态转换

是指将内部网络的私有IP地址转换为公用IP地址时，IP地址是不确定的，是随机的，所有被授权访问上Internet的私有IP地址可随机转换为任何指定的合法IP地址。也就是说，只要指定哪些内部地址可以进行转换，以及用哪些合法地址作为外部地址时，就可以进行动态转换。动态转换可以使用多个合法外部地址集。当[ISP](https://baike.baidu.com/item/ISP/10152)提供的合法IP地址略少于网络内部的计算机数量时。可以采用动态转换的方式。

### 端口多路复用**NAPT**

（Port address Translation,PAT）是指改变外出数据包的源端口并进行端口转换，即端口地址转换PAT，Port Address Translation）.采用端口多路复用方式。内部网络的所有主机均可共享一个合法外部IP地址实现对Internet的访问，从而可以最大限度地节约IP地址资源。同时，又可隐藏网络内部的所有主机，有效避免来自internet的攻击。因此，网络中应用最多的就是端口多路复用方式。

