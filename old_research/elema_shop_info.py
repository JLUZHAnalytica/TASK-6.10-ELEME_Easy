# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
# import requests
# url = 'https://h5.ele.me/pizza/shopping/restaurants/E3803185435017690181/batch_shop'
# headers = {'accept': 'application/json, text/plain, */*',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'zh-CN,zh;q=0.9',
# 'cookie': '__wpkreporterwid_=52a4dd0e-f0e1-45f9-393d-9914d1e2f80d; ubt_ssid=mqmrh8166zjhen0ylww5cu3k9ppdre2l_2020-06-07; perf_ssid=zpq5i8uj861pb5b5mj7t9d1ees1qweyy_2020-06-07; ut_ubt_ssid=blk5zezfz4t1hu1redces0g8j56w11tg_2020-06-07; cna=e9pXF21sJigCAXF2DXOwC4iK; _bl_uid=Utk6wbF644Iremvn5zzt35k66e83; _utrace=28fe3bba1c0ce75484a3e70f9f99d0e3_2020-06-07; _samesite_flag_=true; t=b86f23f7ee94141c087ef5d6f60ac6b5; _tb_token_=ed355b1388036; csg=09484496; t_eleuc4=id4=0%40BA%2FvuHCrrRtQk0MqN0A8ZvMLx537DUeqNxrjZQ%3D%3D; munb=2206579483915; track_id=1591519662|1007f241d03ec6fad54df7f148fd7ac1b04c216fcbaff38b51|ff7c1e2216e2db4412046bcf836fcbf7; tzyy=9933c52edbe4e66dbe32ecc02f6db1fa; cookie2=100cc461ef8464a5e59d11b41db80870; l=eBOWF_cmQVTtCnFKBO5Zhurza77t3IOXhsPzaNbMiInca1yA_hL2aNQDdKL98dtjgtfvxeKPOzL1BRn2JxaU-xaVX9zbTF6ZmYvvF; USERID=1000081304180; UTUSER=1000081304180; SID=CQAAAOjZfap06gAEAABUbGXlEAwxTzSc-Df4jV78HQ48Ise0o10lLnzh; ZDS=1.0|1591571541|WGdv8IeEintFPiD2CWLtgO2Unrdq32nJYQGsZyYw/NostACLD6dj0b4rGRuTyYARdoAGQhOWNRu5zJgHLoGlhw==; x5check_ele=YbcTUKJkbaNwLZWZBOWNnctwWElpmGQZ6Nf7s6mEM6E%3D; x5sec=7b227466653b32223a223361663166356630396339343136376536623566396162323234323165663266434c577739765946454d7952683436583262765176674561447a45774d4441774f44457a4d4451784f4441374d673d3d227d; isg=BMrKpE9UoNjpUix1GcKiVYxdG7Bsu04VQJF0XVQDdp2oB2rBPEueJRBxE3Xb98at',
# 'referer': 'https://h5.ele.me/shop/',
# 'sec-fetch-dest': 'empty',
# 'sec-fetch-mode': 'cors',
# 'sec-fetch-site': 'same-origin',
# 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
# # x-font-version: bf567591c8124d0bbd5642aaac739edd
# 'x-shard': 'shopid=E11293485602379493858;loc=116.322056,39.89491',
# 'x-ua': 'RenderWay/H5 AppName/wap',
# 'x-uab': "124#qmW8jxEmxG0xAPIhR0c7HeKVVpRFx4SskGO1Me+5ZXguXA0v3UtKPvNmSMx+Zk+hswFEEFeDtxEXu2TOmxnkyZJ1gC6xzND3y4WAQ/cu0EG2MN81EhwKTIyB1lZ82v5xm7tD2JdopY1PvWzYSrqOtVr6+UABNgRqzVrp/Rb68/SIjvqQWaH7y62ZlMan6KvBIZYLlw/2mfWeI8bpgTzo72bX/YDJ67vtQC/plm/IHf+ZI8LLgTSo1nIelML267vBIZYLlwYnmfWeIqXpg5Sd1Z2ZlMXng7OBJZEUl5KKmfuUI8Lpg7TVdOxzlbangKC0InYLlBB3neHmCaEJNONNH4qmUdYspycI71Y80/6Tdc/wmayIdrC5SqP2QDEZYCJsWVNjb0z7MFfDF+OSLYWhbPtdL9I8WIwT7QNjDBmmpsm5W7Z+GZCEj0zCGmNvx/PHrqJ9gOVR0qrJSqWRBme9zGGxVRKV6ZY7BSAtssm6JEIILF85PQUdPVbIu9ozoRM4rpxa2vhGLO876neAGLKcJcljynZyGHtNf+gkbTQVOceQoC81MYQnT+SIgV7GxnPTmJ4oSNDZnyYz8gvEFimRgp/jGlxoxBbKhYdudxWX72ZwXD8zO3D3lejbyRR+xFdLfC8lUtQ4UVg4CU5kfz/RL9p0HIYSI/puDbHZ8RPHz+E52XEOKWKGKQqpeMlMEC76ctbNFgvWjv632KSTvA1sr19mNwupTvFJPoHrBn3G0qPC1/QujAhfJeHwY3ExUN2CsQDmcBSTtMQ3xdl8Kivu8i0rEToOS21/0N0BLFQbxSj6mnWZWPxli2YX4CC7hq/EcL4wBo2/r2rrAQIzZ2vwbRVJq+s3kg613jyX9Btc4Xm2Dy1q2HMX3AdrqVio5bSnqDL2CQdSvQlqIPOLK5YmJUKegJA/vqyyu+YJQpummD45t+124x=="
# }
# response = requests.get(url,headers =headers)
# print(response.text)
# import json
# f = open('Shop.json','r',encoding='utf-8')
# fp = open('shop_id','a',encoding='utf-8')
# for eachline in f:
#     text_json = json.loads(eachline)
#     str_s = text_json['id']+'\n'
#     fp.write(str_s)
#     print(text_json['id'])
# f.close()
# fp.close()

# fp = open('39.89491&116.322056shop_id.txt','r',encoding='utf-8')
# f = open('39.89491&116.322056shop_idq.txt','a',encoding='utf-8')
# id_list = []
# for eachline in fp:
#     id_list.append(eachline)
# print(len(id_list))
# id_list = list(set(id_list))
# print(len(id_list))
# for s in id_list:
#     f.write(s)
# f.close()

