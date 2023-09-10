import json
import os
import pandas as pd
from xlsxwriter import Workbook

folder_mono = "E://Json files (Mono)/DB branching"
folder_multi = "E://Json files (Multi)/DB branching"

folder_mono_pro = "E://GDrive/Mono"

count = 0

total_activity = 0

max = 500

name = 'aws-amplify--amplify-category-api.json'

df = pd.DataFrame(
    columns=['Project name', 'Commits', 'Events', 'Issues', 'pull_requests', 'pull_comments', 'issues_comments'])

dict_list = []

for each_file in os.listdir(folder_mono_pro):
    count += 1
    print(len(os.listdir(folder_mono_pro)) - count)
    if '.json' in each_file:
        with open(folder_mono_pro + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            dict1 = {'Project name': '', 'Commits': 0, 'Events': 0, 'Issues': 0, 'Pull requests': 0,
                     'Pull comments': 0, 'Issue comments': 0}

            total_activity = len(file_content['issues']) + len(file_content['pull_requests']) + len(
                file_content['commits']) + len(file_content['events']) + len(file_content['pull_comments']) + len(
                file_content['issues_comments'])

            dict1['Project name'] = each_file
            dict1['Commits'] = len(file_content['commits'])
            dict1['Events'] = len(file_content['events'])
            dict1['Issues'] = len(file_content['issues'])
            dict1['Pull requests'] = len(file_content['pull_requests'])
            dict1['Pull comments'] = len(file_content['pull_comments'])
            dict1['Issue comments'] = len(file_content['issues_comments'])

            if total_activity > max:
                # max = total_activity
                # print(' Most active project for now is %s' % each_file)
                dict_list.append(dict1)

df = pd.DataFrame.from_records(dict_list)

# writer = pd.ExcelWriter('Most active projects (Mono).xlsx', engine='xlsxwriter')
# df.to_excel(writer, 'Sheet1')
# writer.save()


df.to_excel('output.xlsx', index=False)





















# with open(folder_mono_pro + '/' + name, 'r', encoding="utf8") as file:
#     file_content = json.load(file)
#
#     print('issues %d' % len(file_content['issues']))
#     print('pull_requests %d' % len(file_content['pull_requests']))
#     print('commits %d' % len(file_content['commits']))
#     print('events %d' % len(file_content['events']))
#     print('pull_comments %d' % len(file_content['pull_comments']))
#     print('issues_comments %d' % len(file_content['issues_comments']))
