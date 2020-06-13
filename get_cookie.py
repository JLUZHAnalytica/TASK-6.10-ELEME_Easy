from selenium import webdriver
import json

def cookie_to_str():
    with open('output/temp/cookie_get.json','r',encoding='utf-8') as f:
        listCookies=json.loads(f.read())
    cookie = [item["name"] + "=" + item["value"] for item in listCookies]
    cookiestr = '; '.join(item for item in cookie)
    return cookiestr

def cookie_to_file():
    web = webdriver.Chrome()
    web.get('https://h5.ele.me/')
    input("请手动登录后按回车继续...")
    with open("output/temp/cookie_get.json", 'w') as fd:
        fd.write(json.dumps(web.get_cookies(), indent=4))
    print("cookie保存成功")


# get_cookies()
