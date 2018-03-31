import os
import csv
from dateutil.parser import parse

revenue={}

def run():
    filenames=get_filenames()
    for filename in filenames:
        process_file(filename)
    print_revenue()

def get_filenames():
    filenames=[]
    for file in os.listdir("./revenue"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./revenue", file))
    return filenames

def process_file(filename):
    date = filename
    date = date.replace('./revenue/', '')
    date = date.replace('.csv', '')
    date = parse(date)
    date = str(date.month) + '/1/' + str(date.year)

    revenue=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            process_row(date, row)

def process_row(date, row):
    if not date in revenue:
        revenue[date]={}
        revenue[date]['revenue']=0

    # legacy report
    if 'amount' in row:
        revenue[date]['revenue']+=float(row['amount'])

    # current report
    if 'Due Partner' in row:
        revenue[date]['revenue']+=float(row['Due Partner'])

def print_revenue():
    print('Month, Revenue')
    for date in revenue:
        print(date + ', ' + str(revenue[date]['revenue']))

run()
