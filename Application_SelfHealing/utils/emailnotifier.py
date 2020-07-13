import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from .config.params import config as param
from .config.email_template import email_templates
config = param()


#Hard coding email related values.
email_user = 'DISHapi@outlook.com'
email_password = '-PL,0OKM-PL,'
email_send = config['recepient_enail']

def init_mail(job_name, codes, platform):
    code_string = ''
    subject = f'Attention : Job {job_name} failed with code {codes}'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    for code in codes:
        code_string = code_string + code + '<br>'

    mail_template = email_templates(job_name, code_string, platform)
    body = mail_template['email_failure_notification']

    msg.attach(MIMEText(body,'html'))
    text = msg.as_string()
    server = smtplib.SMTP('outlook.office365.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()

def new_error_mail(job_name, codes, platform):
    code_string = ''
    subject = f'Attention : Job {job_name} failed with code {codes}'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    for code in codes:
        code_string = code_string + code + '<br>'

    mail_template = email_templates(job_name, code_string, platform)
    body = mail_template['email_newError_notification']

    msg.attach(MIMEText(body,'html'))
    text = msg.as_string()
    server = smtplib.SMTP('outlook.office365.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
