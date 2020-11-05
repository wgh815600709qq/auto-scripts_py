# -*- coding: utf-8 -*-

# 亚马逊产品监控系统

## 旨在能实时监控产品的图片变化
    ###  准备工具
        ####   vpn翻墙服务器
        ####  driver运行环境


## 设计思路：

    ###   I、一个线上的文档【备选腾讯文档】（xls）维护需要监控的产品链接、 图片链接;

    ###   II、文档内容检测变更（30min/f）;

    ###   III、队列检查产品变更 (10min/f);

    ###   IV、 通知邮件预警。


## 库引入
import time
from config.index import Config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains # 鼠标悬停
from selenium.webdriver.support import expected_conditions # 尝试
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
# import requests
# from requests.exceptions import RequestException
# from bs4 import BeautifulSoup 解析html的

__config__ = Config()


## Part One 检测文件内容
### driver爬腾讯文档流程：登录腾讯文档-> 导出->解析->根据需求通知
### 腾讯文档登录 qq方式(账号/密码) 并下载对应的excel
def login(wait, driver):
    driver.get(__config__.__tencentDocumentLoginUrl__)
    time.sleep(3) # 3s静止
    # Iframe嵌套需要控制调整
    driver.switch_to_frame(driver.find_element_by_id('login_frame'))
    # 切换到账密登陆
    driver.find_element_by_id('switcher_plogin').click()
    time.sleep(1) # 等1s
    # 账号密码填入
    driver.find_element_by_id('u').send_keys(__config__.__qqUsername__)
    driver.find_element_by_id('p').send_keys(__config__.__qqPassword__)
    driver.find_element_by_id('login_button').click()
    time.sleep(3) # 3s后直接访问文档地址
    driver.get(__config__.__onlineDocumentUrl__)
    time.sleep(10) # 10s后开始导出，因腾讯文档需要同步
    # 鼠标点击‘更多’图标，此时才有导出的dom结构
    driver.find_element_by_class_name('titlebar-icon-more').click()
    time.sleep(1)
    lis=driver.find_elements_by_class_name('dui-menu-item')
    for item in lis:
        if item.text == '导出为':
            ActionChains(driver).move_to_element(item).perform()
            # export_excel_xPath='/html/body/div[28]/ul/div[1]/li'
            export_excel_xPath='//li[contains(text(), ".xlsx")]'
            driver.find_element_by_xpath(export_excel_xPath).click()
            break

# 登录跳转流程
# with webdriver.Chrome() as driver:
#     wait = WebDriverWait(driver, 10)
#     login(wait)