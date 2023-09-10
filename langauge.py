import json
import os
from collections import Counter
from matplotlib import pyplot as plt

folder_mono = "E://Json files (Mono)/DB branching"
folder_multi = "E://Json files (Multi)/DB branching"

count = 0
languages = []

# for each_file in os.listdir(folder_mono):
#     count += 1
#     print(len(os.listdir(folder_mono)) - count)
#     if '.json' in each_file:
#         with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             languages.append(file_content['languages'])
#
#
# print(Counter(languages))


languages_front = []
languages_back = []
combinations = []

for each_file in os.listdir(folder_multi):
    count += 1
    print(len(os.listdir(folder_multi)) - count)
    if '.json' in each_file:
        with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            try:
                languages_front.append(file_content['Front Repositories']['languages'])
                languages_back.append(file_content['Back Repositories']['languages'])

                combinations.append(str(file_content['Front Repositories']['languages']) + ' - ' + str(
                    file_content['Back Repositories']['languages']))
            except Exception as error:
                print(error)
                print(each_file)

print(Counter(languages_front))
print(Counter(languages_back))
print(Counter(combinations))








