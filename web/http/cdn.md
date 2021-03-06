（1）CDN的加速资源是跟域名绑定的。
（2）通过域名访问资源，首先是通过DNS分查找离用户最近的CDN节点（边缘服务器）的IP
（3）通过IP访问实际资源时，如果CDN上并没有缓存资源，则会到源站请求资源，并缓存到[CDN节点](https://www.zhihu.com/search?q=CDN节点&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A1604554133})上，这样，用户下一次访问时，该CDN节点就会有对应资源的缓存了。



## 功能

归纳起来，CDN具有以下主要功能：

(1)节省骨干网带宽，减少带宽需求量； 

(2)提供服务器端加速，解决由于用户访问量大造成的服务器过载问题； 

(3)服务商能使用Web Cache技术在本地缓存用户访问过的Web页面和对象，实现相同对象的访问无须占用主干的出口带宽，并提高用户访问因特网页面的相应时间的需求； 

(4)能克服网站分布不均的问题，并且能降低网站自身建设和维护成本； 

(5)降低“通信风暴”的影响，提高网络访问的稳定性。 

## 基本原理

CDN的基本原理是广泛采用各种缓存服务器，将这些缓存服务器分布到用户访问相对集中的地区或网络中，在用户访问网站时，利用全局负载技术将用户的访问指向距离最近的工作正常的缓存服务器上，由缓存服务器直接响应用户请求。 

CDN的基本思路是尽可能避开互联网上有可能影响数据传输速度和稳定性的瓶颈和环节，使内容传输的更快、更稳定。通过在网络各处放置[节点服务器](https://baike.baidu.com/item/节点服务器/4576219)所构成的在现有的互联网基础之上的一层智能[虚拟网络](https://baike.baidu.com/item/虚拟网络/855117)，CDN系统能够实时地根据[网络流量](https://baike.baidu.com/item/网络流量/7489548)和各节点的连接、负载状况以及到用户的距离和响应时间等综合信息将用户的请求重新导向离用户最近的服务节点上。其目的是使用户可就近取得所需内容，解决 Internet网络拥挤的状况，提高用户访问网站的响应速度。