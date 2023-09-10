import json
import os
from collections import Counter
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

folder_mono = "E://Json files (Mono)/DB branching"
folder_multi = "E://Json files (Multi)/DB branching"


count = 0

dev_period = []

a_week = 0
a_month = 0
three_month = 0
six_month = 0
nine_month = 0
a_year = 0
two_years = 0
more_than_2_years = 0

more_50 = 0

data = pd.DataFrame(
    columns=['Development period', 'Team size'])

dict_list = []
languages = []
dict_list_mono = []
dict_list_multi = []

""" ****************************** Mono Repository ***************************************"""
# for each_file in os.listdir(folder_mono):
#     count += 1
#     print(len(os.listdir(folder_mono)) - count)
#     if '.json' in each_file:
#         with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             start = datetime.fromisoformat(file_content['created_at'][:-1])
#             end = datetime.fromisoformat(file_content['last_update'][:-1])
#
#             delta = end - start
#             dev_period.append(delta.days)
#
#             if delta.days < 7:
#                 a_week += 1
#             elif 7 < delta.days < 31:
#                 a_month += 1
#             elif 30 < delta.days < 90:
#                 three_month += 1
#             elif 90 < delta.days < 120:
#                 six_month += 1
#             elif 120 < delta.days < 180:
#                 nine_month += 1
#             elif 180 < delta.days < 365:
#                 a_year += 1
#             elif 365 < delta.days < 730:
#                 two_years += 1
#             elif delta.days > 730:
#                 more_than_2_years += 1

""" ****************************** Multi Repository ***************************************"""
# for each_file in os.listdir(folder_multi):
#     count += 1
#     print(len(os.listdir(folder_multi)) - count)
#     if '.json' in each_file:
#         with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             start1 = datetime.fromisoformat(file_content['Front Repositories']['created_at'][:-1])
#             start2 = datetime.fromisoformat(file_content['Back Repositories']['created_at'][:-1])
#
#             end1 = datetime.fromisoformat(file_content['Front Repositories']['last_update'][:-1])
#             end2 = datetime.fromisoformat(file_content['Back Repositories']['last_update'][:-1])
#
#             if start1 < start2:
#                 start = start1
#             else:
#                 start = start2
#
#             if end1 > end2:
#                 end = end1
#             else:
#                 end = end2
#
#             delta = end - start
#             dev_period.append(delta.days)
#
#             if delta.days < 7:
#                 a_week += 1
#             elif 7 < delta.days < 31:
#                 a_month += 1
#             elif 30 < delta.days < 90:
#                 three_month += 1
#             elif 90 < delta.days < 120:
#                 six_month += 1
#             elif 120 < delta.days < 180:
#                 nine_month += 1
#             elif 180 < delta.days < 365:
#                 a_year += 1
#             elif 365 < delta.days < 730:
#                 two_years += 1
#             elif delta.days > 730:
#                 more_than_2_years += 1

""" ****************************** Mono Repository (Deep analyses) ***************************************"""
for each_file in os.listdir(folder_mono):
    count += 1
    print(len(os.listdir(folder_mono)) - count)
    if '.json' in each_file:
        with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            start = datetime.fromisoformat(file_content['created_at'][:-1])
            end = datetime.fromisoformat(file_content['last_update'][:-1])

            delta = end - start
            contributors = []

            for each_contributor in file_content['contributors']:
                contributors.append(each_contributor['contributor_name'])

            if 2 < len(contributors) < 50 and delta.days < 2500:

                dict1 = {'Development period': delta.days, 'Team size': len(contributors)}
                dict_list.append(dict1)
                dict_list_mono.append(dict1)

""" ****************************** Multi Repository (Deep analyses) ***************************************"""
count = 0
for each_file in os.listdir(folder_multi):
    count += 1
    print(len(os.listdir(folder_multi)) - count)
    if '.json' in each_file:
        with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            contributors = []

            start1 = datetime.fromisoformat(file_content['Front Repositories']['created_at'][:-1])
            start2 = datetime.fromisoformat(file_content['Back Repositories']['created_at'][:-1])

            end1 = datetime.fromisoformat(file_content['Front Repositories']['last_update'][:-1])
            end2 = datetime.fromisoformat(file_content['Back Repositories']['last_update'][:-1])

            if start1 < start2:
                start = start1
            else:
                start = start2

            if end1 > end2:
                end = end1
            else:
                end = end2

            delta = end - start

            for each_contributor in file_content['Front Repositories']['contributors']:
                contributors.append(each_contributor['contributor_name'])

            for each_contributor in file_content['Back Repositories']['contributors']:
                contributors.append(each_contributor['contributor_name'])

            contributors = list(dict.fromkeys(contributors))

            if 2 < len(contributors) < 50 and delta.days < 2500:

                dict1 = {'Development period': delta.days, 'Team size': len(contributors)}
                dict_list.append(dict1)

                dict_list_multi.append(dict1)

""" ******************************************** Simple chart **************************************"""
# df = pd.DataFrame.from_records(dict_list)
# print(df.head(10))
#
# sorted_df = df.sort_values('Development period')
# print(sorted_df.head(10))
#
# correlation = sorted_df['Team size'].corr(sorted_df['Development period'])
# print(f"Correlation between columns Development period and Team size: {correlation}")
#
# # Create a line chart
# plt.scatter(sorted_df['Development period'], sorted_df['Team size'])
#
# # Set the chart title and labels
# plt.xlabel('Development period')
# plt.ylabel('Team size')
#
# # Display the chart
# plt.show()

# print(Counter(dev_period))
#
# print(a_week)
# print(a_month)
# print(three_month)
# print(six_month)
# print(nine_month)
# print(a_year)
# print(two_years)
# print(more_than_2_years)

""" ******************************************** Double chart ***************************************"""
# df_mono = pd.DataFrame.from_records(dict_list_mono)
# df_multi = pd.DataFrame.from_records(dict_list_multi)
#
# sorted_df_mono = df_mono.sort_values('Development period')
# sorted_df_multi = df_multi.sort_values('Development period')
#
# # Create the scatter plot
# plt.scatter(sorted_df_mono['Development period'], sorted_df_mono['Team size'], label='Mono repository projects', s=10)
# plt.scatter(sorted_df_multi['Development period'], sorted_df_multi['Team size'], label='Multi repository projects', s=10)
#
# # Set labels and title
# plt.xlabel('Development period')
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

sorted_df_mono = df_mono.sort_values('Development period')
sorted_df_multi = df_multi.sort_values('Development period')

# Scatter plot data for sorted_df_mono
x_mono = sorted_df_mono['Development period']
y_mono = sorted_df_mono['Team size']

# Scatter plot data for sorted_df_multi
x_multi = sorted_df_multi['Development period']
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
plt.xlabel('Development period')
plt.ylabel('Team size')
plt.title('Scatter Plot with Linear Regression')

# Add legend
plt.legend()

# Show the plot
plt.show()















