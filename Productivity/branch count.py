import json
import os
from collections import Counter

# address_folder = "E://Json files (Multi)/Productivity"
address_folder = "E://Json files (Mono)/Productivity"

productive = 0
low_productive = 0
non_productive = 0
count = 0
branch_list = []
mean_count = 0

zero_five = 0
six_ten = 0
eleven_25 = 0
twentysix_50 = 0
more_50 = 0

ghf_branches_high_productive_list = []
ghf_branches_low_productive_list = []

gf_branches_high_productive_list = []
gf_branches_low_productive_list = []

activity = 0
total_count = len(os.listdir(address_folder))

""" *********************************************** Mono Repository ************************************************ """
for each_file in os.listdir(address_folder):
    count += 1
    print(total_count - count)

    low = 0
    high = 0

    if '.json' in each_file:
        branch_list = []
        # print(each_file)
        with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            for each_branch in file_content['branches']:
                if 'github' not in each_branch['name']:
                    branch_list.append(each_branch['name'])

            if file_content['Branching strategy'] == 'Github Flow' and file_content['Productivity'] == 'High':
                ghf_branches_high_productive_list.append(len(branch_list))

            elif file_content['Branching strategy'] == 'Github Flow' and file_content['Productivity'] == 'Low':
                ghf_branches_low_productive_list.append(len(branch_list))

            elif file_content['Branching strategy'] == 'GitFlow' and file_content['Productivity'] == 'High':
                gf_branches_high_productive_list.append(len(branch_list))

            elif file_content['Branching strategy'] == 'GitFlow' and file_content['Productivity'] == 'Low':
                gf_branches_low_productive_list.append(len(branch_list))

                if 1 < len(branch_list) < 6:
                    zero_five += 1
                elif 5 < len(branch_list) < 11:
                    six_ten += 1
                elif 10 < len(branch_list) < 26:
                    eleven_25 += 1
                elif 25 < len(branch_list) < 51:
                    twentysix_50 += 1
                elif 50 < len(branch_list):
                    more_50 += 1


""" *********************************************** Multi Repository (Frontend) ************************************ """
# for each_file in os.listdir(address_folder):
#     count += 1
#     print(total_count - count)
#
#     low = 0
#     high = 0
#
#     if '.json' in each_file:
#         branch_list = []
#         # print(each_file)
#         with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             for each_branch in file_content['Back Repositories']['branches']:
#                 if 'github' not in each_branch['name']:
#                     branch_list.append(each_branch['name'])
#
#             if file_content['Back Repositories']['Branching strategy'] == 'Github Flow' and file_content['Back Repositories']['Productivity'] == 'High':
#                 ghf_branches_high_productive_list.append(len(branch_list))
#
#             elif file_content['Back Repositories']['Branching strategy'] == 'Github Flow' and file_content['Back Repositories']['Productivity'] == 'Low':
#                 ghf_branches_low_productive_list.append(len(branch_list))
#
#             elif file_content['Back Repositories']['Branching strategy'] == 'GitFlow' and file_content['Back Repositories']['Productivity'] == 'High':
#                 gf_branches_high_productive_list.append(len(branch_list))
#
#             elif file_content['Back Repositories']['Branching strategy'] == 'GitFlow' and file_content['Back Repositories']['Productivity'] == 'Low':
#                 gf_branches_low_productive_list.append(len(branch_list))
#


print('Github Flow - High productivity branch count')
print(Counter(ghf_branches_high_productive_list))
print('Github Flow - Low productivity branch count')
print(Counter(ghf_branches_low_productive_list))

print('GitFlow - High productivity branch count')
print(Counter(gf_branches_high_productive_list))
print('GitFlow - Low productivity branch count')
print(Counter(gf_branches_low_productive_list))


Branch_count = {'zero_five': zero_five, 'six_ten': six_ten, 'eleven_25': eleven_25, 'twentysix_50': twentysix_50, 'more_50': more_50}
print(Branch_count)
























