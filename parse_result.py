import json
file=r'batch_shop_demo_full.json'
#新：名字，地址，优惠，电话
with open (file,'r',encoding='utf-8') as f:
     load_dict = json.load(f)
     #print(load_dict)
    
# "name":"鲍喜鲍鱼饭·炖品(广州荔湾店)"
name=load_dict['rst']['name']#名

#"id":"E11022687882350934983",
ID=load_dict['rst']['id']#id

lianjie='https://h5.ele.me/shop/#id='+ID#链接

#"address":"广州市荔湾区小梅大街2号二层123房"
address=load_dict['rst']['address']
city=address[0:3]

#"phone":null
phone=load_dict['rst']['phone']#电话
#优惠
shop_desrc=load_dict['rst']['activities']
youhui=[]
for i in shop_desrc:
    youhui.append(i['description'])
print(youhui)

shop={'商铺名':name,'店铺ID':ID,'地址':address,
      '联系方式':phone,'店铺链接':lianjie,
      '店铺优惠':youhui}
print(shop)
filename='shop_info.json'
json_shop = json.dumps(shop,ensure_ascii=False,indent=4)
with open (filename,'a',encoding='utf-8') as fd:
    fd.write(json_shop)
