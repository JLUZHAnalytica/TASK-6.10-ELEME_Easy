# 这是我们上一阶段做的一些工作

## 文件说明

### high_level_parse_demo.py

这是当时来自别组的大佬写的一个集解析与爬取为一体的高级程序，可惜的是爬取部分还没有完全完成，但是解析部分是正常的

**面向对象编程大法好**

### parse_elema_shop.py

这是组员写的一份解析店铺信息的json，工作正常

### deal_with_resposne.py

这是我写的，专门处理API返回内容整合之后的JSON，其中copy了elema_shop.py的部分内容

**elema_shopid.py**

这是LiuWH写的，当时想到一个逃避饿了么检测的办法：通过收集组员的cookie和ip信息，如果信息够多，再通过取余的算法进行轮换ip和cookie，基本可以实现爬取功能。但可能是因为和组员不能同步导致的，cookie刚一登记上去我还没有使用就失效，所以这个办法就淘汰了。原理就是通过我代理组员的ip进行使用cookie(PS:因为cookie里面绑定了ip信息)，然后api发起get请求就可以获取到网页信息了。

### demo_data/

目录下是各种API文件的demo

old_research/demo_data/batch_shop_demo_full.json 和 old_research/demo_data/batch_shop_demo.json 是店铺API不同参数的请求值。

前者有数字加密，但是可以看到优惠信息是全的。后者没有数字加密，但是优惠信息那栏是空的。

据回忆，hrk大佬对这个问题的研究成果时，需要在API中加一个参数来指定要返回优惠信息。但是因为大群被解散的缘故，聊天记录已无法找回。不过解决这个问题的思路是，看H5页面自己发出的API请求所带的参数。

old_research/demo_data/restaurants_list_demo.json 是商铺列表 API 的返回值整合示例

old_research/demo_data/shopid.txt 是商铺ID的列表



