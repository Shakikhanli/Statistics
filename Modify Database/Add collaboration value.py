import sys
import time
import os
import json
import requests
import math
import pandas as pd
import shutil

source_folder = "E://Json files (Multi)/Productivity"
target_folder = "E://Database Productive/Multi Repository"
total_request_count = 0

count = 0
total_count = len(os.listdir(source_folder))
total_commit_count = 0
index = 0
commit_count = 0

request_count = 0
existing_files = []

token = ''


def get_contributors(contributors_url):
    try:
        headers = {
            'Authorization': token
        }
        url = contributors_url
        response = requests.request("GET", url, headers=headers)
        contributor_list = json.loads(response.text)
    except Exception as error:
        print(error)
        print('line 47')
        if 'message' in contributor_list:
            print(contributor_list['message'])

    return contributor_list


for each_file in os.listdir(target_folder):
    existing_files.append(each_file)

with open('E://Programming/Pyhton Projects/token.json', 'r', encoding="utf8") as file:
    file_content = json.load(file)

    token = file_content['token']

for each_file in os.listdir(source_folder):
    count += 1
    print(' %d Projects left. Request count: %d' % ( (total_count - count), request_count) )

    if '.json' in each_file and each_file not in existing_files:
        commit_count = 0
        with open(source_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            if len(file_content['Back Repositories']['contributors']) > 2 and file_content['Back Repositories']['Productivity'] != 'None':

                request_count += 2

                if request_count > 4900:
                    sys.exit()

                # if file_content['Front Repositories']['Productivity'] == 'High' and len(file_content['Front Repositories']['contributors']) > 3:
                contributors_url = file_content['Front Repositories']['repo_url'] + '/contributors'
                file_content['Front Repositories']['contributors'] = get_contributors(contributors_url)

                contributors_url = file_content['Back Repositories']['repo_url'] + '/contributors'
                file_content['Back Repositories']['contributors'] = get_contributors(contributors_url)

                json_data = json.dumps(file_content)
                jsonFile = open(target_folder + '/' + each_file, "w")
                jsonFile.write(json_data)
                jsonFile.close()



























