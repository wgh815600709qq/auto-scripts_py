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
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains # 鼠标悬停
# import requests
# from requests.exceptions import RequestException
# from bs4 import BeautifulSoup 解析html的

## 常量定义
__tencentDocumentLoginUrl__ = 'https://docs.qq.com/desktop'
__onlineDocumentUrl__ = 'https://docs.qq.com/sheet/DUVF5dE9TQ1lXUlZk?tab=BB08J2'
__qqUsername__ = ''
__qqPassword__ = ''
__downloadPath__ = 'C:/Users/Administrator/Downloads/amazonListener.xlsx'


## Part One 检测文件内容
### driver爬腾讯文档流程：登录腾讯文档-> 导出->解析->根据需求通知
### 腾讯文档登录 qq方式(账号/密码)
def login():
    driver.get(__tencentDocumentLoginUrl__)
    time.sleep(3) # 3s静止
    # Iframe嵌套需要控制调整
    driver.switch_to_frame(driver.find_element_by_id('login_frame'))
    # 切换到账密登陆
    driver.find_element_by_id('switcher_plogin').click()
    time.sleep(1) # 等1s
    # 账号密码填入
    driver.find_element_by_id('u').send_keys(__qqUsername__)
    driver.find_element_by_id('p').send_keys(__qqPassword__)
    driver.find_element_by_id('login_button').click()
    time.sleep(5) # 5s后直接访问文档地址
    driver.get(__onlineDocumentUrl__)
    time.sleep(20) # 10s后开始导出，因腾讯文档需要同步
    # 鼠标点击‘更多’图标，此时才有导出的dom结构
    driver.find_element_by_class_name('titlebar-icon-more').click()
    # driver.find_element_by_partial_link_text('本地Excel表格').click()
    time.sleep(100)
## Part Two 定时任务检查文件




## 主线程函数
def main():
    print('process main start')
    print('process main end')


# 登录跳转流程
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    login()