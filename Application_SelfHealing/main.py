import csv
import datetime
import os
import glob
import utils.logFileParser as parser
import utils.checkRuleset as cr
import utils.self_heal_report as logger
from utils.config.params import config as param

config = param()

if __name__ == "__main__":
    log_directory = config['log_file_path']
    log_archive = config['log_archive']
    polling_flag = 1
    while polling_flag == 1:
        # Check for termination file
        termination_file_count = len(glob.glob1(log_directory,"*.termination"))
        logfile_count = len(glob.glob1(log_directory,"*.log"))

        if (termination_file_count > 0 and logfile_count == 0):
            polling_flag = 0

        for filename in os.listdir(log_directory):

            if filename.endswith(".log"):
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

                #Move the processed log-file to archive folder
                time_stamp_suffix = datetime.datetime.now().strftime("%b-%d-%y-%H-%M-%S")
                if os.path.isdir(log_archive) == False:
                    os.mkdir(log_archive)
                if os.path.isfile(os.path.join(log_archive,filename.split('.log')[0] + '.' + time_stamp_suffix + ".log")) == False:
                    os.rename(os.path.join(log_directory,filename), os.path.join(log_archive,filename.split('.log')[0] + '.' + time_stamp_suffix + ".log"))

            elif filename.endswith(".termination") and polling_flag == 0:
                os.remove(os.path.join(log_directory,filename))
