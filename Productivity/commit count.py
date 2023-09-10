import json
import os
from collections import Counter

address_folder = "E://Json files (Multi)/Productivity"
# address_folder = "E://Json files (Mono)/Productivity"

zero_five = 0
six_ten = 0
eleven_25 = 0
twentysix_50 = 0
more_50 = 0

count = 0
total_count = len(os.listdir(address_folder))

ghf_commits_high_productive_list = []
ghf_commits_low_productive_list = []

gf_commits_high_productive_list = []
gf_commits_low_productive_list = []


""" *********************************************** Mono Repository ************************************************ """
# for each_file in os.listdir(address_folder):
#     count += 1
#     print(total_count - count)
#
#     if '.json' in each_file:
#         commit_count = 0
#         # print(each_file)
#         with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             commit_count = len(file_content['commits'])
#
#             if file_content['Branching strategy'] == 'GitFlow' and file_content['Productivity'] == 'Low':
#
#                 if 1 < commit_count < 50:
#                     zero_five += 1
#                 elif 50 < commit_count < 100:
#                     six_ten += 1
#                 elif 100 < commit_count < 250:
#                     eleven_25 += 1
#                 elif 250 < commit_count < 500:
#                     twentysix_50 += 1
#                 elif 500 < commit_count:
#                     more_50 += 1


""" *********************************************** Mono Repository ************************************************ """
for each_file in os.listdir(address_folder):
    count += 1
    print(total_count - count)

    if '.json' in each_file:
        commit_count = 0
        # print(each_file)
        with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            commit_count = len(file_content['Back Repositories']['commits'])

            if file_content['Back Repositories']['Branching strategy'] == 'Github Flow' and file_content['Back Repositories']['Productivity'] == 'Low':

                if 1 < commit_count < 50:
                    zero_five += 1
                elif 50 < commit_count < 100:
                    six_ten += 1
                elif 100 < commit_count < 250:
                    eleven_25 += 1
                elif 250 < commit_count < 500:
                    twentysix_50 += 1
                elif 500 < commit_count:
                    more_50 += 1







Branch_count = {'0-50': zero_five, '50-100': six_ten, '100-250': eleven_25, '250-500': twentysix_50, 'more 500': more_50}
print(Branch_count)





















