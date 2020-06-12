from selenium import webdriver
import json

web = webdriver.Chrome()
web.get('https://h5.ele.me/')
input("请手动登录后按回车继续...")
with open("output/temp/cookie_get.json", 'w') as fd:
    fd.write(json.dumps(web.get_cookies(), indent=4))

print("cookie保存成功")
