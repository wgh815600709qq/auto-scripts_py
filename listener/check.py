# -*- coding: utf-8 -*-

# 商品名称   商品链接   正确地址    邮箱

## 定时任务

import sched
import time
from datetime import datetime
import urllib3
import re  # 正则表达式，用于匹配字符
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块 
from mail import sendMail
from config.index import Config
# 初始化sched模块的 scheduler 类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


# 根据excel内容去爬对应的信息，校验并发送邮件
def checkWebSite(data):
    wrong_imgList = []
    http = urllib3.PoolManager(num_pools=100,maxsize=10,block=True,retries=10)
    wrong_imgList.append('腾讯文档在线维护地址:' +  Config.__onlineDocumentUrl__ + ',发现的异常如下：')
    for row in data:
        goods_name = row[0]
        web_url = row[1]
        img_url = row[2]
        email = row[3]
        print(goods_name, web_url, img_url, email)
        response = http.request('GET', url=web_url)
        # page = urllib2.urlopen(web_url)
        if response.status == 200:
            pageContent = response.data
            # print('pageContent', pageContent)
            soup =  BeautifulSoup(pageContent)
            img_list = soup.find_all('img')
            flag = bool(False)
            # print('img_list', img_list)
            for img in img_list:
                img_nowUrl = img.attrs['src']
                if (img_nowUrl == img_url): # 图片找到了
                    flag = bool(True)
                    print('这个图片正常', img_nowUrl)
            if flag==bool(True):
                continue
            else:
                print('图片地址异常', img_url)
                wrong_imgList.append('→商品:['+goods_name+']图片地址异常;')               
        else:
            print(response.status)
    # 汇总发送
    if len(wrong_imgList) > 0:
        print('图片有异常,正在发邮件')
        result = "\n".join(wrong_imgList)
        sendMail(result)
    else:
        print('所有图片都正常, 不发邮件')
    print('连接池数量:', len(http.pools))
# 10s 输出一次
