import re
import os
from .config.params import config as param
config = param()

class log_file_parser:

    def __init__(self, filename):
        self.filename = filename

    def log_file_parser_informatica(self):
        error_code_list = []
        log_file_path = os.path.join(config['log_file_path'],self.filename)

        regex_error_codes = ['(ORA-(.*):)','(RR_(.*):)', '(WRT_(.*):)','(SIP-(.*):)'] # Can be put into a config file once the different Error Codes are identified
        regex_session_name = '(ERROR(.*))'

        with open(log_file_path, "r") as file:
            for line in file:
                for match in re.finditer(regex_session_name, line, re.S):
                    match_text = match.group()
                    error_time =  re.search(': (.*) :',match_text).group(1).split('[', 1)[1].split(']')[0]
                    result = re.search('Session task instance (.*) ',match_text)
                    session_name = result.group(1).split(':')[0].replace(']','').replace('[','').replace(" ","")

                for regex_error_code in regex_error_codes:
                    for match in re.finditer(regex_error_code, line, re.S):
                        match_text = match.group()
                        rex = regex_error_code.split("(.*)")[0].replace('(','')
                        error_code = re.findall(rf'{rex}\w+',match_text)[0]
                        error_code_list.append(error_code)


        return {
        'job': session_name.rstrip('\n'),
        'code': error_code_list,
        'error_time': error_time
        }
