import json
import os
from collections import Counter

address_folder = "E://Json files (Multi)/DB branching"
# address_folder = "E://Json files (Mono)/DB branching"

productive = 0
low_productive = 0
count = 0
mean_count_list = []
mean_count = 0

language_high_productive_list = []
language_low_productive_list = []
language_non_productive_list = []

activity = 0
total_count = len(os.listdir(address_folder))

""" *********************************************** Mono Repository ************************************************ """
# for each_file in os.listdir(address_folder):
#     count += 1
#     print(total_count - count)
#
#     low = 0
#     high = 0
#
#     if '.json' in each_file:
#         with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             if len(file_content['activity']) > 15:
#                 activity += 1
#
#                 for each_day in file_content['activity']:
#                     if each_day['Mean'] > 1:
#                         high += 1
#                     else:
#                         low += 0.5
#
#                 if high > low:
#                     productive += 1
#                     language_high_productive_list.append(file_content['languages'])
#                 else:
#                     low_productive += 1
#                     language_low_productive_list.append(file_content['languages'])
#
#             else:
#                 language_non_productive_list.append(file_content['languages'])

""" *********************************************** Multi Repository ************************************************ """
for each_file in os.listdir(address_folder):
    count += 1
    print(total_count - count)

    low = 0
    high = 0

    if '.json' in each_file:
        with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            if len(file_content['Front Repositories']['activity']) > 15:
                activity += 1
                for each_day in file_content['Front Repositories']['activity']:
                    if each_day['Mean'] > 1:
                        high += 1
                    else:
                        low += 0.5

                if high > low:
                    productive += 1
                    language_high_productive_list.append(file_content['Front Repositories']['languages'])
                else:
                    low_productive += 1
                    language_low_productive_list.append(file_content['Front Repositories']['languages'])
            else:
                language_non_productive_list.append(file_content['Front Repositories']['languages'])


print('Productive project count: %d' % activity)
print('High productive project count: %d' % productive)
print('Low productive project count: %d' % low_productive)

print('Langauge in High Productive:')
print(Counter(language_high_productive_list))
print('Langauge in Low Productive:')
print(Counter(language_low_productive_list))
print('Langauge in Non Productive:')
print(Counter(language_non_productive_list))










