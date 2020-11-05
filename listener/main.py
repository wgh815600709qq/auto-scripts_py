# -*- coding: utf-8 -*-
from selenium import webdriver
from tc_doc_download import login;
from parse_xlsx import parseXlsx;
from listeners import addListener
import mail
import time
from selenium.webdriver.support.ui import WebDriverWait
import asyncio


# def callbackFun(future):
    # result = future.result()

def main(wait, driver):
    login(wait, driver, parse)

def parse():
    xlsxData = parseXlsx()
    addListener(60, xlsxData)


# 登录跳转流程
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    main(wait, driver)

