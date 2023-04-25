import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import Constants

service_key = Constants.GMAIL_PASSKEY

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'Tim DeHof'
email['to'] = 'ttdehof@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({
    'name': 'TinTin',
}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('timdehoftest@gmail.com', service_key)
    smtp.send_message(email)
    print('all good boss!')
