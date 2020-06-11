import json


def pares(load_dict):
    name=load_dict['rst']['name']#名
    ID=load_dict['rst']['id']#id
    lianjie='https://h5.ele.me/shop/#id='+ID#链接
    address=load_dict['rst']['address']#地址
    phone=load_dict['rst']['phone']#电话
    shop_desrc=load_dict['rst']['activities'] #优惠
    youhui=[]
    for i in shop_desrc:
        youhui.append(i['description'])
    shop={'商铺名':name,'店铺ID':ID,'地址':address,
        '联系方式':phone,'店铺链接':lianjie,
        '店铺优惠':youhui}
    print(shop)
    filename='output/res/shop_info.json'
    json_shop = json.dumps(shop,ensure_ascii=False,indent=4)
    with open (filename,'w',encoding='utf-8') as fd:
        fd.write(json_shop)



# 单元测试
file='old_research/demo_data/batch_shop_demo_full.json'
#新：名字，地址，优惠，电话
with open (file,'r',encoding='utf-8') as f:
     load_dict = json.load(f)
     #print(load_dict)
pares(load_dict)