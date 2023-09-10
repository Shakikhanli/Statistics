import json
import os
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

folder_mono = "E://Json files (Mono)/DB branching"
folder_multi = "E://Json files (Multi)/DB branching"

team_size = []
count = 0

one_developer = 0
two_developer = 0
three_five_developer = 0
five_ten_developer = 0
ten_25_developer = 0
more_developer = 0

three_ten_developer = 0

front_devs = []
back_devs = []
size = []

data = pd.DataFrame(
    columns=['Language', 'Team size'])

dict_list_mono = []
dict_list_multi = []
languages = []
languages_front = []
languages_back = []

""" ***************************************** Mono repository ***************************************** """
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

""" ***************************************** Multi repository ***************************************** """
# for each_file in os.listdir(folder_multi):
#     count += 1
#     print(len(os.listdir(folder_multi)) - count)
#     if '.json' in each_file:
#         with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#             contributors = []
#             for each_contributor in file_content['Front Repositories']['contributors']:
#                 contributors.append(each_contributor['contributor_name'])
#
#             for each_contributor in file_content['Back Repositories']['contributors']:
#                 contributors.append(each_contributor['contributor_name'])
#
#             contributors = list(dict.fromkeys(contributors))
#
#             size = len(contributors)
#
#             if size == 1:
#                 one_developer += 1
#             elif size == 2:
#                 two_developer += 1
#             elif 2 < size <= 5:
#                 three_five_developer += 1
#             elif 5 < size <= 10:
#                 five_ten_developer += 1
#             elif 10 < size <= 25:
#                 ten_25_developer += 1
#             elif size > 25:
#                 more_developer += 1

""" **************************************** Deep analysis (Multi repository) ************************** """
for each_file in os.listdir(folder_multi):

    count += 1
    print(len(os.listdir(folder_multi)) - count)
    # print(each_file)
    if '.json' in each_file:
        with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)
            contributors = []

            project_size = 0

            # if len(file_content['Front Repositories']['contributors']) > 2:

            dict1 = {'Project size': 0, 'Team size': 0}

            for each_contributor in file_content['Front Repositories']['contributors']:
                contributors.append(each_contributor['contributor_name'])
                project_size += file_content['Front Repositories']['size']

            for each_contributor in file_content['Back Repositories']['contributors']:
                contributors.append(each_contributor['contributor_name'])
                project_size += file_content['Back Repositories']['size']

            contributors = list(dict.fromkeys(contributors))
            project_size = project_size / 1000

            if 5 < len(contributors) < 50 and project_size < 2000 :

                dict1['Project size'] = project_size
                dict1['Team size'] = len(contributors)

                dict_list_multi.append(dict1)

                # languages_front.append(file_content['Front Repositories']['languages'])
                # languages_back.append(file_content['Back Repositories']['languages'])
    # if count > 1000:
    #     break

""" **************************************** Deep analysis (Mono repository) ************************** """

count = 0

for each_file in os.listdir(folder_mono):

    count += 1
    print(len(os.listdir(folder_mono)) - count)

    if '.json' in each_file:
        with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)
            contributors = []

            project_size = 0

            # if len(file_content['Front Repositories']['contributors']) > 2:

            dict1 = {'Project size': 0, 'Team size': 0}

            for each_contributor in file_content['contributors']:
                contributors.append(each_contributor['contributor_name'])
                project_size = file_content['size']

            contributors = list(dict.fromkeys(contributors))

            if 5 < len(contributors) < 50:
                # languages.append(file_content['languages'])
                project_size = project_size / 1000

                dict1['Project size'] = project_size
                dict1['Team size'] = len(contributors)
                dict_list_mono.append(dict1)
    # if count > 1000:
    #     break

""" ***************************************** Mono repository (Branching vs Team size) ***************************************** """
# one_developer_1 = 0
# two_developer_1 = 0
# three_ten_developer_1 = 0
# more_developer_1 = 0
#
# one_developer_2 = 0
# two_developer_2 = 0
# three_ten_developer_2 = 0
# more_developer_2 = 0
#
# one_developer_3 = 0
# two_developer_3 = 0
# three_ten_developer_3 = 0
# more_developer_3 = 0
#
#
# for each_file in os.listdir(folder_mono):
#     count += 1
#     print(len(os.listdir(folder_mono)) - count)
#     if '.json' in each_file:
#         with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#             # team_size.append(len(file_content['contributors']))
#
#             if len(file_content['commits']) > 2 and file_content['Branching strategy'] == 'Trunk-Based':
#                 size = len(file_content['contributors'])
#
#                 if size == 1:
#                     one_developer_1 += 1
#                 elif size == 2:
#                     two_developer_1 += 1
#                 elif 2 < size <= 10:
#                     three_ten_developer_1 += 1
#                 elif 10 < size:
#                     more_developer_1 += 1
#
#             elif len(file_content['commits']) > 2 and file_content['Branching strategy'] == 'GitFlow':
#                 size = len(file_content['contributors'])
#
#                 if size == 1:
#                     one_developer_2 += 1
#                 elif size == 2:
#                     two_developer_2 += 1
#                 elif 2 < size <= 10:
#                     three_ten_developer_2 += 1
#                 elif 10 < size:
#                     more_developer_2 += 1
#
#             elif len(file_content['commits']) > 2 and file_content['Branching strategy'] == 'Github Flow':
#                 size = len(file_content['contributors'])
#
#                 if size == 1:
#                     one_developer_3 += 1
#                 elif size == 2:
#                     two_developer_3 += 1
#                 elif 2 < size <= 10:
#                     three_ten_developer_3 += 1
#                 elif 10 < size:
#                     more_developer_3 += 1
#
#
# print('Trunk-Based: ')
# print(one_developer_1, two_developer_1, three_ten_developer_1, more_developer_1)
# print('Github Flow: ')
# print(one_developer_3, two_developer_3, three_ten_developer_3, more_developer_3)
# print('GitFlow: ')
# print(one_developer_2, two_developer_2, three_ten_developer_2, more_developer_2)
#
#
#

""" ***************************************** Mono repository (Languages) ***************************************** """
# one_developer_1 = 0
# two_developer_1 = 0
# three_ten_developer_1 = 0
# more_developer_1 = 0
#
# one_developer_2 = 0
# two_developer_2 = 0
# three_ten_developer_2 = 0
# more_developer_2 = 0
#
# one_developer_3 = 0
# two_developer_3 = 0
# three_ten_developer_3 = 0
# more_developer_3 = 0

# for each_file in os.listdir(folder_mono):
#     count += 1
#     print(len(os.listdir(folder_mono)) - count)
#     if '.json' in each_file:
#         with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#             contributors = []
#
#             for each_contributor in file_content['contributors']:
#                 contributors.append(each_contributor['contributor_name'])
#
#             contributors = list(dict.fromkeys(contributors))
#
#             if file_content['languages'] == 'Ruby':
#                 size = len(file_content['contributors'])
#
#                 if size == 1:
#                     one_developer_1 += 1
#                 elif size == 2:
#                     two_developer_1 += 1
#                 elif 2 < size <= 10:
#                     three_ten_developer_1 += 1
#                 elif 10 < size:
#                     more_developer_1 += 1
#
#             # elif file_content['languages'] == 'TypeScript':
#     size = len(file_content['contributors'])
#
#     if size == 1:
#         one_developer_2 += 1
#     elif size == 2:
#         two_developer_2 += 1
#     elif 2 < size <= 10:
#         three_ten_developer_2 += 1
#     elif 10 < size:
#         more_developer_2 += 1
#
# elif file_content['languages'] == 'Python':
#     size = len(file_content['contributors'])
#
#     if size == 1:
#         one_developer_3 += 1
#     elif size == 2:
#         two_developer_3 += 1
#     elif 2 < size <= 10:
#         three_ten_developer_3 += 1
#     elif 10 < size:
#         more_developer_3 += 1


# print('Ruby: ')
# print(one_developer_1, two_developer_1, three_ten_developer_1, more_developer_1)
# print('TypeScript: ')
# print(one_developer_3, two_developer_3, three_ten_developer_3, more_developer_3)
# print('Python: ')
# print(one_developer_2, two_developer_2, three_ten_developer_2, more_developer_2)
#

""" **************************************** Double Scatter plot ******************************************** """
# df_mono = pd.DataFrame.from_records(dict_list_mono)
# df_multi = pd.DataFrame.from_records(dict_list_multi)
#
# sorted_df_mono = df_mono.sort_values('Project size')
# sorted_df_multi = df_multi.sort_values('Project size')
#
# # correlation = sorted_df['Team size'].corr(sorted_df['Project size'])
#
# # print(f"Correlation between columns Team size and Language: {correlation}")
#
# # Create the scatter plot
# plt.scatter(sorted_df_mono['Project size'], sorted_df_mono['Team size'], label='Mono repository projects', s=10)
# plt.scatter(sorted_df_multi['Project size'], sorted_df_multi['Team size'], label='Multi repository projects', s=10)
#
# # Set labels and title
# plt.xlabel('Project size')
# plt.ylabel('Team size')
# # plt.title('Scatter Plot of Two')
#
# # Add legend
# plt.legend()
#
# # Show the plot
# plt.show()

""" **************************************** Double Scatter plot (Linear regression) ******************************************** """

df_mono = pd.DataFrame.from_records(dict_list_mono)
df_multi = pd.DataFrame.from_records(dict_list_multi)

sorted_df_mono = df_mono.sort_values('Project size')
sorted_df_multi = df_multi.sort_values('Project size')

# Scatter plot data for sorted_df_mono
x_mono = sorted_df_mono['Project size']
y_mono = sorted_df_mono['Team size']

# Scatter plot data for sorted_df_multi
x_multi = sorted_df_multi['Project size']
y_multi = sorted_df_multi['Team size']

# Perform linear regression for sorted_df_mono
slope_mono, intercept_mono, r_value_mono, p_value_mono, std_err_mono = linregress(x_mono, y_mono)
line_mono = slope_mono * np.array(x_mono) + intercept_mono

# Perform linear regression for sorted_df_multi
slope_multi, intercept_multi, r_value_multi, p_value_multi, std_err_multi = linregress(x_multi, y_multi)
line_multi = slope_multi * np.array(x_multi) + intercept_multi

# Create the scatter plot
plt.scatter(x_mono, y_mono, label='Mono repository projects', s=10)
plt.scatter(x_multi, y_multi, label='Multi repository projects', s=10)

# Plot linear regression lines
plt.plot(x_mono, line_mono, color='green', label='Linear regression (Mono)')
plt.plot(x_multi, line_multi, color='red', label='Linear regression (Multi)')

# Set labels and title
plt.xlabel('Project size')
plt.ylabel('Team size')
plt.title('Scatter Plot with Linear Regression')

# Add legend
plt.legend()

# Show the plot
plt.show()





# print('1 developer: %d' % one_developer)
# print('2 developer: %d' % two_developer)
# print('3-5 developer: %d' % three_five_developer)
# print('5-10 developer: %d' % five_ten_developer)
# print('10-25 developer: %d' % ten_25_developer)
# print('More developer: %d' % more_developer)
