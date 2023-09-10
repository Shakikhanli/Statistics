import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

data_multi_front_language = {'JavaScript': 3892, 'TypeScript': 2460, 'Vue-Ruby': 690, 'HTML-CSS': 914,
                             'Java': 131, 'PHP': 65, 'Python': 38, 'C': 30}
data_multi_back_language = {'JavaScript': 3194, 'TypeScript': 1602, 'Vue-Ruby': 355, 'HTML-CSS': 350,
                            'Java': 1431, 'PHP': 339, 'Python': 862, 'C': 75}
data_mono_language = {'JavaScript': 16398, 'TypeScript': 4562, 'HTML-CSS': 6399, 'Java': 2330,
                      'Python': 1739, 'PHP': 941, 'Vue-Ruby': 1108, 'C': 50}

""" *****************************************************************************************************************"""
# languages = set(data_multi_front_language.keys()).union(data_multi_back_language.keys()).union(data_mono_language.keys())
# languages = list(languages)
#
# mono_percentages = np.array([(data_mono_language.get(lang, 0) / sum(data_mono_language.values())) * 100 for lang in languages])
# front_end_percentages = np.array([(data_multi_front_language.get(lang, 0) / sum(data_multi_front_language.values())) * 100 for lang in languages])
# back_end_percentages = np.array([(data_multi_back_language.get(lang, 0) / sum(data_multi_back_language.values())) * 100 for lang in languages])
#
# fig, ax = plt.subplots()
# bar_width = 0.3
# index = np.arange(len(languages))
#
# bar1 = ax.bar(index, mono_percentages, bar_width, label='Mono')
# bar2 = ax.bar(index + bar_width, front_end_percentages, bar_width, label='Front-End', color='orange')
# bar3 = ax.bar(index + 2*bar_width, back_end_percentages, bar_width, label='Back-End', color='green')
#
# ax.set_ylabel('Percentage')
# ax.set_title('Language Usage')
# ax.set_xticks(index + bar_width)
# ax.set_xticklabels(languages, rotation=45)
# ax.legend()
#
# plt.tight_layout()
# plt.show()
""" *****************************************************************************************************************"""
# languages = set(data_multi_front_language.keys()).union(data_multi_back_language.keys()).union(data_mono_language.keys())
# languages = list(languages)
#
# mono_percentages = np.array([(data_mono_language.get(lang, 0) / sum(data_mono_language.values())) * 100 for lang in languages])
# front_end_percentages = np.array([(data_multi_front_language.get(lang, 0) / sum(data_multi_front_language.values())) * 100 for lang in languages])
# back_end_percentages = np.array([(data_multi_back_language.get(lang, 0) / sum(data_multi_back_language.values())) * 100 for lang in languages])
#
# fig, ax = plt.subplots()
# bar_width = 0.3
# index = np.arange(len(languages))
#
# bar1 = ax.bar(index, mono_percentages, bar_width, label='Mono')
# bar2 = ax.bar(index + bar_width, front_end_percentages, bar_width, label='Front-End', color='red')
# bar3 = ax.bar(index + 2*bar_width, back_end_percentages, bar_width, label='Back-End', color='green')
#
# ax.set_ylabel('Percentage')
# ax.set_title('Language Usage')
# ax.set_xticks(index + bar_width)
# ax.set_xticklabels(languages, rotation=45)
# ax.legend()
#
# # Add percentage labels on top of each bar
# for bar in bar1 + bar2 + bar3:
#     height = bar.get_height()
#     ax.annotate(f'{height:.2f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
#                 xytext=(0, 2), textcoords='offset points', ha='center', va='bottom')
#
# plt.tight_layout()
# plt.show()

""" ************************************** Linear Regression ********************************************************"""


# # Given data
# y = [1.0, 0.1666666667, 0.3333333333, 0.3333333333, 2.6666666667, 7.1666666667, 7.1666666667, 0.5, 0.8333333333, 1.1666666667,
#      2.8333333333, 4.0, 2.1666666667, 1.5, 2.1666666667, 0.6666666667, 5.8333333333, 3.0, 2.1666666667, 1.3333333333, 1.6666666667,
#      0.6666666667, 0.6666666667, 7.0, 10.3333333333, 3.0, 2.6666666667, 4.1666666667, 2.6666666667, 1.5, 4.0, 4.5, 0.5,
#      0.1666666667, 0.1666666667, 0.6666666667, 0.6666666667, 0.1666666667, 4.8333333333, 0.8333333333, 0.8333333333, 1.8333333333,
#      1.6666666667, 0.1666666667, 3.6666666667, 1.6666666667, 1.0, 1.1666666667, 4.3333333333, 0.3333333333, 0.6666666667,
#      2.3333333333, 2.1666666667, 1.6666666667, 0.5, 0.3333333333, 0.3333333333, 1.3333333333, 0.8333333333, 0.8333333333, 1.5,
#      1.0, 0.8333333333, 0.5, 1.3333333333, 0.8333333333, 1.1666666667, 0.5, 0.8333333333, 0.5, 7.1666666667, 5.8333333333, 4.0,
#      3.6666666667, 0.5, 0.5, 0.5, 0.8333333333, 0.3333333333, 0.3333333333, 0.1666666667, 1.5, 1.5, 0.5, 0.3333333333, 0.1666666667,
#      0.6666666667, 0.1666666667, 2.0, 0.5, 2.0, 5.5, 1.1666666667, 1.1666666667, 0.8333333333, 0.8333333333, 0.5, 1.0, 1.3333333333,
#      0.8333333333, 0.8333333333, 1.1666666667, 0.3333333333, 0.3333333333, 0.6666666667, 0.3333333333, 0.6666666667, 0.3333333333,
#      0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.5, 0.5, 1.0, 2.0, 0.5, 0.5, 0.1666666667, 0.3333333333,
#      0.1666666667, 0.6666666667, 0.3333333333, 0.5, 0.3333333333, 0.5, 0.6666666667, 0.3333333333, 0.3333333333, 0.3333333333,
#      0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.3333333333, 0.1666666667, 0.1666666667, 0.3333333333, 0.6666666667,
#      0.6666666667, 0.1666666667, 0.1666666667, 0.6666666667, 0.3333333333, 0.3333333333, 0.3333333333, 0.1666666667, 0.1666666667,
#      0.1666666667, 0.1666666667, 0.1666666667, 0.3333333333, 0.3333333333, 0.1666666667, 1.1666666667]
#
# # Generate x values ranging from 0 to the length of y
# x = np.arange(len(y))
#
# # Set the figure size
# plt.figure(figsize=(10, 6))
#
# # Plot the data
# plt.plot(x, y, marker='o')
#
# # Customize the chart
# plt.xlabel('Development period')
# plt.ylabel('Mean value of activity')
# # plt.title('Chart Example')
# plt.xticks(np.arange(0, len(y), 10))  # Set x-axis ticks every 10 units
# plt.yticks(np.arange(0, 16, 2))  # Set y-axis ticks every 2 units
#
# # Display the chart
# plt.tight_layout()
# plt.show()