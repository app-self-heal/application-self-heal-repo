import pandas as pd
from .config.params import config as param
config = param()

class check_rule_set:

    def __init__(self, job_name, code):
        self.job_name = job_name
        self.code = code

    def check_ruleset(self):
        rule_file_path = config['rule_set_file']
        pdata = pd.read_csv(rule_file_path)
        pdata = pdata[(pdata['JobName'] == self.job_name) & (pdata['SelfHeal_Flag'] == 'Yes') & (pdata['ErrorCode'] == self.code)]

        pdata = pdata[['SelfHeal_Steps']]
        if pdata.empty :
            print('No rules specifies for this ruleset')
        else:
            self_heal_step = pdata.iat[0,0]

            if self_heal_step == 'Re-run Job':
                print('re-run job')

            elif self_heal_step == 'Email Notification':
                print('Email Notification')
                #Invoke the email notification functionality here
