#!/usr/bin/python 
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
yzj_username = 'xxx'
yzj_password = 'xxx'
url = 'http://crp.kingdee.com'
driver = webdriver.Chrome()  
driver.get(url)          
time.sleep(10)
driver.find_element_by_id('email').send_keys(yzj_username)
driver.find_element_by_id('password').send_keys(yzj_password)
time.sleep(3)
driver.find_element_by_id('authBtn').click()
time.sleep(10)
driver.find_element_by_id("my").click()  
time.sleep(3)
driver.find_elements_by_class_name('to-start-metro-btn')[5].click() # 30构建
time.sleep(3)
driver.find_element_by_id('startMetroBtn').click()
time.sleep(60 * 20) # 20分钟启动 190
driver.find_elements_by_class_name('to-start-metro-btn')[4].click() # 190构建
time.sleep(3)
driver.find_element_by_id('startMetroBtn').click()
time.sleep(3)
driver.close()
