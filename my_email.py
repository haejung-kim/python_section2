from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL
# 3-6-8 연동 성공

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 465
SMTP_USER = 'wowkk006@naver.com'
SMTP_PASSWORD = '1q2w3e4r'

def send_mail(name, addr, contents, attachment=False):
#  msg (메일에 있는 From , To, Subject, 및 본문 에 보일 내용)
    msg = MIMEMultipart('alternative')

    if attachment:
        msg = MIMEMultipart('mixed')

    msg['From'] = name +'<%s>'%SMTP_USER         
    msg['To'] = addr
    msg['Subject'] = '메일 제목'

    text = MIMEText(contents)
    msg.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octet-stream')
        f = open(attachment, 'rb')
        file_contents = f.read()
        file_data.set_payload(file_contents)
        encoders.encode_base64(file_data)

        from os.path import basename
        filename = basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file_data)

    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    smtp.close()

# TEST 해보기    ( 큰의미없음  ,수신 email,  메일 세부내용  , 첨부파일)
# send_mail('wowkk006@naver.com', 'wowkk006@empas.com', '네이버 검색 결과입니다')
