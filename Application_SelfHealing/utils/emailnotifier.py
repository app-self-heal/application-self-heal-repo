import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Hard coding email related values.
email_user = 'DISHapi@outlook.com'
email_password = '-PL,0OKM-PL,'
email_send = 'noejoseph@deloitte.com'
subject = 'Attention : Job failed'
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
body = ' Hi Team,\n\n This is to inform that job has failed. \n \n Thanks & Regards, \n DISHApi'
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()

def init_mail():
    server = smtplib.SMTP('outlook.office365.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()