# -*- coding: utf-8 -*-

# 商品名称   商品链接   正确地址    邮箱

## 定时任务

import sched
import time
from datetime import datetime
import urllib3
import re  # 正则表达式，用于匹配字符
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块 
mockData = [
    [
    '测试商品1', 
    'https://github.com/wgh815600709qq?tab=repositories',
    'https://avatars3.githubusercontent.com/u/17962624?s=460&u=9954c9b33250e12247150bc6fe0fea88877c053e&v=4', 
    '815600709@qq.com'
    ]
]
# 初始化sched模块的 scheduler 类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)

# 被周期性调度触发的函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    listener(mockData)
    # schedule.enter(inc, 0, printTime, (inc,)) # 内部重复调用

# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, printTime, (inc,))
    schedule.run()

def listener(data):
    for row in data:
        goods_name = row[0]
        web_url = row[1]
        img_url = row[2]
        email = row[3]
        print(goods_name, web_url, img_url, email)
        http = urllib3.PoolManager()
        response = http.request('GET', url=web_url)
        # page = urllib2.urlopen(web_url)
        if response.status == 200:
            pageContent = response.data
            print('pageContent', pageContent)
            soup =  BeautifulSoup(pageContent)
            img_list = soup.find_all('img')
            flag = bool(False)
            print('img_list', img_list)
            for img in img_list:
                img_nowUrl = img.attrs['src']
                if (img_nowUrl == img_url): # 图片找到了
                    flag = bool(True)
                    print('find the image', img_nowUrl)
            if flag==bool(True):
                print('Nothing Special')
                break
            else:
                print('Something Wrong', img_url)
        else:
            print(response.status)
# 10s 输出一次
main(60)