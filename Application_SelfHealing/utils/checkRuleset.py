import pandas as pd
import utils.emailnotifier as emailer
from .config.params import config as param
import utils.self_heal_report as ruleset
config = param()

#Class to do a look up on the the rules table.
class check_rule_set:

    #Init function to initialise variables
    def __init__(self, job_name, code):
        self.job_name = job_name
        self.code = code

    #Function to perform The look-up
    def check_ruleset(self):
        rule_file_path = config['rule_set_file']
        pdata = pd.read_csv(rule_file_path)
        pdata = pdata[(pdata['JobName'] == self.job_name) & (pdata['SelfHeal_Flag'] == 'Yes') & (pdata['ErrorCode'].isin(self.code))]
        platform = pdata[['Platform']]
        pdata = pdata[['SelfHeal_Steps']]
        if pdata.empty :
            rule_flag = 'false'
            platform = 'NA'
            self_heal_step = 'Self Healing Action Not Specified'
            ruleset.new_error_code(self.job_name, self.code)
            emailer.new_error_mail(self.job_name, self.code, platform)
            print('No rules specified for this, ruleset entry added to backend and Email sent')

        else:
            rule_flag = 'true'
            self_heal_step = pdata.iat[0,0]
            platform = platform.iat[0,0]

            if self_heal_step == 'Re-run Job':
                print('re-run job')

            elif self_heal_step == 'Email Notification':
                print('Email Notification')
                emailer.init_mail(self.job_name, self.code, platform)
                print('Mail Triggered')

        return {
        "rule_flag": rule_flag,
        "platform": platform,
        "action_taken": self_heal_step
        }
