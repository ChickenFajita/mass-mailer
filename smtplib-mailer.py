import smtplib
import csv
from config import config
from email.message import EmailMessage

msg_tuples = []
#context manager
with open('names.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  for line in csv_reader:
    msg_tuples.append(line)

#context manager for connection handling
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(config['login'], config['password'])

  for tuple in msg_tuples:
    msg = EmailMessage()
    msg['From'] = config['login']
    msg['To'] = tuple[0].strip()
    msg['Subject'] = tuple[1].strip()
    msg.set_content(tuple[2].strip())
    smtp.send_message(msg)
    print(f"Sent to: {tuple[0]}: Subject: {tuple[1]}")
