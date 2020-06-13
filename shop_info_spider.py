import json
import requests


def get_shop_detail(shop_id_list, cookie):
    ls = []
    user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML,' \
                 'like Gecko)Chrome/83.0.4103.61 Mobile Safari/537.36 '
    for shop_id in shop_id_list:
        print(cookie)
        headers = {'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'zh-CN,zh;q=0.9',
                   'cookie': cookie,
                   'referer': 'https://h5.ele.me/shop/',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': user_agent,
                   # x-font-version: bf567591c8124d0bbd5642aaac739edd
                   'x-shard': 'shopid=E11293485602379493858;loc=116.322056,39.89491',
                   'x-ua': 'RenderWay/H5 AppName/wap',
                   'x-uab': "124#qmW8jxEmxG0xAPIhR0c7HeKVVpRFx4SskGO1Me+5ZXguXA0v3UtKPvNmSMx+Zk"
                   "+hswFEEFeDtxEXu2TOmxnkyZJ1gC6xzND3y4WAQ "
                            "/cu0EG2MN81EhwKTIyB1lZ82v5xm7tD2JdopY1PvWzYSrqOtVr6+UABNgRqzVrp/Rb68/SIjvqQWaH7y62ZlMan6KvBIZYLlw"
                            "/2mfWeI8bpgTzo72bX/YDJ67vtQC/plm/IHf"
                            "+ZI8LLgTSo1nIelML267vBIZYLlwYnmfWeIqXpg5Sd1Z2ZlMXng7OBJZEUl5KKmfuUI8Lpg7TVdOxzlbangKC0InYLlBB3neHmCaEJNONNH4qmUdYspycI71Y80/6Tdc/wmayIdrC5SqP2QDEZYCJsWVNjb0z7MFfDF+OSLYWhbPtdL9I8WIwT7QNjDBmmpsm5W7Z+GZCEj0zCGmNvx/PHrqJ9gOVR0qrJSqWRBme9zGGxVRKV6ZY7BSAtssm6JEIILF85PQUdPVbIu9ozoRM4rpxa2vhGLO876neAGLKcJcljynZyGHtNf+gkbTQVOceQoC81MYQnT+SIgV7GxnPTmJ4oSNDZnyYz8gvEFimRgp/jGlxoxBbKhYdudxWX72ZwXD8zO3D3lejbyRR+xFdLfC8lUtQ4UVg4CU5kfz/RL9p0HIYSI/puDbHZ8RPHz+E52XEOKWKGKQqpeMlMEC76ctbNFgvWjv632KSTvA1sr19mNwupTvFJPoHrBn3G0qPC1/QujAhfJeHwY3ExUN2CsQDmcBSTtMQ3xdl8Kivu8i0rEToOS21/0N0BLFQbxSj6mnWZWPxli2YX4CC7hq/EcL4wBo2/r2rrAQIzZ2vwbRVJq+s3kg613jyX9Btc4Xm2Dy1q2HMX3AdrqVio5bSnqDL2CQdSvQlqIPOLK5YmJUKegJA/vqyyu+YJQpummD45t+124x== "
                   }
        url = 'https://h5.ele.me/pizza/shopping/restaurants/' + shop_id + \
              '/batch_shop?extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D'
        try:
            response = requests.get(url, headers=headers)
            print('详情页')
            html_str = response.text
        except Exception:
            print('报错')
        ls.append(html_str)
    return ls


if __name__ == '__main__':
    test_cookie = '__wpkreporterwid_=3d72cc85-f388-43bc-2b38-13ea1199629b; ubt_ssid=sfey2fqjkpel25q84ptsxpm8rwr8rthm_2020-06-11; perf_ssid=y2hktypxz8r2rz63s5w06ie9no86n8s8_2020-06-11; ut_ubt_ssid=nbx8l9f9b4b07kqr7ugs9f7yycn9r1cf_2020-06-11; cna=alNdF9m8MgICAXW1ivMmsc2e; _bl_uid=IeksabyqabF892d3Idgenpsi6CXn; _utrace=133a014a0e2422bd9ff6f77cde57e53d_2020-06-11; t=64f8aa6460cf6a078a44b20a18661759; track_id=1591849854|1a25042eadc71454326c68fb5a25ebb2fab5e792522f873793|955ed194e2a2f068df9627867a113373; USERID=1000081377127; UTUSER=1000081377127; tzyy=0ea3bd83faf3701586a6e1ca12af70f7; l=eBj4RcHRQ9UOegTKBOfZhurza77T9IRfguPzaNbMiOCPOe5p5oCRWZxjBFT9CnGVnsNMR3RILX7BBP8x7P4ZQxv9-e1Sm1u4IdTh.; _samesite_flag_=true; cookie2=147f860202e20dae279acfacdf59a9ec; _tb_token_=fa3e63bbb5635; SID=DAAAAOjZfsdn6gAEAAAAQZ_B6Zy3_rH0SSBzG6bLhnoH2zNXGb5TIsVI; ZDS=1.0|1591867803|CDNiitjz9MqQGdq/5LpQ0+Q98vItLL32sSCnq8SfbkEkADf+6ep0UprGpBR4qV7EnyWu2Q0vmu6V3M+lfMzHTg==; x5check_ele=JJXmecJy89N8zhLn6O4nEnAmWk8eyNcIxGvB%2FFJeBxg%3D; isg=BLOzYm266bsIFqVv81Fyk7KSQrfd6EeqBxlpv2VQD1IJZNMG7bjX-hHyGpKKRJ-i'
    print(get_shop_detail([], test_cookie))
