import smtplib
import logging
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d  %H:%M:%S %a' # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")

mail_host = "smtp.qq.com"
mail_user = "1432305526@qq.com"
mail_pass = "ubujrqiqpgdlfhda"

sender = '1432305526@qq.com'
receivers = ['1432305526@qq.com']

message = MIMEMultipart()
message['From'] = Header(sender)
message['To'] = Header('1432305526@qq.com')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
puretext = MIMEText('<h1 style="color:red;">我的第一份Python邮件</h1>', 'html', 'utf-8')
message.attach(puretext)


message1 = """From: From Person <from@fromdomain.com>
                To: To Person <to@todomain.com>
                MIME-Version: 1.0
                Content-type: text/html
                Subject: SMTP HTML e-mail test
                
                This is an e-mail message to be sent in HTML format
                
                <b>This is HTML message.</b>
                <h1>This is headline.</h1>
            """

jpgpart = MIMEImage(open('../November/pic3.png', 'rb').read())
jpgpart.add_header('Content-Disposition', 'attachment', filename='test.jpg')
message.attach(jpgpart)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.set_debuglevel(1)  # 打印调试代码
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    # print("邮件带附件发送成功")
    logging.info("邮件附件发送成功")
except smtplib.SMTPException:
    # print("邮件带附件发送失败")
    logging.warning("邮件附件发送失败")
