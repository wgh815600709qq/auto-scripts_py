# -*- coding: utf-8 -*-
from selenium import webdriver
from tc_doc_download import login;
from parse_xlsx import parseXlsx;
from listeners import addListener
import mail
import time
from selenium.webdriver.support.ui import WebDriverWait


# 登录跳转流程
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    login(wait, driver)
    time.sleep(5)
    xlsxData = parseXlsx()
    addListener(60, xlsxData)
