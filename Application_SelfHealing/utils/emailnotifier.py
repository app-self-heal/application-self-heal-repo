import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from .config.params import config as param
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
    body = f"""<p1>Hi Team,
<br>Please find the details of the job failure below
<br>
<br>
<br></p1>
<TABLE BORDER="2"    WIDTH="100%"   CELLPADDING="3" CELLSPACING="2">
	<colgroup>
       <col span="1" style="width: 15%;">
       <col span="1" style="width: 15%;">
       <col span="1" style="width: 15%;">
    </colgroup>
   <TR>
      <TH COLSPAN="4"><BR><H3>FAILURE NOTIFICATION</H3>
      </TH>
   </TR>
   <TR>
      <TH>Platform</TH>
      <TH>Job Name</TH>
      <TH>Error Code</TH>
      <TH>Next Steps</TH>
   </TR>
   <TR ALIGN="">
      <TD>{platform}</TD>
      <TD>{job_name}</TD>
      <TD>{code_string}</TD>
      <TD>Please rectify and reply back with subject: <br>[RERUN]|{job_name}</TD>
   </TR>
</TABLE>"""

    msg.attach(MIMEText(body,'html'))
    text = msg.as_string()
    server = smtplib.SMTP('outlook.office365.com',587)
    server.starttls()
    server.login(email_user,email_password)
    server.sendmail(email_user,email_send,text)
    server.quit()
