import re
from .config.params import config as param
config = param()

class log_file_parser:

    def __init__(self):
        print('constructor')

    def log_file_parser_informatica():
        log_file_path = config['log_file_path']
        regex_error_code = '(ORA(.*):)'
        regex_session_name = '(ERROR(.*))'
        with open(log_file_path, "r") as file:
            for line in file:
                for match in re.finditer(regex_session_name, line, re.S):
                    match_text = match.group()
                    error_time =  re.search(': (.*) :',match_text).group(1).split('[', 1)[1].split(']')[0]
                    result = re.search('Session task instance (.*) :',match_text)
                    session_name = result.group(1).replace(']','').replace('[','')

                for match in re.finditer(regex_error_code, line, re.S):
                    match_text = match.group()
                    result = re.search('(.*):',match_text).group(1)
                    error_code = result
        print(error_time)
        return {
        'job': session_name.rstrip('\n'),
        'code': error_code.rstrip('\n'),
        'error_time': error_time
        }
