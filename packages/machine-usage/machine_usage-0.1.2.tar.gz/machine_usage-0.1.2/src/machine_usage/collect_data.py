from datetime import datetime
import json

# Reads in machine_usage.dat
def CollectData(data):
    with open('/home/jan/public_html/machine_usage/machine_usage.dat') as file:
        if data == 'log_date':
            time_stamp = int(next(file))
            log_date = datetime.fromtimestamp(time_stamp)
            log_date = log_date.strftime("%d/%m/%Y, %H:%M:%S")
            return log_date
        elif data == 'usage_data':
            next(file)
            usage_data = json.load(file)
            return usage_data
