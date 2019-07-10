import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

msg = EmailMessage()
msg['Subject'] = '메일 제목'
msg['From'] = '보내는 사람 이메일 주소'
msg['To'] = '받는 사람 이메일 주소'
msg.set_content('메일 내용')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('아이디', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')