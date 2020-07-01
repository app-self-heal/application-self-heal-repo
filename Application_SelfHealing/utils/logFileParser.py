import re

class log_file_parser:

    def __init__(self):
        print('constructor')

    def log_file_parser_informatica():
        log_file_path = r"C:\Users\noejoseph\Documents\PythonProjects\SampleLog.log"
        regex_error_code = '(ERROR(.*))'
        with open(log_file_path, "r") as file:
            for line in file:
                for match in re.finditer(regex_error_code, line, re.S):
                    match_text = match.group()
                    result = re.search('Session task instance (.*) :',match_text)
                    session_name = result.group(1).replace(']','').replace('[','')
                    result = re.search('exited with error(.*)',line)
                    error_code = result.group(1).replace(']','').replace('[','')
                                        
        return {
        'job': session_name.rstrip('\n'),
        'code': int(error_code.rstrip('\n'))
        }
