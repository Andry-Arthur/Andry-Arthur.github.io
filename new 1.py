import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject = 'Office hours attendance tonight:'
    body = 'Here are the students who attended office hours:'
    
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS, 'rakoan02@gettysburg.edu', msg)