import csv
import datetime
import os.path
from .config.params import config as param
config = param()

file_exists = os.path.isfile(config['self_heal_report'])

def self_heal_report(platform, job, code, error_time, action_taken, self_heal_time):
    with open(config['self_heal_report'], 'a', newline='') as csvfile:
        fieldnames = ['Platform','JobName', 'ErrorCode', 'Failure_Date_Time', 'Action_Taken','SelfHeal_Start_Date_Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow({'Platform': platform,
                        'JobName': job,
                        'ErrorCode': code,
                        'Failure_Date_Time': error_time,
                        'Action_Taken': action_taken,
                        'SelfHeal_Start_Date_Time': self_heal_time})

def new_error_code(job, code):
    with open(config['rule_set_file'], 'a', newline='') as csvfile:
        fieldnames = ['Platform','JobName', 'ErrorCode','SelfHeal_Flag','SelfHeal_Steps']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        Platform = 'Informatica'
        Flag = 'No'
        Step = 'Email Notification'

        listtostr = ''.join([str(elem) for elem in code])
        writer.writerow({'Platform': Platform,
                        'JobName': job,
                        'ErrorCode': listtostr,
                        'SelfHeal_Flag': Flag,
                        'SelfHeal_Steps': Step})
