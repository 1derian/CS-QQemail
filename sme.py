# Author : derian
import sys

import smtplib  # smtplib发送邮件
from email.mime.text import MIMEText  # 构造文本内容
from email.header import Header  # 构造标题内容


def post_email(ip, username, computer_name, arch):
    # 设置服务器地址
    mail_host = "smtp.qq.com"
    # 设置服务器端口
    mail_port = 465

    # QQ邮件登录账号
    mail_user = "27xxxx"
    # QQ邮箱第三方授权码
    mail_pass = "pldcxxxxdcge"

    # 初始化发送方账号
    sender = "27xxxx@qq.com"
    # 初始化接收方账号
    receivers = "27xxxx@qq.com"
    # 构造文本对象，三个参数：文本内容，设置文本格式,设置编码
    data = f"""上线主机IP:{ip}
上线主机用户名:{username}
上线主机计算机名:{computer_name}
上线主机架构:{arch}
"""

    message = MIMEText(data, "plain", "utf-8")
    # 文本对象 添加 发送者
    message["From"] = sender
    # 文本对象 添加 接收者
    message["To"] = receivers
    # 文本对象 添加 标题
    message["Subject"] = Header("至风一样男子的邮件")

    # 创建 SMTP 对象，连接目标服务器
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    # 自己账号登录
    smtpObj.login(mail_user, mail_pass)
    # 发送邮件到目标地址  注意：信息由MTMEText对象 转为 字符串对象
    smtpObj.sendmail(sender, receivers, message.as_string())
    # 结束 SMTP 对象
    smtpObj.quit()


if __name__ == '__main__':
    ip = sys.argv[1]
    username = sys.argv[2]
    computer_name = sys.argv[3]
    arch = sys.argv[4]
    post_email(ip, username, computer_name, arch)
    