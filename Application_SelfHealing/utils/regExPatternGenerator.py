import re
import os
import pandas as pd
from .config.params import config as param
config = param()
rule_file_path = config['rule_set_file']


def regEx_error_code_pattern_generator():
    # ===== Read the distinct patterns of error code from the ruleSet file ======#
    pdata = pd.read_csv(rule_file_path)
    error_code_list = pdata['ErrorCode'].values.tolist()
    error_code_list = ['(' + re.sub('[0-9]', '', i) + '(.*):)' for i in error_code_list];

    return list(set(error_code_list))
