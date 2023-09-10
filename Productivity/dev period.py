import json
import os
from collections import Counter
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

folder_mono = "E://Json files (Mono)/Productivity"
folder_multi = "E://Json files (Multi)/Productivity"


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
    columns=['Development period', 'Team size', 'Productivity'])

dict_list = []
languages = []
dict_list_mono = []
dict_list_multi = []


""" ****************************** Mono Repository ***************************************"""
for each_file in os.listdir(folder_mono):
    count += 1
    #
    print(len(os.listdir(folder_mono)) - count)
    if '.json' in each_file:
        with open(folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            start = datetime.fromisoformat(file_content['created_at'][:-1])
            end = datetime.fromisoformat(file_content['last_update'][:-1])

            delta = end - start
            dev_period.append(delta.days)

            if (file_content['Productivity'] == 'Low' or file_content['Productivity'] == 'High') and (0 < len(file_content['contributors']) < 50) \
                    and file_content['Branching strategy'] == 'Github Flow':
                dict1 = {'Development period': delta.days, 'Team size': len(file_content['contributors']), 'Productivity': file_content['Productivity']}
                dict_list.append(dict1)
                dict_list_mono.append(dict1)

""" ****************************** Multi Repository (frontend) ***************************************"""
# for each_file in os.listdir(folder_multi):
#     count += 1
#     #
#     print(len(os.listdir(folder_multi)) - count)
#     if '.json' in each_file:
#         with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             start = datetime.fromisoformat(file_content['Front Repositories']['created_at'][:-1])
#             end = datetime.fromisoformat(file_content['Front Repositories']['last_update'][:-1])
#
#             delta = end - start
#             dev_period.append(delta.days)
#
#             if (file_content['Front Repositories']['Productivity'] == 'Low' or file_content['Front Repositories']['Productivity'] == 'High') \
#                     and (len(file_content['Front Repositories']['contributors']) < 35) and (delta.days < 2500):
#                 dict1 = {'Development period': delta.days, 'Team size': len(file_content['Front Repositories']['contributors']),
#                          'Productivity': file_content['Front Repositories']['Productivity']}
#                 dict_list.append(dict1)
#                 dict_list_mono.append(dict1)

""" ****************************** Multi Repository (backend) ***************************************"""
# for each_file in os.listdir(folder_multi):
#     count += 1
#     #
#     print(len(os.listdir(folder_multi)) - count)
#     if '.json' in each_file:
#         with open(folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             start = datetime.fromisoformat(file_content['Back Repositories']['created_at'][:-1])
#             end = datetime.fromisoformat(file_content['Back Repositories']['last_update'][:-1])
#
#             delta = end - start
#             dev_period.append(delta.days)
#
#             if (file_content['Back Repositories']['Productivity'] == 'Low' or file_content['Back Repositories']['Productivity'] == 'High') \
#                     and (len(file_content['Back Repositories']['contributors']) < 35) and (delta.days < 2500):
#                 dict1 = {'Development period': delta.days, 'Team size': len(file_content['Back Repositories']['contributors']),
#                          'Productivity': file_content['Back Repositories']['Productivity']}
#                 dict_list.append(dict1)
#                 dict_list_mono.append(dict1)

data = dict_list_mono

# Extracting values of A, C, and B from the data
values_of_A = [d["Development period"] for d in data]
values_of_C = [d["Team size"] for d in data]
values_of_B = [d["Productivity"] for d in data]

# Create a colormap for "B" values
colors = {"Low": "red", "High": "blue"}
dot_colors = [colors[b] for b in values_of_B]

# Set up the scatter plot
plt.scatter(values_of_A, values_of_C, c=dot_colors, edgecolors="black", s=25)

# Set the x-axis and y-axis labels, and the title
plt.xlabel('Development period')
plt.ylabel('Team size')
plt.title('Scatter Plot of Development period and Team size with different productivity values (Github Flow)')

# Add a legend
legend_colors = [plt.scatter([], [], c=colors[b], edgecolors="black", s=100, label=b) for b in colors]
plt.legend(handles=legend_colors, title="Productivity", loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()










