import smtplib
import csv
import os
from config import config
from email.message import EmailMessage

contacts = []
#context manager
with open('names.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  for line in csv_reader:
    contacts.append(line[0])

msg = EmailMessage()
msg['Subject'] = config['subject']
msg['From'] = config['login']
msg['To'] = ', '.join(contacts)
msg.set_content(config['body'])

#context manager for connection handling
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  
  smtp.login(config['login'], config['password'])
  smtp.send_message(msg)
  print("Emails sent!")