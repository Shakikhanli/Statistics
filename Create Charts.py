from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd

# Creating dataset
data_mono_team_size = {'Single developer': 19348, '2 developers': 1965, '3-10 developers': 1100, '< 10 developers': 195}
data_multi_team_size = {'Single developer': 4991, '2 developers': 1368, '3-10 developers': 1567, '< 10 developers': 130}

data_mono_language = {'JavaScript': 16398, 'TypeScript': 4562, 'HTML-CSS': 6399, 'Java': 2330,
                      'Python': 1739, 'PHP': 941, 'Vue-Ruby': 1108, 'C':  50}
data_multi_front_language = {'JavaScript': 3892, 'TypeScript': 2460, 'Vue-Ruby': 690, 'HTML-CSS': 914,
                             'Java': 131, 'PHP': 65, 'Python': 38, 'Dart': 33, 'C': 30}

data_multi_back_language = {'JavaScript': 3194, 'TypeScript': 1602, 'Vue-Ruby': 355, 'HTML-CSS': 350,
                            'Java': 1431, 'PHP': 339, 'Python': 862, 'Go': 128, 'C': 75}

data_multi_front_back_language = {'JavaScript//JavaScript': 2141, 'TypeScript//TypeScript': 1115,
                                  'TypeScript//Java': 528,
                                  'JavaScript//Java': 481, 'JavaScript//Python': 433, 'TypeScript//JavaScript': 381,
                                  'JavaScript//Ruby': 259, 'JavaScript//TypeScript': 251, 'Vue//JavaScript': 239,
                                  'CSS//JavaScript': 177, 'HTML//JavaScript': 157, 'TypeScript//Python': 142,
                                  'Vue//Python': 118,
                                  'Vue//Java': 116, 'TypeScript//HTML': 108, 'JavaScript//PHP': 105, 'HTML//Java': 96,
                                  'CSS//TypeScript': 83, 'Java//Java': 76}

data_mono_dev_period = {'< 1 month': 8010, '1-3 months': 3262, '3-6 months': 804, '6-9 months': 949,
                        '9-12 months': 1738, '12-24 months': 1290, '> 24 months': 1230}

data_multi_dev_period = {'< 1 month': 3367, '1-3 months': 1344, '3-6 months': 403, '6-9 months': 512,
                         '9-12 months': 1001, '12-24 months': 1012, '> 24 months': 693}

data_mono_branching_strategy = {'Trunk-Based': 13350, 'Github Flow': 3315, 'GitFlow': 828}
data_multi_front_branching_strategy = {'Trunk-Based': 3464, 'Github Flow': 1654, 'GitFlow': 893}
data_multi_back_branching_strategy = {'Trunk-Based': 3705, 'Github Flow': 1478, 'GitFlow': 918}

''' ********************* Pie chart ********************************* '''
# fig, ax = plt.subplots()
# ax.pie(data_mono, labels=developers2, autopct='%1.1f%%', startangle=90)
#
# # Display the chart
# ax.axis('equal')
# plt.show()

''' ********************* Bar chart ******************************** '''
# total = sum(data_mono_language)
# percentages = [size / total * 100 for size in data_mono_language]
#
# # Create bar chart
# fig, ax = plt.subplots()
# ax.bar(languages, percentages)
#
# # Add percentage labels to bars
# for i, v in enumerate(percentages):
#     ax.text(i, v + 1, f'{v:.1f}%', ha='center')
#
# # Set axis labels and title
# ax.set_xlabel('Lnaguages')
# ax.set_ylabel('Percentage')
#
# # Show chart
# plt.show()

''' ********************* Bar chart (Dictionary) ******************************** '''
# total = sum(data_mono_dev_period.values())
#
# # calculate percentages
# percentages = [100 * value / total for value in data_mono_dev_period.values()]
#
# bars = plt.bar(data_mono_dev_period.keys(), percentages)
#
# # add labels and title
# plt.xlabel('Programming language')
# plt.ylabel('Percentage')
#
# # add percentages on top of bars
# for i, bar in enumerate(bars):
#     plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
#              f"{percentages[i]:.2f}%", ha='center', va='bottom')
#
# # plt.xticks(rotation=15, ha='right')
#
# plt.show()

''' ********************* Double Bar chart (Dictionary) ******************************** '''

# total1 = sum(data_mono_team_size.values())
# total2 = sum(data_multi_team_size.values())
#
# percent1 = [100*value/total1 for value in data_mono_team_size.values()]
# percent2 = [100*value/total2 for value in data_multi_team_size.values()]
#
# # Set the width of the bars
# barWidth = 0.35
#
# # Set the x positions of the bars
# r1 = range(len(percent1))
# r2 = [x + barWidth for x in r1]
#
# # Create the double bar chart
# plt.bar(r1, percent1, width=barWidth, edgecolor='white', label='Mono Repository')
# plt.bar(r2, percent2, width=barWidth, edgecolor='white', label='Multi Repository')
#
# # Format the y-axis tick labels as percentages
# plt.gca().set_yticklabels(['{:.0f}%'.format(y) for y in plt.gca().get_yticks()])
#
# # Add percentage values on top of each bar
# for i, value in enumerate(percent1):
#     plt.text(i, value+2, '{:.0f}%'.format(value), ha='center', va='bottom')
# for i, value in enumerate(percent2):
#     plt.text(i+barWidth, value+2, '{:.0f}%'.format(value), ha='center', va='bottom')
#
# plt.xticks([r + barWidth/2 for r in range(len(percent1))], data_mono_team_size.keys())
#
# # Add a legend
# plt.legend()
#
# # Show the chart
# plt.show()


''' ********************* Pie chart (Dictionary) ********************************* '''

# labels = list(data_mono_branching_strategy.keys())
# values = list(data_mono_branching_strategy.values())
#
# # Create a pie chart with the labels and values
# plt.pie(values, labels=labels, autopct='%1.1f%%')
#
# # Add a title to the chart
# # plt.title('Branching Strategies in Mono Repository structure')
#
# # Show the chart
# plt.show()

""" ****************************** Double Pie Charts (Dictionary) **********************************************"""

# # Create a figure with two subplots
# fig, (ax1, ax2) = plt.subplots(1, 2)
#
# # Set the title for the chart
# # fig.suptitle('Two Pie Charts')
#
# # Plot the first pie chart in the first subplot
# ax1.pie(data_multi_front_branching_strategy.values(), labels=data_multi_front_branching_strategy.keys(), autopct='%1.1f%%')
# ax1.set_title('Frontend Repositories')
#
# # Plot the second pie chart in the second subplot
# ax2.pie(data_multi_back_branching_strategy.values(), labels=data_multi_back_branching_strategy.keys(), autopct='%1.1f%%')
# ax2.set_title('Backend Repositories')
#
# # Show the chart
# plt.show()

""" ****************************** Corralation *************************************************************"""
# mono_repo_data = {
#     '1 developer': 85.6,
#     '2 developers': 8.7,
#     '3-10 developers': 4.9,
#     'More than 10 developers': 0.9
# }
#
# # Data for Multi Repository
# multi_repo_data = {
#     '1 developer': 62,
#     '2 developers': 17,
#     '3-10 developers': 19.5,
#     'More than 10 developers': 1.6
# }
#
# # Create a figure and axis
# fig, ax = plt.subplots()
#
# # Plotting the data
# mono_repo_bars = ax.bar(mono_repo_data.keys(), mono_repo_data.values(), label='Mono Repository')
# multi_repo_bars = ax.bar(multi_repo_data.keys(), multi_repo_data.values(), label='Multi Repository')
#
# # Adding labels and title
# ax.set_xlabel('Team Size')
# ax.set_ylabel('Percentage')
# ax.set_title('Team Size Distribution in Mono Repository and Multi Repository Projects')
#
# # Adding a legend
# ax.legend()
#
# # Displaying the chart
# plt.show()
#

""" ****************************** Language usage all together *************************************************************"""
#

""" ****************************** Corralation (Mono Multi together) *************************************************************"""


















