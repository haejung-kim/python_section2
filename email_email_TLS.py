
# TLS (Naver) 
# 단순히
import smtplib
from email.mime.text import MIMEText

sendEmail = "wowkk006@naver.com"   # 보내느 email (gmail일때 id@gmail.co)
recvEmail = "wowkk006@empas.com"     # 수신 email
password = "1q2w3e4r"                 # password

smtpName = "smtp.naver.com" #smtp 서버 (Gmail일때는 smtp.gmail.com)
smtpPort = 587 #smtp 포트 번호

text = "매일 내용"
msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

msg['Subject'] ="이것은 메일제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string())

s=smtplib.SMTP(smtpName ,smtpPort) #메일 서버 연결
s.ehlo()
s.starttls()            #TLS 보안 처리
s.login(sendEmail,password)            #로그인
s.sendmail(sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
s.close() #smtp 서버 연결을 종료합니다.
