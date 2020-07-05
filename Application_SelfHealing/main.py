import csv
import datetime
import os
import utils.logFileParser as parser
import utils.checkRuleset as cr
import utils.self_heal_report as logger
from utils.config.params import config as param

config = param()

if __name__ == "__main__":
    log_directory = config['log_file_path']
    for filename in os.listdir(log_directory):

        """
        If the logfile needs to be renamed to a .done file post processing, the below logic can be implemented.
        So that it will not be re-processed on the next run-
        
         os.rename(os.path.join(dir,filename), os.path.join(dir,filename+'.done'))
        """
        #Instantiating the parser object for informatica log files
        obj_parser = parser.log_file_parser(filename)
        val = obj_parser.log_file_parser_informatica()
        print(val)

        #Instantiating the rule check object to trigger the corrective action.
        obj_crs = cr.check_rule_set(val['job'], val['code'])
        ruleset_return = obj_crs.check_ruleset()

        #Creating log
        SelfHeal_Start_Date_Time = datetime.datetime.now().strftime(" %B %d %H:%M:%S %Y") if ruleset_return['rule_flag'] == 'true' else 'NA'
        logger.self_heal_report(ruleset_return['platform'],  val['job'], val['code'], val['error_time'], ruleset_return['action_taken'], SelfHeal_Start_Date_Time)
