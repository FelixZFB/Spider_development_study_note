from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 先定义一个格式化邮件地址的方法
# 发件人和收件人，注意不能简单地传入name <addr@example.com>，
# 因为如果包含中文，需要通过Header对象进行编码。
# 下面的方法传入的参数包含一些中文字符和一个邮件地址
# 会自动进行格式化会可以识别的邮件地址，
# 表面看起来一个字符串：一号爬虫<zfb123zfb@126.com> ，实际代表zfb123zfb@126.com这个邮箱地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 发件人邮箱地址和密码,网易邮箱服务器地址
from_addr = 'zfb123zfb@126.com'
password = 'zfb123456zfb'
smtp_server = 'smtp.126.com'

# 收件人地址
to_addr = '18200116656@qq.com'

# 设置邮件的信息
# 正文信息，三个参数，第一个为文本内容，第二个 plain 设置纯文本格式，第三个 utf-8 设置编码
msg = MIMEText('Python爬虫运行异常，异常信息为遇到HTTP 403错误', 'plain', 'utf-8')
# 发送邮件中显示的：发送者和接收者的信息，参考邮件图片
msg['From'] = _format_addr('一号爬虫<%s>' % from_addr)
msg['To'] = _format_addr('一号爬虫主人<%s>' % to_addr)
# 邮件主题
msg['Subject'] = Header('一号爬虫运行状态', 'utf-8').encode()

# 发送邮件，一般情况下 SMTP 端口号为25
try:
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")






