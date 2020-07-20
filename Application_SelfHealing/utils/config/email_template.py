def email_templates(job_name, code_string, platform):
    template = {
    "email_failure_notification": f"""<p1>Hi Team,
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
                </TABLE>""",

    "email_newError_notification": f"""<p1>Hi Team,
                <br>This is to notify that the failed job doesn't come under self heal category. Please find the details of the job failure below
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
                      <TD>New entry has been added to backend with "No" self heal action. Please rectify and reply back with subject: <br>[RERUN]|{job_name}</TD>
                   </TR>
                </TABLE>"""

    }

    return template
