import json
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Trunk based = only 1 branch
Github Flow = master and feature branches
GitFlow = master, develop and feature branches
"""

# address_folder = "E://Json files (Mono)/Productivity"
# external_folder = "E://Json files (Mono)/DB branching"

address_folder = "E://Json files (Multi)/New Database"
external_folder = "E://Json files (Multi)/DB branching"


def define_branch_strategy_gitFlow(branch_list):
    master = False
    dev = False
    if 'master' in branch_list or 'main' in branch_list:
        master = True

    for each_branch in branch_list:
        if 'dev' in each_branch:
            dev = True
            break

    if dev and master:
        return True
    else:
        return False


mono_count = 0
double_count = 0
triple_count = 0
count = 0

total_count = len(os.listdir(address_folder))

errors = []

''' ********************* Mono Repository ********************************* '''
# for each_file in os.listdir(address_folder):
#     count += 1
#
#     print(total_count - count)
#
#     if '.json' in each_file:
#         with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             branch_list = []
#
#             for each_branch in file_content['branches']:
#                 if 'dependabot' not in each_branch['name']:
#                     branch_list.append(each_branch['name'])
#
#             try:
#                 if len(branch_list) == 1:
#                     mono_count += 1
#                     file_content['Branching strategy'] = 'Trunk-Based'
#
#                 elif len(branch_list) >= 2 and define_branch_strategy_gitFlow(branch_list):
#                     triple_count += 1
#                     file_content['Branching strategy'] = 'GitFlow'
#
#                 elif not define_branch_strategy_gitFlow(branch_list) and len(branch_list) > 1:
#                     double_count += 1
#                     file_content['Branching strategy'] = 'Github Flow'
#
#                 elif len(branch_list) == 0:
#                     file_content['Branching strategy'] = 'None'
#
#                 if file_content['Branching strategy']:
#                     json_data = json.dumps(file_content)
#                     jsonFile = open(external_folder + '/' + each_file, "w")
#                     jsonFile.write(json_data)
#                     jsonFile.close()

#             except Exception as error:
#                 print(error)
#                 errors.append(each_file)
#
#
# print(errors)
# print(len(errors))

''' ********************* Multi Repository ********************************* '''
for each_file in os.listdir(address_folder):
    count += 1

    print(total_count - count)

    if '.json' in each_file:
        with open(address_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            branch_list_front = []
            branch_list_back = []

            try:
                for each_branch in file_content['Front Repositories']['branches']:
                    if 'dependabot' not in each_branch['name']:
                        branch_list_front.append(each_branch['name'])

                if len(branch_list_front) == 1:
                    mono_count += 1
                    file_content['Front Repositories']['Branching strategy'] = 'Trunk-Based'

                elif len(branch_list_front) >= 2 and define_branch_strategy_gitFlow(branch_list_front):
                    triple_count += 1
                    file_content['Front Repositories']['Branching strategy'] = 'GitFlow'

                elif not define_branch_strategy_gitFlow(branch_list_front) and len(branch_list_front) > 1:
                    double_count += 1
                    file_content['Front Repositories']['Branching strategy'] = 'Github Flow'

                elif len(branch_list_front) == 0:
                    file_content['Front Repositories']['Branching strategy'] = 'None'

                # *******************************************************************************************

                for each_branch in file_content['Back Repositories']['branches']:
                    if 'dependabot' not in each_branch['name']:
                        branch_list_back.append(each_branch['name'])

                if len(branch_list_back) == 1:
                    mono_count += 1
                    file_content['Back Repositories']['Branching strategy'] = 'Trunk-Based'

                elif len(branch_list_back) >= 2 and define_branch_strategy_gitFlow(branch_list_back):
                    triple_count += 1
                    file_content['Back Repositories']['Branching strategy'] = 'GitFlow'

                elif not define_branch_strategy_gitFlow(branch_list_back) and len(branch_list_back) > 1:
                    double_count += 1
                    file_content['Back Repositories']['Branching strategy'] = 'Github Flow'

                elif len(branch_list_back) == 0:
                    file_content['Back Repositories']['Branching strategy'] = 'None'

                json_data = json.dumps(file_content)
                jsonFile = open(external_folder + '/' + each_file, "w")
                jsonFile.write(json_data)
                jsonFile.close()

            except Exception as error:
                print(error)
                print(each_file)
                continue

