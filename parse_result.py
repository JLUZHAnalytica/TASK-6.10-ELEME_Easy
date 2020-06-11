import json

def pares(load_dict):
    name=load_dict['rst']['name']#名
    ID=load_dict['rst']['id']#id
    lianjie='https://h5.ele.me/shop/#id='+ID#链接
    address=load_dict['rst']['address']#地址
    #phone=load_dict['rst']['phone']#电话
    shop_desrc=load_dict['rst']['activities'] #优惠
    youhui=[]
    for i in shop_desrc:
        youhui.append(i['description'])
    phone_num = phonenumber(url,headers)
    shop={'商铺名':name,'店铺ID':ID,'地址':address,
        '联系方式':phone_num,'店铺链接':lianjie,
        '店铺优惠':youhui}
    print(shop)
    filename='output/res/shop_info.json'
    json_shop = json.dumps(shop,ensure_ascii=False,indent=4)
    with open (filename,'a',encoding='utf-8') as fd:
        fd.write(json_shop)
        
import requests

def phonenumber(url,headers):
    response = requests.get(url, headers=headers)
    with open('phone.josn','w',encoding='utf-8') as f:
        f.write(response.text)
    with open('phone.json','r',encoding='utf-8') as f:
        phone=json.load(f)
        phone_num=phone[0]['numbers']
    return phone_num

# 单元测试
url='https://h5.ele.me/restapi/giraffe/restaurant/phone?shopId=E5911365526736648620'
headers = {
    "User-Agent":'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
    'Cookie':'__wpkreporterwid_=e75cba11-e4dd-45f4-266f-070d385cdc68; ubt_ssid=gciqxpu97s1chtkx380h1orps05pmu2x_2020-06-07; perf_ssid=n65wfktgu54wvzhv70h4i4gs4465kxsd_2020-06-07; ut_ubt_ssid=kn2pvboj1rmh5z2u6wsi7b9p3nlulo56_2020-06-07; cna=tSMTF2ohL3kCAXjlr5Ts1wnj; _bl_uid=17ktLbn84nhsa467Ub9hm9XdO3a9; _utrace=fb5297c3cbd37e1e045511a817eea439_2020-06-07; t=1c79c845ba615cc0e37f39f9970caa5f; munb=2206068010646; UTUSER=5407314634; tzyy=a7ffd12f77ac88f98f4f4d473bd536c3; UM_distinctid=1728e97f0223b7-0822275439ca7-f7d1d38-144000-1728e97f02333b; track_id=1591535088|7aa12c09aaa08889ea310832bee468ebb741c1f73807c135cb|a764c2088f2f6d3c1227f19184983e16; USERID=5407314634; ZDS=1.0|1591539025|0y1iH8kgbkkdmHiyItunsm3cULpzTVrjJDn9lhlvjdiaKXk2iqJCHRP0BXKPcbRjdcg0raO7GEWOY/327pCFHg==; t_eleuc4=id4=0%40BA%2FvuHCrrRtVoUZvsz1lgA6nBRSM7Ec5xGX28A%3D%3D; SID=AwAAAAFCTRLK7AAG0AAuRQX3CqfrpRDTvFiCfDWVd2pKp5LBIkn-Htcc; x5check_ele=gsiqy0Gse6EJh%2FQju67bm2vgDrOyjiWVpq9Sv2vgRHo%3D; pizza7567632f76332f72=5xMqRQuOWng_3Lh8jjs5aKCRFGbAATlaXIGR6iLSoFUlxnxbv--phXYPZbbOKr2j; l=eBO_vjteQVjo07tvBO5ahurza77toIdXfsPzaNbMiInca6OhgFw2JOQDcAfkzdtjgtfb_etPOzL1BR32-DzU-x6sZYyG6i7f2xJwj; isg=BJKSWR9hGMwCHWSNE8iV5vai41h0o5Y9OF5cFlzrp8WfbzZpRDKrTFDJ28vTHw7V'}
file='old_research/demo_data/batch_shop_demo_full.json'
#新：名字，地址，优惠，电话
with open (file,'r',encoding='utf-8') as f:
     load_dict = json.load(f)
     #print(load_dict)
pares(load_dict)