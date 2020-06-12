# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import json


# 加载文件中保存的cookie
def load_cookie(web):
    with open("output/temp/cookie_get.json") as fd:
        cookies = json.loads(fd.read())
    for cookie in cookies:
        web.add_cookie(cookie)

def login():
    '''启动chrom进行登录'''
    options = webdriver.ChromeOptions()
#     '''设置浏览器为手机显示'''
    mobile_emulation = {"deviceName":"Galaxy S5"}
    capabilities = DesiredCapabilities.CHROME
    capabilities['loggingPrefs'] = { 'browser':'ALL' }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    #修改windows.navigator.webdriver，防机器人识别机制，selenium自动登陆判别机制desired_capabilities=capabilities,
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # drive = webdriver.Chrome(executable_path='E:\Google\Chrome\Application\chromedriver.exe',options=options)
    drive = webdriver.Chrome(options=options) # bin目录中放置driver
    #CDP执行JavaScript 代码  重定义windows.navigator.webdriver的值
    drive.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    url = 'https://h5.ele.me/'
    drive.implicitly_wait(10)
    drive.get(url)

    # 实现登陆，请务必先运行get_bookie.py
    load_cookie(drive) #加载必须在打开页面之后 
    drive.refresh() #刷新后发现正常登陆

    my = drive.find_element_by_xpath('//*[@ubt-click="105141"]')
    my.click()
    time.sleep(1)
    signup_login = drive.find_element_by_xpath('//*[@class="profile-1_mtk"]')
    signup_login.click()
    input('请手动登陆(登陆完成后按任意键继续)...')
    drive.maximize_window() #窗口最大化
    time.sleep(2)
    return drive

def choose(web):
    '''进行选择城市，地点，筛选'''
    web.execute_script("document.getElementsByClassName('index-2uW_v_0')[0].click()")
    web.execute_script("document.getElementsByClassName('index-21dnA_0')[0].click()")
    sleep(1)
    Input = web.find_element_by_xpath('//*[@placeholder="输入城市名或者拼音"]')
    Input.click()
    city = str(input('请输入城市名:'))
    Input.send_keys(city)
    citys = web.find_elements_by_xpath('//*[@class="city-5r26m_0"]')
    for i in citys:
        if citys.index(i) > 5:
            break
        print(citys.index(i) + 1, '：' + i.text.replace('\n', ' '))
    num = 0
    while num < 1 or num > 5:
        num = int(input('请选择地址：'))
        if num < 1 or num > 5:
            print('输入错误！')
    citys[num - 1].click()
    sleep(1)
    address = web.find_element_by_xpath('//*[@placeholder="请输入地址"]')
    address.click()
    address_describe = str(input('请输入详细地址:'))
    address.send_keys(address_describe)
    sleep(1)
    address_describe = web.find_elements_by_xpath('//*[@class="AddressCell-2WCnC_0"]')
    address_list = []
    for i in address_describe:
        if address_describe.index(i) > 5:
            break
        address_list.append(i.text.replace('\n', ' '))
        print(address_describe.index(i) + 1, '：' + i.text.replace('\n', ' '))
    num = 0
    while num < 1 or num > 6:
        num = int(input('请选择地址：'))
        if num < 1 or num > 6:
            print('输入错误！')
    address_describe[num - 1].click()
    print('您选择的地址为：', address_list[num - 1])
    web.execute_script("document.getElementsByClassName('filter-nav-more')[0].click()")
    for i in range(1, 4):
        title = web.find_element_by_xpath(
            '/html/body/div/div[1]/div[6]/aside/section[2]/div[1]/dl[{}]/dt'.format(i)).text
        print(title + '\n')
        choose = web.find_element_by_xpath(
            '/html/body/div/div[1]/div[6]/aside/section[2]/div[1]/dl[{}]/dd'.format(i)).text.split('\n')
        for j in range(len(choose)):
            print(j + 1, '：' + choose[j])
        if i == 1:
            while True:
                num = int(input('请选择(按下:-1退出多选)：'))
                if num == -1:
                    break
                web.execute_script("document.getElementsByClassName('morefilter-3GXUR_0')[{}].click()".format(num - 1))
        elif i == 2:
            num = int(input('请选择：'))
            web.execute_script("document.getElementsByClassName('morefilter-3GXUR_0')[{}].click()".format(num - 1 + 7))
        else:
            num = int(input('请选择：'))
            web.execute_script("document.getElementsByClassName('morefilter-3GXUR_0')[{}].click()".format(num - 1 + 9))
            web.execute_script("document.getElementsByClassName('morefilter-16ilq_0 morefilter-2Dfps_0')[0].click()")

login()