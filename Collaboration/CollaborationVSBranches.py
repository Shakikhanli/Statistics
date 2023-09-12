import os
import json
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np

address_folder_multi = "E://Final Database(Collaboration)/Multi Repository"
address_folder_mono = "E://Final Database(Collaboration)/Mono Repository"

count = 0
total_count = len(os.listdir(address_folder_mono))
index = 0

dict_list = []
dict_list_mono = []
dict_list_multi = []

one_branch = 0
between_50_100 = 0
between_100_200 = 0
more_than_200 = 0

corrupted_files = ['12cesar--frontend-meang-online-shop1--backend-meang-online-shop.json', 'Aashishb4u--deck-cards-front-end--deck-cards-back-end.json',
                   'adwait-thattey--cdr-ipdr-visualizer-ui--cdr-ipdr-visualizer-backend.json', 'ajose-malik--spindle_yarn_frontend--spindle_yarn_backend.json',
                   'ajose-malik--spindle_yarn_frontend--spindle_yarn_backend.json', 'AleksanderTech--influential-people-.json', 'Amiens-bot--maxelec-.json', ''
                                                                                                                                                             'Amiens-bot--maxelec-.json', 'amitgur--hendrix-frontend--hendrix-backend.json', 'amitgur--hendrix-frontend--hendrix-backend.json', 'andersonrms--gobarber-web--gobarber-backend.json', 'andersonrms--gobarber-web--gobarber-backend.json', 'ansaar-in--ansaar.in.frontend--ansaar.in.backend.json', 'ansaar-in--ansaar.in.frontend--ansaar.in.backend.json', 'antonisierakowski--brainhub-form-frontend--brainhub-form-backend.json', 'antonisierakowski--brainhub-form-frontend--brainhub-form-backend.json', 'aota18--nuber-eats-frontend--nuber-eats-backend.json', 'aota18--nuber-eats-frontend--nuber-eats-backend.json', 'ArchivesPortalEuropeFoundation--ape-frontend--ape-backend.json', 'art-sn--chess-online-frontend--chess-online-backend.json', 'art-sn--chess-online-frontend--chess-online-backend.json', 'aurelticot--okato-client-verida--okato-server.json', 'awecode--edusanjal-frontend-archived--edusanjal-backend-archived.json', 'badjin--scraptube_frontend--scraptube_backend.json', 'badjin--scraptube_frontend--scraptube_backend.json', 'badjin--wedcamp_frontend--wedcamp_backend.json', 'badjin--wedcamp_frontend--wedcamp_backend.json', 'Baobah--.json', 'Baobah--.json', 'be-pongit--confac-front--confac-back.json', 'beatrizrms--savingtime-front--savingtime-backend.json', 'beatrizrms--savingtime-front--savingtime-backend.json', 'bentagai--mmmenu-.json', 'bentagai--mmmenu-.json', 'bequipedia--optitask-frontend--optitask-backend.json', 'bequipedia--optitask-frontend--optitask-backend.json', 'Bestfosscord--fosscord-client-cs.json', 'Bestfosscord--fosscord-ui.json',
                   'BogdanCinar--ecomm-frontend--ecomm-backend.json', 'BogdanCinar--ecomm-frontend--ecomm-backend.json', 'BondarOleg98--build-in-system-backend--Analysis-system-backend.json', 'BraianMendes--boilerplate_frontend-app-with-React.js-Redux--boilerplate_backend-app-with-Node.js-Express-Mongodb.json', 'brc-intern--tt_pho_frontend--tt_pho_backend.json', 'brc-intern--tt_pho_frontend--tt_pho_backend.json', 'bynjamin--flow-.json', 'bynjamin--flow-.json', 'caiomestres--rs-gobrb-front--rs-gobrb-back.json', 'caiomestres--rs-gobrb-front--rs-gobrb-back.json', 'ceopaludetto--teste-descomplica-web--teste-descomplica-api.json', 'ceopaludetto--teste-descomplica-web--teste-descomplica-api.json', 'fairandsmart--consent-manager-gui--consent-manager-back.json', 'fairandsmart--consent-manager-gui--consent-manager-back.json', 'haenah--1CL_front.json', 'haenah--1CL_front.json', 'IIP-Design--content-commons-client--content-commons-server.json', 'IIP-Design--content-commons-client--content-commons-server.json', 'JorgeAlejandroAguirreGutierrez--gym-frontend--gym-backend.json', 'JorgeAlejandroAguirreGutierrez--gym-frontend--gym-backend.json', 'JorgeAlejandroAguirreGutierrez--sic-ecuador-frontend--sic-ecuador-backend.json', 'JorgeAlejandroAguirreGutierrez--sic-ecuador-frontend--sic-ecuador-backend.json', 'over55--workery-front--workery-backend.json', 'over55--workery-frontend--workery-backend.json', 'over55--workery-frontend--workery-backend.json', 'Polar-Animal-League--pal-frontend--pal-backend.json', 'Polar-Animal-League--pal-frontend--pal-backend.json', 'rodrigolanes--oqueeoquee-.json', 'rodrigolanes--oqueeoquee-.json', 'SrijitaT--keyafeweb--keyafe-server.json', 'SWCapstoneDesign-Premium--Premium-.json', 'SWCapstoneDesign-Premium--Premium-.json', 'threecommasclub--tcc-.json', 'threecommasclub--tcc-.json', 'TradeDis--.json', 'vanityindia--.json', 'vanityindia--.json']


""" *********************************************** Mono Repository ************************************************ """
for each_file in os.listdir(address_folder_mono):
    count += 1
    print(total_count - count)

    if '.json' in each_file:
        commit_count = 0
        # print(each_file)
        with open(address_folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            if len(file_content['contributors']) > 2 and  0 < len(file_content['branches']) < 300 and \
                    file_content['Average collaboration value'] < 400:

                index += 1

                dict1 = {'Branch count': len(file_content['branches']),
                         'Collaboration ratio': file_content['Average collaboration value'],
                         'Productivity': file_content['Productivity']}

                dict_list.append(dict1)
                dict_list_mono.append(dict1)

""" *********************************************** Multi Repository (Front) ************************************************ """
# total_count = len(os.listdir(address_folder_multi))
#
# for each_file in os.listdir(address_folder_multi):
#     count += 1
#     print(total_count - count)
#
#     if '.json' in each_file:
#         commit_count = 0
#         # print(each_file)
#         with open(address_folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             branches = []
#             developers = []
#
#             front_productivity = file_content['Front Repositories']['Productivity']
#             back_productivity = file_content['Front Repositories']['Productivity']
#
#             for each_dev in file_content['Front Repositories']['branches']:
#                 if 'depend' not in each_dev['name']:
#                     branches.append(each_dev['name'])
#
#             for each_dev in file_content['Back Repositories']['branches']:
#                 if 'depend' not in each_dev['name']:
#                     branches.append(each_dev['name'])
#
#             for each_dev in file_content['Front Repositories']['contributors']:
#                 developers.append(each_dev['login'])
#
#             for each_dev in file_content['Back Repositories']['contributors']:
#                 developers.append(each_dev['login'])
#
#             branches = list(set(branches))
#             unique_developers = list(set(developers))
#
#             if front_productivity == 'High' or back_productivity == 'High':
#                 productivity = 'High'
#
#             elif (front_productivity != 'High' and back_productivity != 'High') and (
#                     front_productivity == 'Low' or back_productivity == 'Low'):
#                 productivity = 'Low'
#             else:
#                 productivity = 'None'
#
#             if len(branches) < 125 and len(unique_developers) > 1 and file_content['Average collaboration value'] < 500:
#                 dict1 = {'Branch count': len(branches),
#                          'Collaboration ratio': file_content['Average collaboration value'],
#                          'Productivity': productivity}
#
#                 dict_list.append(dict1)
#                 dict_list_multi.append(dict1)


""" ************************************ Create Scatter Plot with correlation line ********************************* """
data = dict_list_mono

data = sorted(data, key=lambda x: x['Branch count'])

x = [entry['Branch count'] for entry in data]
y = [entry['Collaboration ratio'] for entry in data]

# Extracting data for 'Branch Count' and 'Collaboration Ratio'
branch_count = [entry['Branch count'] for entry in data]
collaboration_ratio = [entry['Collaboration ratio'] for entry in data]

# Separate the data into different categories
low_productivity_data = [entry for entry in data if entry['Productivity'] == "Low"]
high_productivity_data = [entry for entry in data if entry['Productivity'] == "High"]
none_productivity_data = [entry for entry in data if entry['Productivity'] == "None"]

# Calculate the correlation coefficient
correlation_coefficient, _ = pearsonr(branch_count, collaboration_ratio)

# Calculate correlation coefficients for each category
correlation_coefficient_low, _ = pearsonr(
    [entry['Branch count'] for entry in low_productivity_data],
    [entry['Collaboration ratio'] for entry in low_productivity_data]
)

correlation_coefficient_high, _ = pearsonr(
    [entry['Branch count'] for entry in high_productivity_data],
    [entry['Collaboration ratio'] for entry in high_productivity_data]
)

correlation_coefficient_none, _ = pearsonr(
    [entry['Branch count'] for entry in none_productivity_data],
    [entry['Collaboration ratio'] for entry in none_productivity_data]
)

# Define colors for each 'Productivity' category
colors = {'Low': 'blue', 'High': 'green', 'None': 'red'}

# Create a scatter plot
# plt.scatter(x, y, marker='o', s=10, label=f'Correlation = {correlation_coefficient:.2f}')


# Create a scatter plot with colors based on 'Productivity'
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed
for entry in data:
    plt.scatter(
        entry['Branch count'],
        entry['Collaboration ratio'],
        color=colors[entry['Productivity']],
        s=15,  # Decrease dot size to 50 (adjust as needed)
        label=None  # No label for individual points
    )


# Adding labels and title
plt.xlabel('Branch count')
plt.ylabel('Collaboration ratio')
plt.title('Correlation Ratio vs. Branch Count (Scatter Plot)')

# Add a correlation line
z = np.polyfit(branch_count, collaboration_ratio, 1)
p = np.poly1d(z)
# plt.plot(branch_count, p(branch_count), 'r--', label=f'Correlation = {correlation_coefficient:.2f}')

# Create a custom legend with unique 'Productivity' labels
legend_labels = {productivity: color for productivity, color in colors.items()}
for label, color in legend_labels.items():
    plt.scatter([], [], color=color, label=f"Productivity: {label}", s=50)

plt.text(
    0.02, 0.95,
    f'Correlation for Low: {correlation_coefficient_low:.2f}',
    transform=plt.gca().transAxes
)
plt.text(
    0.02, 0.90,
    f'Correlation for High: {correlation_coefficient_high:.2f}',
    transform=plt.gca().transAxes
)
plt.text(
    0.02, 0.85,
    f'Correlation for None: {correlation_coefficient_none:.2f}',
    transform=plt.gca().transAxes
)

# Move the legend to the upper-right corner
plt.legend(loc='upper right')


# Show the chart
plt.grid(True)
plt.show()

""" **************************************** Corralation   **************************************************** """
# # Extracting data for 'Branch Count' and 'Collaboration Ratio'
# branch_count = [entry['Branch count'] for entry in dict_list_mono]
# collaboration_ratio = [entry['Collaboration ratio'] for entry in dict_list_mono]
#
# # Calculate the correlation coefficient
# correlation_coefficient, _ = pearsonr(branch_count, collaboration_ratio)
#
# # Print the correlation coefficient
# print(f'Correlation Coefficient: {correlation_coefficient}')
#














