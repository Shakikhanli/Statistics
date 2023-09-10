import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


""" ********************************************* Given data for Mono ********************************************** """
# high_productivity = {
#     'less_than_50': 21,
#     'between_50_100': 54,
#     'between_100_200': 45,
#     'more_than_200': 9
# }
#
# low_productivity = {
#     'less_than_50': 3,
#     'between_50_100': 41,
#     'between_100_200': 56,
#     'more_than_200': 25
# }

""" ********************************************* Given data for Mono ********************************************** """
# high_productivity = {
#     'less_than_50': 23,
#     'between_50_100': 169,
#     'between_100_200': 49,
#     'more_than_200': 5
# }
#
# low_productivity = {
#     'less_than_50': 7,
#     'between_50_100': 171,
#     'between_100_200': 55,
#     'more_than_200': 13
# }

""" Creating bar charts for both Mono and Multi repo projects"""
# # Calculate the total sum of values for both high and low productivity
# total_sum_high = sum(high_productivity.values())
# total_sum_low = sum(low_productivity.values())
#
# # Calculate percentages for each category
# high_productivity_percentages = [(value / total_sum_high) * 100 for value in high_productivity.values()]
# low_productivity_percentages = [(value / total_sum_low) * 100 for value in low_productivity.values()]
#
# # Extract categories
# categories = high_productivity.keys()
#
# # Create x-axis positions for the bars
# x = range(len(categories))
#
# # Create the bar chart
# bar_width = 0.35
# plt.bar(x, high_productivity_percentages, width=bar_width, label='High Productivity')
# plt.bar([i + bar_width for i in x], low_productivity_percentages, width=bar_width, label='Low Productivity')
#
# # Set the x-axis labels
# plt.xticks([i + bar_width / 2 for i in x], categories)
#
# # Add percentage values on top of each bar
# for i, value in enumerate(high_productivity_percentages):
#     plt.text(i, value, f'{value:.1f}%', ha='center', va='bottom')
# for i, value in enumerate(low_productivity_percentages):
#     plt.text(i + bar_width, value, f'{value:.1f}%', ha='center', va='bottom')
#
# # Set labels and title
# plt.xlabel('Categories')
# plt.ylabel('Percentage')
# plt.title('Productivity Comparison by Category')
#
# # Add a legend
# plt.legend()
#
# # Show the chart
# plt.show()

