import json

import requests
from shop_info_spider import get_phone_number


def pares(load_dict_list, filename):
    res = []
    for load_dict in load_dict_list:
        load_dict = json.loads(load_dict)
        name = load_dict['rst']['name']  # 名
        ID = load_dict['rst']['id']  # id
        lianjie = 'https://h5.ele.me/shop/#id=' + ID  # 链接
        address = load_dict['rst']['address']  # 地址
        # phone=load_dict['rst']['phone']#电话
        shop_desrc = load_dict['rst']['activities']  # 优惠
        youhui = []
        for i in shop_desrc:
            youhui.append(i['description'])
        phone_num = get_phone_number('https://h5.ele.me/restapi/giraffe/restaurant/phone?shopId={}'.format(ID))
        shop = {'商铺名': name, '店铺ID': ID, '地址': address,
                '联系方式': phone_num, '店铺链接': lianjie,
                '店铺优惠': youhui}
        # print(shop)
        # filename = 'output/res/shop_info.json'
        res.append(shop)
    with open(filename, 'w', encoding='utf-8') as fd:
        fd.write(json.dumps(res, ensure_ascii=False, indent=4))
    print("结果已输出至{}".format(filename))
    if input("是否需要显示(y/n):") == 'y':
        print(json.dumps(res, ensure_ascii=False, indent=4))



# 单元测试
if __name__ == '__main__':
    file = 'old_research/demo_data/batch_shop_demo_full.json'
    # 新：名字，地址，优惠，电话
    with open(file, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
        # print(load_dict)
    pares(load_dict)
