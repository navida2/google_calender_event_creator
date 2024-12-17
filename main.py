import api
import csv_reader

def main():
    read_dict = csv_reader.file_opener('test.csv')
    read_dict = csv_reader.format_into_google_calender_event(read_dict)
    
    service = api.api_validate()
    calender_name = input("Enter the name for this calender ")
    cal_id = api.create_calender(service, calender_name)
    for event_id, event in read_dict.items():
        api.add_events(service, cal_id,event)
    print("Action completed")
    
    
if __name__ == '__main__':
    main()
    
