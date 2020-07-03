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
