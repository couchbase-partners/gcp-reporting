import os
import csv
from dateutil.parser import parse

usage={}

def run():
    process_file()
    print_usage()

def process_file():
    filename='Solution use by VM hours.csv'
    hourly=0
    byol=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            process_row(row)

def process_row(row):
    date = parse(row['PartitionDate'])
    date = str(date.month) + '/1/' + str(date.year)

    if not date in usage:
        usage[date]={}
        usage[date]['hourly']=0
        usage[date]['byol']=0

    if 'byol' in row['SolutionId']:
        usage[date]['byol']+=float(row['VmHours'])
    else:
        usage[date]['hourly']+=float(row['VmHours'])

def print_usage():
    print('Date, Hourly Pricing Usage, BYOL Usage, Total Usage')
    for date in usage:
        total = usage[date]['hourly']+usage[date]['byol']
        print(date + ', ' + str(usage[date]['hourly']) + ', ' + str(usage[date]['byol']) + ', ' + str(total))

run()
