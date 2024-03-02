import smtplib
import credentials
from email.mime.text import MIMEText
smtp_server = smtplib.SMTP('smtp.gmail.com: 587')
smtp_server.starttls()
email = credentials.email
password = credentials.password
smtp_server.login(email,password)
message = MIMEText('Python email automation involves using Python to automate tasks such as sending, receiving, parsing emails, managing lists, scheduling, and monitoring, facilitated by libraries like `smtplib` and `imaplib`, enhancing efficiency and scalability in email-related workflows.')
To = 'jeevanskoushik@gmail.com'
message['From'] = email
message['To'] = To
message['Subject'] = 'Automated Email'
smtp_server.sendmail(email,To,message.as_string())
# confirmation
print("Email confirming success has been dispatched.")