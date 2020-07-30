import smtplib
from email.message import EmailMessage

config = {
    'from': 'thom.huynh06@gmail.com',
    'subject': 'Want food?',
    'body' : 'Hello, lets have dinner tonight!',
    'to': 'thom_huynh98@gmx.de',
    'server': 'smtp.gmail.com',
    'port': '587',
    'password': '',
} # TODO: use config or environment variables

msg = EmailMessage()
msg['Subject'] = config['subject']
msg['From'] = config['from']
msg['To'] = config['to']
msg.set_content(config['body'])

#context manager
with smtplib.SMTP(config['server'], config['port']) as smtp:
  smtp.starttls()
  smtp.login(config['from'], config['password'])
  smtp.send_message(msg)