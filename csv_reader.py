import csv


EVENT_TYPES = ["event_name", "days", "time", "location"]

# opens and reads files
def file_opener(csv_file):

    with open(csv_file, mode='r') as file:
        csvFile = csv.reader(file) 
        header = next(csvFile)
        org_dict = {}
        for lines in csvFile:
            org_dict = file_dict_maker(org_dict, lines)
            print(org_dict)

def file_dict_maker(dictionary, line):
    size = len(dictionary) 
    event_num = size + 1

    dictionary[f"Event-{event_num}"] = {}
    for i in range(len(line)):
        info = "" if len(line[i]) == 0 else line[i]
    
        dictionary[f"Event-{event_num}"][EVENT_TYPES[i]] = info
    return dictionary

