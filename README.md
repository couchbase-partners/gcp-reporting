# gcp-reporting
These are scripts to crunch GCP reports.  

## Usage
First off, you're going to need a copy of "Solution use by VM hours.csv" for the maximum time period.  You can download that from [here](https://console.cloud.google.com/partner/analytics?project=couchbase-public).

After that you can run:

    python usage.py

## Revenue
The revenue information is all in a Google drive that Google shares with us.  You'll need to grab the latest month and dump that in a csv under the revenue directory.  For that you want the "Charges and Usage" file.  Rename that to be the date with a '.csv' at the end.

After that you can run:

    python revenue.py
