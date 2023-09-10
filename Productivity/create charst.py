import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

""" ****************************************** General Statistics ************************************************** """

# # Mono Repository Statistics
# mono_high_productive_count = 1923
# mono_low_productive_count = 3958
# mono_non_productive_count = 27000
#
# # Multi Repository (Front) Statistics
# multi_front_high_productive_count = 1150
# multi_front_low_productive_count = 1893
# multi_front_non_productive_count = 4875
#
# # Multi Repository (Back) Statistics
# multi_back_high_productive_count = 1115
# multi_back_low_productive_count = 2100
# multi_back_non_productive_count = 5000
#
# # Calculate percentages
# total_mono_projects = mono_high_productive_count + mono_low_productive_count + mono_non_productive_count
# total_multi_front_projects = multi_front_high_productive_count + multi_front_low_productive_count + multi_front_non_productive_count
# total_multi_back_projects = multi_back_high_productive_count + multi_back_low_productive_count + multi_back_non_productive_count
#
# mono_high_productive_percent = (mono_high_productive_count / total_mono_projects) * 100
# mono_low_productive_percent = (mono_low_productive_count / total_mono_projects) * 100
# mono_non_productive_percent = (mono_non_productive_count / total_mono_projects) * 100
#
# multi_front_high_productive_percent = (multi_front_high_productive_count / total_multi_front_projects) * 100
# multi_front_low_productive_percent = (multi_front_low_productive_count / total_multi_front_projects) * 100
# multi_front_non_productive_percent = (multi_front_non_productive_count / total_multi_front_projects) * 100
#
# multi_back_high_productive_percent = (multi_back_high_productive_count / total_multi_back_projects) * 100
# multi_back_low_productive_percent = (multi_back_low_productive_count / total_multi_back_projects) * 100
# multi_back_non_productive_percent = (multi_back_non_productive_count / total_multi_back_projects) * 100
#
# # Create bar chart for Mono Repository projects
# mono_labels = ['High', 'Low', 'Non']
# mono_values = [mono_high_productive_percent, mono_low_productive_percent, mono_non_productive_percent]
#
# plt.subplot(1, 3, 1)
# bars = plt.bar(mono_labels, mono_values)
# plt.title('Mono Repository Projects')
# plt.xlabel('Productivity Type')
# plt.ylabel('Percentage')
#
# # Add percentage labels on top of each bar
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom')
#
# # Create bar chart for Multi Repository (Front) projects
# multi_front_labels = ['High', 'Low', 'Non']
# multi_front_values = [multi_front_high_productive_percent, multi_front_low_productive_percent, multi_front_non_productive_percent]
#
# plt.subplot(1, 3, 2)
# bars = plt.bar(multi_front_labels, multi_front_values)
# plt.title('Multi Repository (Front) Projects')
# plt.xlabel('Productivity Type')
# plt.ylabel('Percentage')
#
# # Add percentage labels on top of each bar
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom')
#
# # Create bar chart for Multi Repository (Back) projects
# multi_back_labels = ['High', 'Low', 'Non']
# multi_back_values = [multi_back_high_productive_percent, multi_back_low_productive_percent, multi_back_non_productive_percent]
#
# plt.subplot(1, 3, 3)
# bars = plt.bar(multi_back_labels, multi_back_values)
# plt.title('Multi Repository (Back) Projects')
# plt.xlabel('Productivity Type')
# plt.ylabel('Percentage')
#
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom')
#
# plt.tight_layout()
# plt.show()

""" ***************************************** Branching strategies (Mono Repository) ******************************* """
# Mono Repository Workflow Statistics
# mono_high_productive = {'Trunk-Based': 142, 'Github Flow': 196, 'GitFlow': 90}
# mono_low_productive = {'Trunk-Based': 1203, 'Github Flow': 594, 'GitFlow': 161}
# mono_non_productive = {'Trunk-Based': 26611, 'Github Flow': 3755, 'GitFlow': 852}

# Multi Repository (Frontend) Workflow Statistics
# mono_high_productive = {'Trunk-Based': 60, 'Github Flow': 169, 'GitFlow': 144}
# mono_low_productive = {'Trunk-Based': 661, 'Github Flow': 547, 'GitFlow': 288}
# mono_non_productive = {'Trunk-Based': 4878, 'Github Flow': 1131, 'GitFlow': 601}

# Multi Repository (Backend) Workflow Statistics
# mono_high_productive = {'Trunk-Based': 56, 'Github Flow': 145, 'GitFlow': 114}
# mono_low_productive = {'Trunk-Based': 725, 'Github Flow': 500, 'GitFlow': 313}
# mono_non_productive = {'Trunk-Based': 5016, 'Github Flow': 1018, 'GitFlow': 591}


# Calculate total project count
# total_projects = sum(mono_high_productive.values()) + sum(mono_low_productive.values()) + sum(mono_non_productive.values())
#
# # Calculate percentages for each category
# high_productive_percent = [(val / total_projects) * 100 for val in mono_high_productive.values()]
# low_productive_percent = [(val / total_projects) * 100 for val in mono_low_productive.values()]
# non_productive_percent = [(val / total_projects) * 100 for val in mono_non_productive.values()]
#
# # Workflow types and colors
# workflow_types = list(mono_high_productive.keys())
# colors = ['lightblue', 'lightgreen', 'lightcoral']
#
# # Set the figure size
# plt.figure(figsize=(12, 4))
#
# # Pie chart for High Productive
# plt.subplot(1, 3, 1)
# plt.pie(high_productive_percent, labels=workflow_types, colors=colors, autopct='%1.1f%%')
# plt.title('High Productive')
# plt.axis('equal')
#
# # Pie chart for Low Productive
# plt.subplot(1, 3, 2)
# plt.pie(low_productive_percent, labels=workflow_types, colors=colors, autopct='%1.1f%%')
# plt.title('Low Productive')
# plt.axis('equal')
#
# # Pie chart for Non Productive
# plt.subplot(1, 3, 3)
# plt.pie(non_productive_percent, labels=workflow_types, colors=colors, autopct='%1.1f%%')
# plt.title('Non Productive')
# plt.axis('equal')
#
# # Adjusting the layout and displaying the chart
# plt.tight_layout()
# plt.show()

""" ***************************************** Languages in (Mono Repository) ******************************* """

# # Language distribution in High Productive
# high_productive = Counter({'JavaScript': 214, 'TypeScript': 80, 'HTML-CSS': 55, 'Java': 19, 'Python': 22, 'PHP': 16, 'Vue': 5, 'Ruby': 11})
#
# # Language distribution in Low Productive
# low_productive = Counter({'JavaScript': 1047, 'TypeScript': 327, 'HTML-CSS': 273, 'Java': 90, 'Python': 80, 'PHP': 51, 'Vue': 57, 'Ruby': 31})
#
# # Language distribution in Non Productive
# non_productive = Counter({'JavaScript': 15137, 'TypeScript': 4155, 'HTML-CSS': 6069, 'Java': 2221, 'Python': 1637, 'PHP': 874, 'Vue': 510, 'Ruby': 494})
#
# # Calculate total project count for each category
# total_high_productive = sum(high_productive.values())
# total_low_productive = sum(low_productive.values())
# total_non_productive = sum(non_productive.values())
#
# # Calculate percentages for each language in each category
# high_productive_percent = [(val / total_high_productive) * 100 for val in high_productive.values()]
# low_productive_percent = [(val / total_low_productive) * 100 for val in low_productive.values()]
# non_productive_percent = [(val / total_non_productive) * 100 for val in non_productive.values()]
#
# # Language names and colors
# languages = list(high_productive.keys())
# colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightsalmon', 'lightpink', 'lightskyblue', 'lightgray', 'lightgreen', 'lightseagreen']
#
# # Set the figure size
# plt.figure(figsize=(12, 4))
#
# # Pie chart for High Productive
# plt.subplot(1, 3, 1)
# plt.pie(high_productive_percent, labels=languages, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
# plt.title('Language Distribution in High Productive')
# plt.axis('equal')
#
# # Pie chart for Low Productive
# plt.subplot(1, 3, 2)
# plt.pie(low_productive_percent, labels=languages, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
# plt.title('Language Distribution in Low Productive')
# plt.axis('equal')
#
# # Pie chart for Non Productive
# plt.subplot(1, 3, 3)
# plt.pie(non_productive_percent, labels=languages, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
# plt.title('Language Distribution in Non Productive')
# plt.axis('equal')
#
# # Adjusting the layout and displaying the chart
# plt.tight_layout()
# plt.show()

""" ***************************************** Languages in Multi Repository (Frontend)******************************* """

# # Language distribution in High Productive
# high_productive = Counter({'JavaScript': 203, 'TypeScript': 105, 'Vue': 30, 'HTML-CSS': 21, 'Java': 5, 'Others': 6})
#
# # Language distribution in Low Productive
# low_productive = Counter({'JavaScript': 696, 'TypeScript': 453, 'Vue': 150, 'HTML-CSS': 133, 'Java': 16, 'Others': 24})
#
# # Language distribution in Non Productive
# non_productive = Counter({'JavaScript': 2993, 'TypeScript': 1902, 'Vue': 492, 'HTML-CSS': 760, 'Java': 110, 'Others': 141})
#
# # Calculate total project count for each category
# total_high_productive = sum(high_productive.values())
# total_low_productive = sum(low_productive.values())
# total_non_productive = sum(non_productive.values())
#
# # Calculate percentages for each language in each category
# high_productive_percent = [(val / total_high_productive) * 100 for val in high_productive.values()]
# low_productive_percent = [(val / total_low_productive) * 100 for val in low_productive.values()]
# non_productive_percent = [(val / total_non_productive) * 100 for val in non_productive.values()]
#
# # Language names and colors
# languages_high = list(high_productive.keys())
# languages_low = list(low_productive.keys())
# languages_non = list(non_productive.keys())
# colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightyellow', 'lightskyblue']
#
# # Set the figure size
# plt.figure(figsize=(12, 4))
#
# # Pie chart for High Productive
# plt.subplot(1, 3, 1)
# plt.pie(high_productive_percent, labels=languages_high, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 12})
# plt.title('Language Distribution in High Productive')
# plt.axis('equal')
#
# # Pie chart for Low Productive
# plt.subplot(1, 3, 2)
# plt.pie(low_productive_percent, labels=languages_low, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 12})
# plt.title('Language Distribution in Low Productive')
# plt.axis('equal')
#
# # Pie chart for Non Productive
# plt.subplot(1, 3, 3)
# plt.pie(non_productive_percent, labels=languages_non, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 12})
# plt.title('Language Distribution in Non Productive')
# plt.axis('equal')
#
# # Adjusting the layout and displaying the chart
# plt.tight_layout()
# plt.show()

""" ***************************************** Branch count in Mono Repository ************************************** """

# # Data for Github Flow - High productivity branch count
# high_productive = {'zero_five': 34, 'six_ten': 17, 'eleven_25': 19, 'twentysix_50': 8, 'more_50': 7}
# total_high_productive = sum(high_productive.values())
#
# # Data for Github Flow - Low productivity branch count
# low_productive = {'zero_five': 80, 'six_ten': 22, 'eleven_25': 27, 'twentysix_50': 18, 'more_50': 4}
# total_low_productive = sum(low_productive.values())
#
# # Calculate percentages for high productivity branches
# high_productive_percent = [count / total_high_productive * 100 for count in high_productive.values()]
#
# # Calculate percentages for low productivity branches
# low_productive_percent = [count / total_low_productive * 100 for count in low_productive.values()]
#
# # Categories and bar positions
# categories = list(high_productive.keys())
# bar_positions = np.arange(len(categories))
#
# # Set the figure size
# plt.figure(figsize=(10, 6))
#
# # Plotting the bars for high productivity branches
# plt.bar(bar_positions - 0.2, high_productive_percent, width=0.4, label='High Productivity', align='center')
#
# # Plotting the bars for low productivity branches
# plt.bar(bar_positions + 0.2, low_productive_percent, width=0.4, label='Low Productivity', align='center')
#
# # Adding data labels on top of each bar
# for i in range(len(categories)):
#     plt.text(bar_positions[i] - 0.2, high_productive_percent[i] + 1, f'{high_productive_percent[i]:.1f}%', ha='center', fontsize=10)
#     plt.text(bar_positions[i] + 0.2, low_productive_percent[i] + 1, f'{low_productive_percent[i]:.1f}%', ha='center', fontsize=10)
#
# # Customize the chart
# plt.xticks(bar_positions, categories)
# plt.xlabel('Branch Count')
# plt.ylabel('Percentage')
# plt.title('GitFlow - High vs Low Productivity Branch Count')
# plt.legend()
#
# # Display the chart
# plt.tight_layout()
# plt.show()

""" ***************************************** Branch count in Multi Repository (Frontend) ************************** """
#
# # Data for Github Flow - High productivity branch count
# high_productive = {'zero_five': 50, 'six_ten': 37, 'eleven_25': 35, 'twentysix_50': 32, 'more_50': 15}
# total_high_productive = sum(high_productive.values())
#
# # Data for Github Flow - Low productivity branch count
# low_productive = {'zero_five': 273, 'six_ten': 78, 'eleven_25': 129, 'twentysix_50': 59, 'more_50': 8}
# total_low_productive = sum(low_productive.values())
#
# # Calculate percentages for high productivity branches
# high_productive_percent = [count / total_high_productive * 100 for count in high_productive.values()]
#
# # Calculate percentages for low productivity branches
# low_productive_percent = [count / total_low_productive * 100 for count in low_productive.values()]
#
# # Categories and bar positions
# categories = list(high_productive.keys())
# bar_positions = np.arange(len(categories))
#
# # Set the figure size
# plt.figure(figsize=(10, 6))
#
# # Plotting the bars for high productivity branches
# plt.bar(bar_positions - 0.2, high_productive_percent, width=0.4, label='High Productivity', align='center')
#
# # Plotting the bars for low productivity branches
# plt.bar(bar_positions + 0.2, low_productive_percent, width=0.4, label='Low Productivity', align='center')
#
# # Adding data labels on top of each bar
# for i in range(len(categories)):
#     plt.text(bar_positions[i] - 0.2, high_productive_percent[i] + 1, f'{high_productive_percent[i]:.1f}%', ha='center', fontsize=10)
#     plt.text(bar_positions[i] + 0.2, low_productive_percent[i] + 1, f'{low_productive_percent[i]:.1f}%', ha='center', fontsize=10)
#
# # Customize the chart
# plt.xticks(bar_positions, categories)
# plt.xlabel('Branch Count')
# plt.ylabel('Percentage')
# plt.title('GitFlow - High vs Low Productivity Branch Count')
# plt.legend()
#
# # Display the chart
# plt.tight_layout()
# plt.show()

""" ***************************************** Branch count in Multi Repository (Frontend) (All together) ************************** """
# # Data
# github_flow_high_productivity = {
#     'zero_five': 50,
#     'six_ten': 37,
#     'eleven_25': 35,
#     'twentysix_50': 32,
#     'more_50': 15
# }
#
# github_flow_low_productivity = {
#     'zero_five': 273,
#     'six_ten': 78,
#     'eleven_25': 129,
#     'twentysix_50': 59,
#     'more_50': 8
# }
#
# gitflow_high_productivity = {
#     'zero_five': 42,
#     'six_ten': 27,
#     'eleven_25': 25,
#     'twentysix_50': 42,
#     'more_50': 8
# }
#
# gitflow_low_productivity = {
#     'zero_five': 121,
#     'six_ten': 58,
#     'eleven_25': 72,
#     'twentysix_50': 32,
#     'more_50': 5
# }

#  Backend Statistics

# Data
# github_flow_high_productivity = {
#     'zero_five': 47,
#     'six_ten': 22,
#     'eleven_25': 40,
#     'twentysix_50': 25,
#     'more_50': 6
# }
#
# github_flow_low_productivity = {
#     'zero_five': 267,
#     'six_ten': 88,
#     'eleven_25': 121,
#     'twentysix_50': 24,
#     'more_50': 5
# }
#
# gitflow_high_productivity = {
#     'zero_five': 43,
#     'six_ten': 19,
#     'eleven_25': 42,
#     'twentysix_50': 17,
#     'more_50': 8
# }
#
# gitflow_low_productivity = {
#     'zero_five': 126,
#     'six_ten': 70,
#     'eleven_25': 77,
#     'twentysix_50': 17,
#     'more_50': 8
# }


# X-axis categories
# categories = ['zero_five', 'six_ten', 'eleven_25', 'twentysix_50', 'more_50']
#
#
# # Calculate the sum of branch counts for each productivity category and branching strategy
# github_flow_high_total = sum(github_flow_high_productivity.values())
# github_flow_low_total = sum(github_flow_low_productivity.values())
# gitflow_high_total = sum(gitflow_high_productivity.values())
# gitflow_low_total = sum(gitflow_low_productivity.values())
#
# # Heights of bars as percentages
# github_flow_high = [val / github_flow_high_total * 100 for val in github_flow_high_productivity.values()]
# github_flow_low = [val / github_flow_low_total * 100 for val in github_flow_low_productivity.values()]
# gitflow_high = [val / gitflow_high_total * 100 for val in gitflow_high_productivity.values()]
# gitflow_low = [val / gitflow_low_total * 100 for val in gitflow_low_productivity.values()]
#
# # Set the bar width
# bar_width = 0.2
#
# # Set the x positions of the bars
# index = np.arange(len(categories))
#
# # Plotting the bar chart
# plt.bar(index, github_flow_high, bar_width, label='Github Flow - High Productivity')
# plt.bar(index + bar_width, github_flow_low, bar_width, label='Github Flow - Low Productivity')
#
# # Add spacing between the bars of different branching strategies
# plt.bar(index + 2 * bar_width + 0.1, gitflow_high, bar_width, label='GitFlow - High Productivity')
# plt.bar(index + 3 * bar_width + 0.1, gitflow_low, bar_width, label='GitFlow - Low Productivity')
#
# # Set x-axis labels, y-axis label, and title
# plt.xlabel('Branch Count')
# plt.ylabel('Percentage')
# plt.title('Branch Counts by Branching Strategy and Productivity')
#
# # Set the x-axis tick positions and labels
# plt.xticks(index + 2 * bar_width + 0.1, categories)
#
# # Add percentages on top of each bar
# for i, val in enumerate(github_flow_high):
#     plt.text(i, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(github_flow_low):
#     plt.text(i + bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(gitflow_high):
#     plt.text(i + 2 * bar_width + 0.1, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(gitflow_low):
#     plt.text(i + 3 * bar_width + 0.1, val + 1, f'{val:.1f}%', ha='center', va='bottom')
#
# # Add a legend
# plt.legend()
#
# # Display the plot
# plt.tight_layout()
# plt.show()

""" ***************************************** Branch count in Multi Repository (Backend) (All together) ************************** """
# # Data
# github_flow_high_productivity = {
#     'zero_five': 47,
#     'six_ten': 22,
#     'eleven_25': 40,
#     'twentysix_50': 25,
#     'more_50': 6
# }
#
# github_flow_low_productivity = {
#     'zero_five': 267,
#     'six_ten': 88,
#     'eleven_25': 121,
#     'twentysix_50': 24,
#     'more_50': 5
# }
#
# gitflow_high_productivity = {
#     'zero_five': 43,
#     'six_ten': 19,
#     'eleven_25': 42,
#     'twentysix_50': 17,
#     'more_50': 8
# }
#
# gitflow_low_productivity = {
#     'zero_five': 126,
#     'six_ten': 70,
#     'eleven_25': 77,
#     'twentysix_50': 17,
#     'more_50': 8
# }
#
# categories = ['zero_five', 'six_ten', 'eleven_25', 'twentysix_50', 'more_50']
#
# # Calculate the sum of branch counts for each productivity category and branching strategy
# github_flow_high_total = sum(github_flow_high_productivity.values())
# github_flow_low_total = sum(github_flow_low_productivity.values())
# gitflow_high_total = sum(gitflow_high_productivity.values())
# gitflow_low_total = sum(gitflow_low_productivity.values())
#
# # Heights of bars as percentages
# github_flow_high = [val / github_flow_high_total * 100 for val in github_flow_high_productivity.values()]
# github_flow_low = [val / github_flow_low_total * 100 for val in github_flow_low_productivity.values()]
# gitflow_high = [val / gitflow_high_total * 100 for val in gitflow_high_productivity.values()]
# gitflow_low = [val / gitflow_low_total * 100 for val in gitflow_low_productivity.values()]
#
# # Set the bar width
# bar_width = 0.2
#
# # Set the x positions of the bars
# index = np.arange(len(categories))
#
# # Plotting the bar chart
# plt.bar(index, github_flow_high, bar_width, label='Github Flow - High Productivity')
# plt.bar(index + bar_width, github_flow_low, bar_width, label='Github Flow - Low Productivity')
#
# # Add spacing between the bars of different branching strategies
# plt.bar(index + 2 * bar_width + 0.1, gitflow_high, bar_width, label='GitFlow - High Productivity')
# plt.bar(index + 3 * bar_width + 0.1, gitflow_low, bar_width, label='GitFlow - Low Productivity')
#
# # Set x-axis labels, y-axis label, and title
# plt.xlabel('Branch Count')
# plt.ylabel('Percentage')
# plt.title('Branch Counts by Branching Strategy and Productivity')
#
# # Add percentages on top of each bar
# for i, val in enumerate(github_flow_high):
#     plt.text(i, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(github_flow_low):
#     plt.text(i + bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(gitflow_high):
#     plt.text(i + 2 * bar_width + 0.1, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(gitflow_low):
#     plt.text(i + 3 * bar_width + 0.1, val + 1, f'{val:.1f}%', ha='center', va='bottom')
#
# # Add a legend
# plt.legend()
#
# # Display the plot
# plt.tight_layout()
# plt.show()

""" ***************************************** Commit count in Mono Repository ************************************** """
# # Data
# github_flow_high_productivity = {
#     '0-50': 3,
#     '50-100': 15,
#     '100-250': 86,
#     '250-500': 50,
#     'more 500': 28
# }
#
# github_flow_low_productivity = {
#     '0-50': 130,
#     '50-100': 186,
#     '100-250': 164,
#     '250-500': 35,
#     'more 500': 24
# }
#
# gitflow_high_productivity = {
#     '0-50': 1,
#     '50-100': 5,
#     '100-250': 44,
#     '250-500': 17,
#     'more 500': 15
# }
#
# gitflow_low_productivity = {
#     '0-50': 28,
#     '50-100': 49,
#     '100-250': 42,
#     '250-500': 14,
#     'more 500': 7
# }
#
# # X-axis categories
# categories = ['0-50', '50-100', '100-250', '250-500', 'more 500']
#
# # Calculate the sum of commit counts for each productivity category and branching strategy
# github_flow_high_total = sum(github_flow_high_productivity.values())
# github_flow_low_total = sum(github_flow_low_productivity.values())
# gitflow_high_total = sum(gitflow_high_productivity.values())
# gitflow_low_total = sum(gitflow_low_productivity.values())
#
# # Heights of bars as percentages
# github_flow_high = [val / github_flow_high_total * 100 for val in github_flow_high_productivity.values()]
# github_flow_low = [val / github_flow_low_total * 100 for val in github_flow_low_productivity.values()]
# gitflow_high = [val / gitflow_high_total * 100 for val in gitflow_high_productivity.values()]
# gitflow_low = [val / gitflow_low_total * 100 for val in gitflow_low_productivity.values()]
#
# # Set the bar width
# bar_width = 0.2
#
# # Set the x positions of the bars
# index = np.arange(len(categories))
#
# # Plotting the bar chart
# plt.bar(index, github_flow_high, bar_width, label='Github Flow - High Productivity')
# plt.bar(index + bar_width, github_flow_low, bar_width, label='Github Flow - Low Productivity')
#
# # Set x-axis labels, y-axis label, and title
# plt.xlabel('Commit Count')
# plt.ylabel('Percentage')
# plt.title('Commit Counts by Branching Strategy and Productivity')
#
# # Add percentages on top of each bar
# for i, val in enumerate(github_flow_high):
#     plt.text(i, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(github_flow_low):
#     plt.text(i + bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
#
# # Plotting the bar chart for GitFlow
# plt.bar(index + 2 * bar_width, gitflow_high, bar_width, label='GitFlow - High Productivity')
# plt.bar(index + 3 * bar_width, gitflow_low, bar_width, label='GitFlow - Low Productivity')
#
# # Add percentages on top of each bar for GitFlow
# for i, val in enumerate(gitflow_high):
#     plt.text(i + 2 * bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(gitflow_low):
#     plt.text(i + 3 * bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
#
# # Set the x-axis tick positions and labels
# plt.xticks(index + 2 * bar_width, categories)
#
# # Add a legend
# plt.legend()
#
# # Display the plot
# plt.tight_layout()
# plt.show()

""" ***************************************** Commit count in Multi Repository ************************************** """

# Data  Frontend
# github_flow_high_productivity = {
#     '0-50': 1,
#     '50-100': 16,
#     '100-250': 80,
#     '250-500': 42,
#     'more 500': 28
# }
#
# github_flow_low_productivity = {
#     '0-50': 130,
#     '50-100': 177,
#     '100-250': 158,
#     '250-500': 33,
#     'more 500': 36
# }
#
# gitflow_high_productivity = {
#     '0-50': 0,
#     '50-100': 14,
#     '100-250': 59,
#     '250-500': 34,
#     'more 500': 37
# }
#
# gitflow_low_productivity = {
#     '0-50': 52,
#     '50-100': 85,
#     '100-250': 104,
#     '250-500': 30,
#     'more 500': 14
# }

# Data Backend
# github_flow_high_productivity = {
#     '0-50': 2,
#     '50-100': 26,
#     '100-250': 62,
#     '250-500': 31,
#     'more 500': 17
# }
#
# github_flow_low_productivity = {
#     '0-50': 130,
#     '50-100': 161,
#     '100-250': 139,
#     '250-500': 38,
#     'more 500': 30
# }
#
# gitflow_high_productivity = {
#     '0-50': 2,
#     '50-100': 8,
#     '100-250': 63,
#     '250-500': 25,
#     'more 500': 29
# }
#
# gitflow_low_productivity = {
#     '0-50': 56,
#     '50-100': 88,
#     '100-250': 107,
#     '250-500': 23,
#     'more 500': 18
# }
#
# # X-axis categories
# categories = ['0-50', '50-100', '100-250', '250-500', 'more 500']
#
# # Calculate the sum of commit counts for each productivity category and branching strategy
# github_flow_high_total = sum(github_flow_high_productivity.values())
# github_flow_low_total = sum(github_flow_low_productivity.values())
# gitflow_high_total = sum(gitflow_high_productivity.values())
# gitflow_low_total = sum(gitflow_low_productivity.values())
#
# # Heights of bars as percentages
# github_flow_high = [val / github_flow_high_total * 100 for val in github_flow_high_productivity.values()]
# github_flow_low = [val / github_flow_low_total * 100 for val in github_flow_low_productivity.values()]
# gitflow_high = [val / gitflow_high_total * 100 for val in gitflow_high_productivity.values()]
# gitflow_low = [val / gitflow_low_total * 100 for val in gitflow_low_productivity.values()]
#
# # Set the bar width
# bar_width = 0.2
#
# # Set the x positions of the bars
# index = np.arange(len(categories))
#
# # Plotting the bar chart
# plt.bar(index, github_flow_high, bar_width, label='Github Flow - High Productivity')
# plt.bar(index + bar_width, github_flow_low, bar_width, label='Github Flow - Low Productivity')
#
# # Set x-axis labels, y-axis label, and title
# plt.xlabel('Commit Count')
# plt.ylabel('Percentage')
# plt.title('Commit Counts by Branching Strategy and Productivity')
#
# # Add percentages on top of each bar
# for i, val in enumerate(github_flow_high):
#     plt.text(i, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(github_flow_low):
#     plt.text(i + bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
#
# # Plotting the bar chart for GitFlow
# plt.bar(index + 2 * bar_width, gitflow_high, bar_width, label='GitFlow - High Productivity')
# plt.bar(index + 3 * bar_width, gitflow_low, bar_width, label='GitFlow - Low Productivity')
#
# # Add percentages on top of each bar for GitFlow
# for i, val in enumerate(gitflow_high):
#     plt.text(i + 2 * bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
# for i, val in enumerate(gitflow_low):
#     plt.text(i + 3 * bar_width, val + 1, f'{val:.1f}%', ha='center', va='bottom')
#
# # Set the x-axis tick positions and labels
# plt.xticks(index + 2 * bar_width, categories)
#
# # Add a legend
# plt.legend()
#
# # Display the plot
# plt.tight_layout()
# plt.show()
#

""" ****************************************  """





