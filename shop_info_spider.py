import json
import requests
from get_cookie import cookie_to_str


def get_phone_number(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
        'Cookie': cookie_to_str()}
    response = requests.get(url, headers=headers)
    phone = json.loads(response.text)
    phone_num = phone[0]['numbers']
    return phone_num

def get_shop_detail(shop_id_list):
    ls = []
    user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML,' \
                 'like Gecko)Chrome/83.0.4103.61 Mobile Safari/537.36 '
    
    # print(cookiestr)
    for shop_id in shop_id_list:
        headers = {'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'zh-CN,zh;q=0.9',
                   'cookie': cookie_to_str(),
                   'referer': 'https://h5.ele.me/shop/',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': user_agent,
                   # x-font-version: bf567591c8124d0bbd5642aaac739edd
                   'x-shard': 'shopid=E11293485602379493858;loc=116.322056,39.89491',
                   'x-ua': 'RenderWay/H5 AppName/wap',
                   'x-uab': "124#9hKOaJEvxG0xAqVXR0c7HeKVVpRFx4SskGO1Me+5ZXguXA0v3UtKPvNmSMx+Zk+hswFEEFeDtxEXu2TOmxnkyZRJs66xzND3y4WAQ/cu0EG2MNPRvWs/AvpDfqK0Y22MiHrU4MlM2ZMElh+njdUEG/MOvuI19PEY3A3eoq/Ruwi+Gzx08kUzInYLlTYIm4WZIqXLgTzd1Z2ebUL2gKvm/UwT5wiJm4afI8LpgTG41nIelUX2g7vtIZ/Llm/Jm4WZIqXLg5Sd1Z2ZlMLng7OBInYLlwYnmfWxJMbBgmUd1qyelULnm6VDLDuLUTY2USAeIqXpM0jeg9USvwi5uEqNRldbhEscJwSaNEGADpRZeJx+c8LZ1+sNKUYVHD3s4PjnSsTLPcas33k4LB7ejT46xD4XbmWruwuk4S8f58TKJs41sMrAAqauYJOndVD/cp2OeNOrt0U8nbr4Vtuy/o1B5bmzXMghBcLeUpf/usfwaUgJwq2QE0O4Q5rxTa6f70PVyi4FqbP7CXc6awwrla+bx/EDNseqo6SBndUS8WUbzcEhFFOKUqPBwZoqAP0peP9wpblP0MFAJqUZ5rvH2/1TfFSzb6ijjeZX/1Afjec4vTKjXpWan469foW8th/oc2k9ny+7a9yOmpZP2aKKzRWjAu2MnpOGwS76zXB5n1TnNdnc7NDyDDBesaXJ5icGwZyJrjDlMhs6vTMxZv3QvdKj3ihmUubN83W5qMbaD0HPDS/k1qlnI/X5Ck6e4Ue7l/869w6b4+YtqPUT+PL0Oke729sm5K83VizMwSitzO1D2E71mxIdRQPiUTLkBctNf0hzB1Tu9dPTeDskkuX7lobznoQUqXcAqQTwL+BVN3U2baCV8YAdmTjSp6damztypj0ZFicQgx=="
                   }
        url = 'https://h5.ele.me/pizza/shopping/restaurants/' + shop_id + \
              '/batch_shop?extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D'
        try:
            response = requests.get(url, headers=headers)
            print('详情页 {} 爬取成功...'.format(shop_id_list.index(shop_id)+1))
            html_str = response.text
        except Exception:
            print('详情页 {} 爬取失败！！'.format(shop_id_list.index(shop_id)+1))
        ls.append(html_str)
    return ls


if __name__ == '__main__':
    test_cookie = '__wpkreporterwid_=3d72cc85-f388-43bc-2b38-13ea1199629b; ubt_ssid=sfey2fqjkpel25q84ptsxpm8rwr8rthm_2020-06-11; perf_ssid=y2hktypxz8r2rz63s5w06ie9no86n8s8_2020-06-11; ut_ubt_ssid=nbx8l9f9b4b07kqr7ugs9f7yycn9r1cf_2020-06-11; cna=alNdF9m8MgICAXW1ivMmsc2e; _bl_uid=IeksabyqabF892d3Idgenpsi6CXn; _utrace=133a014a0e2422bd9ff6f77cde57e53d_2020-06-11; t=64f8aa6460cf6a078a44b20a18661759; track_id=1591849854|1a25042eadc71454326c68fb5a25ebb2fab5e792522f873793|955ed194e2a2f068df9627867a113373; USERID=1000081377127; UTUSER=1000081377127; tzyy=0ea3bd83faf3701586a6e1ca12af70f7; l=eBj4RcHRQ9UOegTKBOfZhurza77T9IRfguPzaNbMiOCPOe5p5oCRWZxjBFT9CnGVnsNMR3RILX7BBP8x7P4ZQxv9-e1Sm1u4IdTh.; _samesite_flag_=true; cookie2=147f860202e20dae279acfacdf59a9ec; _tb_token_=fa3e63bbb5635; SID=DAAAAOjZfsdn6gAEAAAAQZ_B6Zy3_rH0SSBzG6bLhnoH2zNXGb5TIsVI; ZDS=1.0|1591867803|CDNiitjz9MqQGdq/5LpQ0+Q98vItLL32sSCnq8SfbkEkADf+6ep0UprGpBR4qV7EnyWu2Q0vmu6V3M+lfMzHTg==; x5check_ele=JJXmecJy89N8zhLn6O4nEnAmWk8eyNcIxGvB%2FFJeBxg%3D; isg=BLOzYm266bsIFqVv81Fyk7KSQrfd6EeqBxlpv2VQD1IJZNMG7bjX-hHyGpKKRJ-i'
    print(get_shop_detail([], test_cookie))
