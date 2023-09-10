import sys
import time
import os
import json
import requests
import math
import pandas as pd
import shutil

source_folder = "E://Json files (Mono)/Productivity"
target_folder = "E://Database Productive/Mono Repository"
total_request_count = 0

count = 0
total_count = len(os.listdir(source_folder))
total_commit_count = 0
index = 0
commit_count = 0

request_count = 0

existing_files = []

token =''


def get_commit_stats(commit_url):
    try:
        headers = {
            'Authorization': token
        }
        url = commit_url
        response = requests.request("GET", url, headers=headers)
        commit_content = json.loads(response.text)

        commit_stats = {'stats': commit_content['stats'], 'files': commit_content['files']}

    except Exception as error:
        print(error)
        print('line 47')
        if 'message' in commit_content:
            print(commit_content['message'])

    return commit_stats


for each_file in os.listdir(target_folder):
    existing_files.append(each_file)

with open('E://Programming/Pyhton Projects/token.json', 'r', encoding="utf8") as file:
    file_content = json.load(file)

    token = file_content['token']


existing_files.append('aws-amplify--amplify-category-api.json')
existing_files.append('NoQuarterTeam--boilerplate.json')

for each_file in os.listdir(source_folder):
    count += 1
    print(total_count - count)

    if '.json' in each_file and each_file not in existing_files:
        commit_count = 0
        with open(source_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            if file_content['Productivity'] == 'High' and len(file_content['contributors']) > 3:

                total_commit_count = len(file_content['commits'])

                print(each_file)

                for each_commit in file_content['commits']:
                    commit_count += 1
                    request_count += 1

                    if request_count > 4900:
                        sys.exit()

                    commit = each_commit['url'].replace('/git', '')
                    print('Commits left %d,  Request count: %d' % ((total_commit_count - commit_count), request_count))

                    each_commit['stats'] = get_commit_stats(commit)

                print('commits finished')

                json_data = json.dumps(file_content)
                jsonFile = open(target_folder + '/' + each_file, "w")
                jsonFile.write(json_data)
                jsonFile.close()
