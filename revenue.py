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

    hourly=0
    byol=0
    legacyfree=0
    legacypaid=0

#    with open(filename) as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            process_row(row)

def update_revenue(row):
    date = row['Charge Date']
    if date:
        date = date.split(' ')[0]
        date = parse(date)
        date = str(date.month) + '/1/' + str(date.year)
    else:
        date = None

    if date:
        if not date in revenue:
            revenue[date]={}
            revenue[date]['revenue']=0
            revenue[date]['legacyrevenue']=0

        if 'Charge' in row['Transaction Type'] or 'Customer Refund' in row['Transaction Type']:
            if 'Hourly Pricing' in row['SKU']:
                revenue[date]['revenue']+=float(row['Payout Amount (PC)'])
            else:
                revenue[date]['legacyrevenue']+=float(row['Payout Amount (PC)'])

def print_revenue():
    print('Month, Revenue, Legacy Revenue, Total Revenue')
    for date in revenue:
        total = revenue[date]['revenue']+revenue[date]['legacyrevenue']
        print(date + ', ' + str(revenue[date]['revenue']) + ', ' + str(revenue[date]['legacyrevenue']) + ', ' + str(total))

run()
