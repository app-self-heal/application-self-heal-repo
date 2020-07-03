import re
import pandas as pd
import utils.logFileParser as parser
import utils.checkRuleset as cr
import utils.self_heal_report as logger
import csv
import datetime


if __name__ == "__main__":

    #Instantiating the parser object for informatica log files
    obj_parser = parser.log_file_parser
    val = obj_parser.log_file_parser_informatica()
    print(val)

    #Instantiating the rule check object to trigger the corrective action.
    obj_crs = cr.check_rule_set(val['job'], val['code'])
    ruleset_return = obj_crs.check_ruleset()

    #Creating log
    SelfHeal_Start_Date_Time = datetime.datetime.now().strftime(" %B %d %H:%M:%S %Y") if ruleset_return['rule_flag'] == 'true' else 'NA'
    logger.self_heal_report(ruleset_return['platform'],  val['job'], val['code'], val['error_time'], ruleset_return['action_taken'], SelfHeal_Start_Date_Time)
