import json
import os
from collections import Counter


folder_mono = "E://Json files (Mono)/DB branching"
folder_multi = "E://Json files (Multi)/DB branching"

count = 0

branchings = []


""" ****************************** Mono Repository ***************************************"""
# for each_file in os.listdir(folder_mono):
#     count += 1
#     print(len(os.listdir(folder_mono)) - count)
#     if '.json' in each_file:
#         with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             try:
#                 if len(file_content['commits']) > 5:
#                     branchings.append(file_content['Branching strategy'])
#             except Exception as error:
#                 print(error)
#                 print(each_file)
#
# print(Counter(branchings))

""" ****************************** Multi Repository ***************************************"""
branchings_front = []
branchings_back = []

for each_file in os.listdir(folder_multi):
    count += 1
    print(len(os.listdir(folder_multi)) - count)
    if '.json' in each_file:
        with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            try:
                if len(file_content['Front Repositories']['commits']) > 5:
                    branchings_front.append(file_content['Front Repositories']['Branching strategy'])
                if len(file_content['Back Repositories']['commits']) > 5:
                    branchings_back.append(file_content['Back Repositories']['Branching strategy'])
            except Exception as error:
                print(error)
                print(each_file)

print(Counter(branchings_front))
print(Counter(branchings_back))




















