import smtplib
from email.mime.text import MIMEText
from custom_logger import CustomLogging


class SendEmail:
    def __init__(
            self,
            receiver_address: list or str,
            mail_title=None,
            mail_content=None
    ):
        self.receiver_address = receiver_address
        self.mail_title = mail_title
        self.mail_content = mail_content

    def send_mail(self):
        # logger 记录
        logger = CustomLogging(path='C:', filename='log.log').get_logger()
        if type(self.receiver_address) is str:
            receiver_address = self.receiver_address
        elif type(self.receiver_address) is list:
            # 将 receiver_address 从 list 格式转换为 str 格式
            receiver_address = str()
            for mail_address in self.receiver_address:
                receiver_address = receiver_address + mail_address + '; '

        mailserver = 'smtp.abc.com'  # 邮箱 smtp 服务器
        sender_address = '123@abc.com'  # 发送人邮箱地址
        sender_pwd = 'abc'  # 发送人邮箱密码
        msg = MIMEText(self.mail_content, "plain", 'utf-8')
        msg["Subject"] = self.mail_title
        msg["From"] = sender_address
        msg["To"] = receiver_address

        if type(self.receiver_address) is str:
            try:
                smtp_server = smtplib.SMTP(mailserver)  # 连接邮箱服务器
                smtp_server.login(sender_address, sender_pwd)  # 登陆邮箱服务器
                smtp_server.sendmail(sender_address, self.receiver_address, msg.as_string())  # 发送邮件
                smtp_server.quit()
                logger.info('发送至 ' + self.receiver_address + ' 邮件发送成功')
                print('发送至 ' + self.receiver_address + ' 邮件发送成功')

            except smtplib.SMTPException as e:
                logger.error('发送至 ' + self.receiver_address + ' 邮件发送失败,失败原因：', e)
                print('发送至 ' + self.receiver_address + ' 邮件发送失败,失败原因：', e)

        elif type(self.receiver_address) is list:
            for mail_address in self.receiver_address:
                try:
                    smtp_server = smtplib.SMTP(mailserver)  # 连接邮箱服务器
                    smtp_server.login(sender_address, sender_pwd)  # 登陆邮箱服务器
                    smtp_server.sendmail(sender_address, mail_address, msg.as_string())  # 发送邮件
                    smtp_server.quit()
                    logger.info('发送至 ' + mail_address + ' 邮件发送成功')
                    print('发送至 ' + mail_address + ' 邮件发送成功')

                except smtplib.SMTPException as e:
                    logger.error('发送至 ' + mail_address + ' 邮件发送失败,失败原因：', e)
                    print('发送至 ' + mail_address + ' 邮件发送失败,失败原因：', e)
        else:
            pass


if __name__ == '__main__':
    content = 'test'
    title = 'test'
    rev = '123@abc.com'
    send = SendEmail(rev, mail_title=title, mail_content=content)
    send.send_mail()
