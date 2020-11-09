# -*- coding: utf-8 -*-
from selenium import webdriver
from tc_doc_download import login, download;
from parse_xlsx import parseXlsx;
from check import checkWebSite
import mail
import time
from selenium.webdriver.support.ui import WebDriverWait
import asyncio
from datetime import datetime
import sched
schedule = sched.scheduler(time.time, time.sleep)
inc=60*60*12 # 间隔检查流程的时间 60 * 5 [60 * 60 * 12]

def main(wait, driver):
    login(wait, driver, parse)

def parse():
    xlsxData = parseXlsx()
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数、函数参数。
    # 给该触发函数的参数（tuple形式)
    schedule.enter(5, 0, loop, (xlsxData,)) # 5s执行
    schedule.run()

# 被周期性调度触发的函数
def loop(data):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    checkWebSite(data)
    print('检查完毕，'+ str(inc) +'s后尝试进入下一个循环')
    time.sleep(inc)
    try:
        print('开始下一轮检查')
        driver.refresh()
        print('driver刷新了')
        time.sleep(15) # 休息会
        print('开始检查任务')
        schedule.enter(inc, 0, download, (driver, parse)) 
        # download(driver, parse)
        # main(wait, driver)
    except Exception as e:
        print(e)


# 登录跳转流程
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    main(wait, driver)

