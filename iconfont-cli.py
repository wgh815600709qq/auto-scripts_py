#coding=utf-8
# iconfont官网的图标替换后，自动构建 脚本
# 1、iconfont官网下载图标
# 2、本地bos分支拉取新分支
# 3、文件替换、git提交
# 4、合并分支
# 5、交付平台构建


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By # 可能无相关引用了
from selenium.webdriver.support.expected_conditions import presence_of_element_located # 可能无相关引用了
import time
from shutil import copyfile
import os
import subprocess
import zipfile
import shutil

# 常量、变量
iconfont_url = 'https://www.iconfont.cn' 
bos_path = 'D:/V7/Main/bos-dev-platform'
bos_font_cli_path = 'D:/V7/Main/bos-dev-platform/font-replace-cli.js'
bos_dir_download_path = 'D:\\V7\\Main\\bos-dev-platform\\download.zip'
download_path = 'C:\Users\Administrator\Downloads\download.zip'
git_username = 'xxx'
git_password = 'xxx'
build_url = 'http://crp.kingdee.com'
font_path = 'D:/V7/Main/bos-dev-platform/static/font'
yzj_username = 'xxx'
yzj_password = 'xxx'


# 先清除下载目录
if (os.path.exists(download_path)):
  os.remove(download_path)

# bos分支切换新分支
def check_branch():
    try:
      os.chdir(bos_path)        #转到工程路径下
    finally:
        subprocess.call(['git', 'checkout', 'dev'])
        subprocess.call(['git', 'branch', '-D', 'feat/fontReplace'])
        subprocess.call(['git', 'pull'])
        subprocess.call(['git', 'checkout', '-b', 'feat/fontReplace'])
        print('[checkout_branch]: feat/fontReplace')

check_branch()

# 下载压缩包
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(iconfont_url)
    time.sleep(10)
    driver.find_element_by_class_name('signin').click()
    time.sleep(1)
    driver.find_element_by_class_name('github').click()
    time.sleep(1)
    driver.find_element_by_id('login_field').send_keys(git_username)
    driver.find_element_by_id('password').send_keys(git_password)
    time.sleep(5)
    driver.find_element_by_css_selector("input[type='submit']").click()
    print('download iconfont by login github')
    time.sleep(10)
    driver.execute_script("document.querySelectorAll('.nav-item')[2].children[1].children[2].children[0].click()")
    time.sleep(3)
    driver.execute_script("document.querySelectorAll('.nav-container')[1].children[1].children[0].click()")
    time.sleep(3)
    driver.execute_script("document.querySelectorAll('.project-manage-bar')[0].children[2].click()")
    time.sleep(3)
    driver.close()
    print('get the download.zip')
# 拷贝zip包到bos根目录
os.chdir(bos_path)
copyfile(download_path, bos_dir_download_path)
time.sleep(10)
print('[cooy zip] finish')

# 解压文件到decompress文件夹
z = zipfile.ZipFile('download.zip')
z.extractall(path='./decompress')
z.close()
print('[decompress zip] finish')

# 删除zip包
os.remove(bos_dir_download_path)
time.sleep(3)

# 删除原bos的font文件夹
shutil.rmtree(font_path)
print('[delete pre font dir] finish')

# 将解压的文件拷贝过去
_fileName = os.listdir(bos_path + '/decompress')[0]
source_path = bos_path + '/decompress/' + _fileName
shutil.copytree(source_path, font_path)
print('[replace font dir] finish')

# 重命名
os.rename(font_path + '/demo_index.html', font_path + '/fontclass.html')
print('[rename fontclass.html] finish.')

# 删除解压文件
shutil.rmtree(bos_path + '/decompress')
print('[delete decompress dir] finish.')

# git 提交
def git_commit():
  subprocess.call(['git', 'add', '.'])
  subprocess.call(['git', 'commit', '-m', 'python script:font replace'])
  subprocess.call(['git', 'push', '--set-upstream', 'origin', 'feat/fontReplace']) # git push --set-upstream origin feat/fontReplace
print('[git_commit] finish')
git_commit()


def git_merge():
  subprocess.call(['git', 'checkout', 'dev'])
  subprocess.call(['git', 'merge', 'feat/fontReplace'])
  subprocess.call(['git', 'push', '-u', 'origin', 'dev']) # git push --set-upstream origin feat/fontReplace
  print('[git_merge] finish')
  subprocess.call(['git', 'branch', '-D', 'feat/fontReplace'])
git_merge()

# 构建脚本
with webdriver.Chrome() as driver:
    driver = webdriver.Chrome()
    driver.get(build_url)          
    time.sleep(10)
    driver.find_element_by_id('email').send_keys(yzj_username)
    driver.find_element_by_id('password').send_keys(yzj_password)
    time.sleep(10)
    driver.find_element_by_id('authBtn').click()
    time.sleep(10)
    driver.find_element_by_id("my").click()  
    time.sleep(3)
    driver.find_elements_by_class_name('to-start-metro-btn')[5].click() # 30构建
    time.sleep(3)
    driver.find_element_by_id('startMetroBtn').click()
    time.sleep(3)
    driver.close()
    print('[start to build]: 30')


# js脚本遇到解析问题
# def get_js():
#   f = io.open(bos_font_cli_path, encoding='utf-8')
#   line = f.readline()
#   htmlstr = ''
#   while line:
#     htmlstr = htmlstr + line
#     line = f.readline()
#   return htmlstr
# strs = get_js()
# ctx = execjs.compile(strs)
# ctx.call('py_start')
# print('font replace finish')
