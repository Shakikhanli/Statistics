import json
import os
from collections import Counter

# address_folder = "E://Json files (Multi)/DB branching"
target_folder = "E://Json files (Multi)/Productivity"
address_folder = "E://Json files (Mono)/Productivity"

productive = 0
low_productive = 0
non_productive = 0
count = 0
mean_count_list = []
mean_count = 0

high_productive_list = []
low_productive_list = []
non_productive_list = []

activity = 0
total_count = len(os.listdir(address_folder))

""" *********************************************** Mono Repository ************************************************ """
for each_file in os.listdir(address_folder):
    count += 1
    print(total_count - count)

    low = 0
    high = 0

    if '.json' in each_file:
        with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            if len(file_content['activity']) > 50:
                new_list = []

                for each_day in file_content['activity']:
                    if each_day['Mean'] > 1:
                        high += 1
                    else:
                        low += 0.5
                    new_list.append(each_day['Mean'])

                if high > low:
                    print(new_list)
                    break



            # if len(file_content['activity']) > 15:
            #     activity += 1
            #
            #     for each_day in file_content['activity']:
            #         if each_day['Mean'] > 1:
            #             high += 1
            #         else:
            #             low += 0.5
            #
            #     if high > low:
            #         productive += 1
            #         high_productive_list.append(file_content['Branching strategy'])
            #         file_content['Productivity'] = 'High'
            #     else:
            #         low_productive += 1
            #         low_productive_list.append(file_content['Branching strategy'])
            #         file_content['Productivity'] = 'Low'
            #
            # else:
            #     non_productive += 1
            #     non_productive_list.append(file_content['Branching strategy'])
            #     file_content['Productivity'] = 'None'
            #
            # json_data = json.dumps(file_content)
            # jsonFile = open(target_folder + '/' + each_file, "w")
            # jsonFile.write(json_data)
            # jsonFile.close()

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
                    high_productive_list.append(file_content['Front Repositories']['Branching strategy'])
                    file_content['Front Repositories']['Productivity'] = 'High'
                else:
                    low_productive += 1
                    low_productive_list.append(file_content['Front Repositories']['Branching strategy'])
                    file_content['Front Repositories']['Productivity'] = 'Low'
            else:
                non_productive += 1
                non_productive_list.append(file_content['Front Repositories']['Branching strategy'])
                file_content['Front Repositories']['Productivity'] = 'None'

            if len(file_content['Back Repositories']['activity']) > 15:
                activity += 1
                for each_day in file_content['Back Repositories']['activity']:
                    if each_day['Mean'] > 1:
                        high += 1
                    else:
                        low += 0.5
                if high > low:
                    productive += 1
                    high_productive_list.append(file_content['Back Repositories']['Branching strategy'])
                    file_content['Back Repositories']['Productivity'] = 'High'
                else:
                    low_productive += 1
                    low_productive_list.append(file_content['Back Repositories']['Branching strategy'])
                    file_content['Back Repositories']['Productivity'] = 'Low'
            else:
                non_productive += 1
                non_productive_list.append(file_content['Back Repositories']['Branching strategy'])
                file_content['Back Repositories']['Productivity'] = 'None'

            json_data = json.dumps(file_content)
            jsonFile = open(target_folder + '/' + each_file, "w")
            jsonFile.write(json_data)
            jsonFile.close()






print('Productive project count: %d' % activity)
print('High productive project count: %d' % productive)
print('Low productive project count: %d' % low_productive)
print('Non productive project count: %d' % non_productive)

print('High Productive:')
print(Counter(high_productive_list))
print('Low Productive:')
print(Counter(low_productive_list))
print('Non Productive:')
print(Counter(non_productive_list))










