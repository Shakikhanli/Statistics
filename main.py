import json
import os
from collections import Counter

folder_mono = "E://Json files (Mono)/Productivity"
folder_multi = "E://Json files (Multi)/Productivity"

team_size = []
count = 0

one_developer = 0
two_developer = 0
three_five_developer = 0
five_ten_developer = 0
ten_25_developer = 0
more_developer = 0

# for each_file in os.listdir(folder_mono):
#     count += 1
#     print(len(os.listdir(folder_mono)) - count)
#     if '.json' in each_file:
#         with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#             # team_size.append(len(file_content['contributors']))
#
#             if len(file_content['commits']) > 2:
#                 size = len(file_content['contributors'])
#
#                 if size == 1:
#                     one_developer += 1
#                 elif size == 2:
#                     two_developer += 1
#                 elif 2 < size <= 5:
#                     three_five_developer += 1
#                 elif 5 < size <= 10:
#                     five_ten_developer += 1
#                 elif 10 < size <= 25:
#                     ten_25_developer += 1
#                 else:
#                     more_developer += 1


for each_file in os.listdir(folder_multi):
    count += 1
    print(len(os.listdir(folder_multi)) - count)
    if '.json' in each_file:
        with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)
            contributors = []
            for each_contributor in file_content['Front Repositories']['contributors']:
                contributors.append(each_contributor['contributor_name'])

            for each_contributor in file_content['Back Repositories']['contributors']:
                contributors.append(each_contributor['contributor_name'])

            contributors = list(dict.fromkeys(contributors))

            size = len(contributors)

            if size == 1:
                one_developer += 1
            elif size == 2:
                two_developer += 1
            elif 2 < size <= 5:
                three_five_developer += 1
            elif 5 < size <= 10:
                five_ten_developer += 1
            elif 10 < size <= 25:
                ten_25_developer += 1
            elif size > 25:
                more_developer += 1

# print(Counter(team_size))

print('1 developer: %d' % one_developer)
print('2 developer: %d' % two_developer)
print('3-5 developer: %d' % three_five_developer)
print('5-10 developer: %d' % five_ten_developer)
print('10-25 developer: %d' % ten_25_developer)
print('More developer: %d' % more_developer)
