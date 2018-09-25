import smtplib
from email.mime.text import MIMEText


class SendEmail:
    def __init__(
            self,
            receiver_address: str,
            mail_title=None,
            mail_content=None
    ):
        self.receiver_address = receiver_address
        self.mail_title = mail_title
        self.mail_content = mail_content

    def send_mail(self):
        mailserver = 'your email smtp server address'  # 邮箱 smtp 服务器
        sender_address = 'abc@abc.com'  # 发送人邮箱地址
        sender_pwd = 'abc'  # 发送人邮箱密码
        msg = MIMEText(self.mail_content, "plain", 'utf-8')
        msg["Subject"] = self.mail_title
        msg["From"] = sender_address
        msg["To"] = self.receiver_address
        try:
            smtp_server = smtplib.SMTP(mailserver)  # 连接邮箱服务器
            smtp_server.login(sender_address, sender_pwd)  # 登陆邮箱服务器
            smtp_server.sendmail(sender_address, self.receiver_address, msg.as_string())  # 发送邮件
            smtp_server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败,失败原因：', e)


if __name__ == '__main__':
    content = 'test'
    title = 'test_title'
    rev = 'qwerty@qwerty.com'
    send = SendEmail(receiver_address=rev, mail_title=title, mail_content=content)
    send.send_mail()
