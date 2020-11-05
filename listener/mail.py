# -*- coding: utf-8 -*-
# 发送邮箱
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config.index import Config
 
smtpserver = "smtp.qq.com"
smtpport = 465
sender = '815600709@qq.com'
receivers = ['815600709@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
pass_key = Config.__qqMailVerify__
print('pass_key', pass_key)
def sendMail(msg): 
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("帅的一匹", 'utf-8')   # 发送者
    message['To'] =  Header("测试", 'utf-8')        # 接收者
    
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    print('message', message)
    try:
        smtpObj = smtplib.SMTP_SSL(smtpserver, smtpport)
        print('create service')
        smtpObj.login(sender, Config.__qqMailVerify__)
        print('login')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except (smtplib.SMTPException) as e:
        print("Error: 无法发送邮件", e)


