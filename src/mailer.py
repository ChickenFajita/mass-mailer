import smtplib
import csv
import os
from email.message import EmailMessage

config = {
    'login': 'thom.huynh06@gmail.com',
    'password': '',
    'subject': 'Want food?',
    'body' : 'Hello, lets have dinner tonight!',
}

contacts = []
#receiver context manager
with open('names.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  for line in csv_reader:
    contacts.append(line[0])

msg = EmailMessage()
msg['Subject'] = config['subject']
msg['From'] = config['login']
msg['To'] = ', '.join(contacts)
print(msg['To'])
msg.set_content(config['body'])

#context manager for connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(config['login'], config['password'])
  smtp.send_message(msg)