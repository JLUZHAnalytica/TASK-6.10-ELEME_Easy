# TASK-6.10-ELEME_Easy

## 我们已经做完了什么

对店铺详情的获取已经基本完成，可以参见 old_research/high_level_parse_demo.py 中对店铺详情的解析部分。其中有一些未能实现的（比如对地点的获取），可以参见同目录下另外一份解析程序。


## 我们还要做什么

1. 根据指定的地点和筛选项目请求店铺列表API，将结果作为一个函数的值返回 **shop_list_spider.py**

2. 店铺列表请求函数的返回值作为参数，请求店铺详情页API，将结果作为一个函数的值返回（必须包括完整的优惠信息，以及所有需求字段）**shop_info_spider.py**

3. 整理解析程序，解析店铺详情的JSON，保存为指定字段的JSON（在根据需求的字段原来的基础上删减）**parse_result.py**

## 协作

* 请尽快将自己负责部分程序的输出文件示例放在 output/demo 文件夹中

* 统一将结果输出文件设置为 output/res

* 用于测试的临时输出文件目录为 output/temp ，提交时可不包括此文件夹中的内容

* 在已有的程序文件基础上可以自行根据需要增添文件

* 文件名的命名请保证有意义，并避免互相冲突

* 本次因不涉及多人修改同一文件，可以直接 push 更改到 master 分支

## 需求

![image](https://github.com/JLUZHAnalytica/TASK-6.10-ELEME_Easy/blob/master/img/WX20200610-232104@2x.png?raw=true)

![image](https://github.com/JLUZHAnalytica/TASK-6.10-ELEME_Easy/blob/master/img/WX20200610-232153@2x.png?raw=true)