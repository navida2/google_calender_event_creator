import csv
from datetime import datetime
import random

EVENT_TYPES = ["summary", "days", "time", "location"]

# opens and reads files
def file_opener(csv_file):
    with open(csv_file, mode='r') as file:
        csvFile = csv.reader(file) 
        header = next(csvFile)
        org_dict = {}
        for lines in csvFile:
            org_dict = file_dict_maker(org_dict, lines)
        return org_dict

def file_dict_maker(dictionary, line):
    size = len(dictionary) 
    event_num = size + 1
    dictionary[f"Event-{event_num}"] = {}
    for i in range(len(line)):
        info = "" if len(line[i]) == 0 else line[i].strip()
        dictionary[f"Event-{event_num}"][EVENT_TYPES[i]] = info
    return dictionary

def convert_to_24_hour_timezone(time):
    converted_time = datetime.strptime(time, '%I:%M %p').strftime('%H:%M:%S')
    return converted_time

def format_into_google_calender_event(dictionary):
    qtr_start = input("Enter the date your quarter starts(YYYY-MM-DD):" )
    qtr_ends = input("Enter the date your quarter ends(YYYY-MM-DD):" )
    for keys, events in dictionary.items():
        start_end_times = events["time"].split('-')
        converted_start_time = convert_to_24_hour_timezone(start_end_times[0])
        converted_end_time = convert_to_24_hour_timezone(start_end_times[1])
        event = {
            'summary': events['summary'],
            'location': events['location'],
            'description': "",
            'start':{
                'dateTime':f"{qtr_start}T{converted_start_time}",
                'timeZone':'America/Los_Angeles',
            },
            'end':{
                'dateTime':f"{qtr_start}T{converted_end_time}",
                'timeZone':'America/Los_Angeles',
            },
            'recurrence': [
                 f"RRULE:FREQ=WEEKLY;UNTIL=20250620;BYDAY={','.join(events['days'].split())}",
            ],
         'reminders': {
            'useDefault': True,
         },   
         'colorId': random_color()
        }
        dictionary[keys] = event
    return dictionary

def random_color():
    return str(random.randint(1,11))



