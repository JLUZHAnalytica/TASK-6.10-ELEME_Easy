# coding=utf-8

# @Time : 2020/6/7 21:53
# @Author   : xiaozhen
# @Project -->  File : 测试  -->  demo.py
# @IDE : PyCharm 
# @Desc : 饿了么demo


import json
import time
import threading

import requests


class elm():
    def __init__(self):
        with open('store_information.csv', 'a', encoding='utf-8')as f:
            f.write('商铺名,商铺id,营业状态,省份,城市,平台分类(菜系),地址,经纬度,店铺订单量,联系方式,营业时间,店铺优惠活动,店铺链接,评分,评论数,店铺评分')
        with open('food_information.csv', 'a', encoding='utf-8')as f:
            f.write('商品名,店铺id,商品描述,原价,促销价,商品分类,商品销量,菜单序号,商品评分,图片链接,是否缺货')
        self.cookie = self.get_cookie()
        self.header = {
            'cookie': self.cookie,
            # 'cookie': '__wpkreporterwid_=b3258b36-f10c-4136-207d-b676ba03ba02; ubt_ssid=susro8i20m5aixc7bfwzmmw8fif8wr72_2020-06-05; perf_ssid=qp7eh2ypeomuo0fpgktbi7lqw8ymv12n_2020-06-05; ut_ubt_ssid=k6jsndkpnp5d95ls9ozhlmaao49imf89_2020-06-05; _bl_uid=0Ikd4bwC20vaC886tdCwl8eowhpq; cna=WFYoF2EhCXICAX0qK3QhMpHQ; _utrace=69a7e4de66fb3e2056c0b737d4741915_2020-06-05; track_id=1591366519|fc9bf72d8bc075e9619cfe1cbfaaf6943598230075b3a8e3ba|afe95d3671b0b0be992d7f08c580c4bd; USERID=1230249698; UTUSER=1230249698; tzyy=809009da655e9df79bd2fee877c9adfe; t=de449cc563c1f281dd79db3d36baa05c; munb=2205028799185; ZDS=1.0|1591519863|6dIBOUX0LGosC6PZgZgjFj5l8qRBUqDQeAqPbigKC+imMFU/1/ooiDeUvZ4TLT1xrJPG8lWEVdgdAFdN1BiydQ==; t_eleuc4=id4=0%40BA%2FvuHCrrRj3bd54jv7WG9Zymj40PpqrwicXZA%3D%3D; SID=AwAAAABJVB7i7AAGRgD6NWzPtYpLpMOni32aB2QSMaaGM5M9rVMT8-b1; x5check_ele=I7JAdQdQg6RSUn1FqipWQzLVbO6O0F%2B%2BMyVhQoy%2Bn%2Bw%3D; l=eBxwegFVQVGlJ8u-BOfZlurza779kIRCguPzaNbMiOCP_7X9rdXdWZvKCYtpCnGVnswWq3oNzJ6TBRLKdy4EQxv9-e9bMdFs3dJf.; isg=BFRUBwFZ9tuvWGKRz1JPp8TLJZLGrXiXun-6P-414F9i2fQjFr1IJwpf3dfBIbDv',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
        }

    def get_shop_list(self, latitude, longitude, index=0):
        '''获取商铺列表'''
        url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?'
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'offset': index,
            'limit': '20',
            'extras[]': 'activities',
            'extras[]': 'tags',
            'extra_filters': 'home',
            'terminal': 'h5',
        }
        try:
            response = requests.get(url, params=params, headers=self.header)
            print('店铺页')
            data = json.loads(response.text)
            self.parse_shop_list(data)
            has_next = data['has_next']
            index += 1
            if has_next:
                self.get_shop_list(latitude, longitude, index)
            else:
                print('已经采集完毕')
        except:
            if '请登录' in response.text:
                print('报错')
                self.cookie = self.get_cookie()
            self.get_shop_list(latitude, longitude, index)

    def get_shop_detail(self, shop_id):
        url = 'https://h5.ele.me/pizza/shopping/restaurants/%s/batch_shop?' % (shop_id)
        try:
            response = requests.get(url, headers=self.header)
            print('详情页')
            self.parse_shop_datil(response.text)
        except:
            if '请登录' in response.text:
                print('报错')
                self.cookie = self.get_cookie()
            self.get_shop_detail(shop_id)

    def get_cookie(self):
        url = 'http://127.0.0.1:5000/api/'
        cookie = requests.get(url).text
        return cookie

    def parse_shop_list(self, data):
        print('店铺开始解析')
        items = data['items']
        for i in range(len(items)):
            shop_id = items[i]['restaurant']['id']  # 店铺id
            shop_business_info = eval(items[i]['restaurant']['business_info'])
            self.shop_description = ''  # 店铺优惠
            for j in range(len(shop_business_info)):
                self.shop_description += items[i]['restaurant']['activities'][j]['description'] + ';'
            self.shop_pickup_scheme = shop_business_info['pickup_scheme']  # 店铺链接

            self.get_shop_detail(shop_id)

    def parse_shop_datil(self, data):
        print('详情开始解析')
        data = json.loads(data)
        # 店铺信息
        rst = data['rst']
        shop_name = rst['name']  # 商铺名
        shop_id = rst['id']  # 商铺id
        shop_status = rst['status']  # 营业状态
        shop_pro = '北京市'  # 省份
        shop_city = '北京市'  # 城市
        shop_platform = ''  # 平台分类
        for i in range(len(rst['flavors'])):
            shop_platform += rst['flavors'][i]['name'] + '/'
        shop_address = rst['address']  # 地址
        shop_longitude = rst['longitude']  # 经度
        shop_latitude = rst['latitude']  # 纬度
        shop_ddl = eval(rst['business_info'])['recent_order_num_display']  # 订单量
        shop_phone = rst['phone']  # 联系方式
        shop_opening_hours = rst['opening_hours']  # 营业时间
        shop_rating = rst['rating']  # 评分  店铺评分
        shop_rating_count = rst['rating_count']  # 评论数
        print('')
        item = '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(shop_name, shop_id, shop_status, shop_pro,
                                                                          shop_city, shop_platform, shop_address,
                                                                          shop_longitude + '|' + shop_latitude,
                                                                          shop_ddl, shop_phone, shop_opening_hours,
                                                                          self.shop_description,
                                                                          self.shop_pickup_scheme, shop_rating,
                                                                          shop_rating_count, shop_rating)
        with open('store_information.csv', 'a', encoding='utf-8')as f:
            f.write(item)
        print('店铺保存成功')

        # 菜品信息
        menu = data['menu']
        for i in menu:
            commodity = menu[i]['foods']
            for j in commodity:
                commodity_name = commodity['name']  # 商品名
                commodity_id = commodity['restaurant_id']  # 店铺id
                commodity_description = commodity['description']  # 商品描述
                commodity_origin_price = commodity['origin_price']  # 商品原价
                commodity_price = commodity['price']  # 商品促销价
                commodity_icon_name = commodity['specfoods'][0]['activity']['icon_name']  # 商品分类
                commodity_month_sales = commodity['month_sales']  # 商品销量
                commodity_vfood_id = commodity['vfood_id']  # 商品序号
                commodity_rating = commodity['rating']  # 商品评分
                commodity_photo = commodity['photo']  # 图片链接
                commodity_sold_out = commodity['sold_out']  # 是否缺货
                item = '{},{},{},{},{},{},{},{},{},{},{}\n'.format(commodity_name, commodity_id, commodity_description,
                                                                   commodity_origin_price, commodity_price,
                                                                   commodity_icon_name, commodity_month_sales,
                                                                   commodity_vfood_id, commodity_rating,
                                                                   commodity_photo,
                                                                   commodity_sold_out)
                with open('food_information.csv', 'a', encoding='utf-8')as f:
                    f.write(item)
                print('菜品保存成功')

    def run(self, latitude, longitude):
        self.get_shop_list(latitude, longitude)


def main():
    spyder = elm()
    with open('jw.txt', 'r', encoding='utf-8')as f:
        jwd = list(map(lambda x: x.strip().split(','), f.readlines()))
    for i in jwd:
        spyder.run(i[1], i[0])
        jwd.pop(i)
        with open('jw.txt', 'w', encoding='utf-8')as f:
            for j in jwd:
                f.write('{},{}\n'.format(j[0], j[1]))


if __name__ == '__main__':
    main()
