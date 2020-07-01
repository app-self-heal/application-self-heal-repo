import re
import pandas as pd
import utils.logFileParser as parser
import utils.checkRuleset as cr


if __name__ == "__main__":

    #Instantiating the parser object for informatica log files
    obj_parser = parser.log_file_parser
    val = obj_parser.log_file_parser_informatica()
    print(val)

    #Instantiating the rule check object to trigger the corrective action.
    obj_crs = cr.check_rule_set(val['job'], val['code'])
    obj_crs.check_ruleset()
