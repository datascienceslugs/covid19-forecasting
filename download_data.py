"""
I re-hosted the files on my server so that they're easier to download
and don't require setting up the kaggle API

whenever a new data set comes out I'll push the new ones up
"""

import sys
import os
import requests
import csv

this_dir = os.path.dirname(__file__)

if len(sys.argv) <= 1:
    print("Provide the folder for which week you want to download the files for. E.g. python3 download_data.py week2")
    sys.exit(1)

target_week_dir = os.path.join(this_dir, sys.argv[1])
if not os.path.exists(target_week_dir):
    print(f"Could not find a directory at {os.path.abspath(target_week_dir)}")
    sys.exit(1)

raw_dir = os.path.join(this_dir, sys.argv[1], "data", "raw")

os.makedirs(raw_dir, exist_ok=True)

print("Note: this takes a while to download... ")

# rehosted the csv files on my server so we dont have to use kaggle API on everyones machine
base_url = f"https://seanbr.com/remsync/covid_data/{sys.argv[1]}"

files = ("submission.csv", "test.csv", "train.csv")

def download(file_name):
    print(f"Downloading {file_name}...")
    resp = requests.get(f"{base_url}/{file_name}")
    resp.raise_for_status() # exit if failed
    csv_content = resp.content.decode('utf-8')
    with open(os.path.join(raw_dir, file_name), 'w') as write_to:
        write_to.write(csv_content)

for f in files:
    download(f)
