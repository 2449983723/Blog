#coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
import sys
sys.path.append('../')
from testurllib.test.xiaohua import gettiquneirong

mail_info = {
    "from": "2449983723@qq.com",
    "to": "1352211034@qq.com",
    "hostname": "smtp.qq.com",
    "username": "2449983723@qq.com",
    "password": "xiaonian@hbutrj1b",
    "mail_subject": "轻松一刻！",
    "mail_text": "",
    "mail_encoding": "utf-8"
}

if __name__ == '__main__':
    #这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    
    content_head = ''
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])
    mail_info["mail_text"] = content_head + gettiquneirong(5000, 10)
    msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    print msg.as_string()
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

    smtp.quit()