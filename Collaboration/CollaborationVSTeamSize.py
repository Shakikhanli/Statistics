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

corrupted_files = ['12cesar--frontend-meang-online-shop1--backend-meang-online-shop.json',
                   'Aashishb4u--deck-cards-front-end--deck-cards-back-end.json',
                   'adwait-thattey--cdr-ipdr-visualizer-ui--cdr-ipdr-visualizer-backend.json',
                   'ajose-malik--spindle_yarn_frontend--spindle_yarn_backend.json',
                   'AleksanderTech--influential-people-.json', 'Amiens-bot--maxelec-.json', ''
                                                                                            'Amiens-bot--maxelec-.json',
                   'amitgur--hendrix-frontend--hendrix-backend.json', 'amitgur--hendrix-frontend--hendrix-backend.json',
                   'andersonrms--gobarber-web--gobarber-backend.json',
                   'ansaar-in--ansaar.in.frontend--ansaar.in.backend.json',
                   'antonisierakowski--brainhub-form-frontend--brainhub-form-backend.json',
                   'aota18--nuber-eats-frontend--nuber-eats-backend.json',
                   'ArchivesPortalEuropeFoundation--ape-frontend--ape-backend.json',
                   'art-sn--chess-online-frontend--chess-online-backend.json',
                   'aurelticot--okato-client-verida--okato-server.json',
                   'awecode--edusanjal-frontend-archived--edusanjal-backend-archived.json',
                   'badjin--scraptube_frontend--scraptube_backend.json',
                   'badjin--wedcamp_frontend--wedcamp_backend.json', 'badjin--wedcamp_frontend--wedcamp_backend.json',
                   'Baobah--.json', 'Baobah--.json', 'be-pongit--confac-front--confac-back.json',
                   'beatrizrms--savingtime-front--savingtime-backend.json', 'bentagai--mmmenu-.json',
                   'bentagai--mmmenu-.json', 'bequipedia--optitask-frontend--optitask-backend.json',
                   'bequipedia--optitask-frontend--optitask-backend.json', 'Bestfosscord--fosscord-client-cs.json',
                   'Bestfosscord--fosscord-ui.json',
                   'BogdanCinar--ecomm-frontend--ecomm-backend.json', 'BogdanCinar--ecomm-frontend--ecomm-backend.json',
                   'BondarOleg98--build-in-system-backend--Analysis-system-backend.json',
                   'BraianMendes--boilerplate_frontend-app-with-React.js-Redux--boilerplate_backend-app-with-Node.js-Express-Mongodb.json',
                   'brc-intern--tt_pho_frontend--tt_pho_backend.json', 'bynjamin--flow-.json', 'bynjamin--flow-.json',
                   'caiomestres--rs-gobrb-front--rs-gobrb-back.json', 'caiomestres--rs-gobrb-front--rs-gobrb-back.json',
                   'ceopaludetto--teste-descomplica-web--teste-descomplica-api.json',
                   'fairandsmart--consent-manager-gui--consent-manager-back.json', 'haenah--1CL_front.json',
                   'haenah--1CL_front.json', 'IIP-Design--content-commons-client--content-commons-server.json',
                   'IIP-Design--content-commons-client--content-commons-server.json',
                   'JorgeAlejandroAguirreGutierrez--gym-frontend--gym-backend.json',
                   'JorgeAlejandroAguirreGutierrez--sic-ecuador-frontend--sic-ecuador-backend.json',
                   'over55--workery-front--workery-backend.json', 'over55--workery-frontend--workery-backend.json',
                   'over55--workery-frontend--workery-backend.json',
                   'Polar-Animal-League--pal-frontend--pal-backend.json', 'rodrigolanes--oqueeoquee-.json',
                   'rodrigolanes--oqueeoquee-.json', 'SrijitaT--keyafeweb--keyafe-server.json',
                   'SWCapstoneDesign-Premium--Premium-.json', 'SWCapstoneDesign-Premium--Premium-.json',
                   'threecommasclub--tcc-.json', 'threecommasclub--tcc-.json', 'TradeDis--.json',
                   'vanityindia--.json']

""" *********************************************** Mono Repository ************************************************ """
for each_file in os.listdir(address_folder_mono):
    count += 1
    print(total_count - count)

    if '.json' in each_file:
        commit_count = 0
        # print(each_file)
        with open(address_folder_mono + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            if 50 > len(file_content['contributors']) > 2 and 0 < len(file_content['commits']) < 4000 and file_content['Average collaboration value'] < 500:
                index += 1

                dict1 = {'Team size': len(file_content['contributors']),
                         'Collaboration ratio': file_content['Average collaboration value']}

                dict_list.append(dict1)
                dict_list_mono.append(dict1)

""" *********************************************** Multi Repository (Front) ************************************************ """
total_count = len(os.listdir(address_folder_multi))

for each_file in os.listdir(address_folder_multi):
    count += 1
    print(total_count - count)

    if '.json' in each_file:
        commit_count = 0
        # print(each_file)
        with open(address_folder_multi + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            branches = []
            developers = []

            commit_count = len(file_content['Front Repositories']['commits']) + len(file_content['Back Repositories']['commits'])

            # for each_dev in file_content['Front Repositories']['branches']:
            #     if 'depend' not in each_dev['name']:
            #         branches.append(each_dev['name'])
            #
            # for each_dev in file_content['Back Repositories']['branches']:
            #     if 'depend' not in each_dev['name']:
            #         branches.append(each_dev['name'])

            for each_dev in file_content['Front Repositories']['contributors']:
                developers.append(each_dev['login'])

            for each_dev in file_content['Back Repositories']['contributors']:
                developers.append(each_dev['login'])

            # branches = list(set(branches))
            unique_developers = list(set(developers))

            if 50 > len(unique_developers) > 2 and 0 < commit_count < 4000:
                dict1 = {'Team size': len(unique_developers),
                         'Collaboration ratio': file_content['Average collaboration value']}

                dict_list.append(dict1)
                dict_list_multi.append(dict1)

""" ************************************ Create Scatter Plot with correlation line Mono vs Multi ******************* """

# Sort both datasets by 'Collaboration Ratio'
dict_list_mono = sorted(dict_list_mono, key=lambda x: x['Collaboration ratio'])
dict_list_multi = sorted(dict_list_multi, key=lambda x: x['Collaboration ratio'])

# Combine both datasets
combined_data = dict_list_mono + dict_list_multi

# Extract 'Commit Count' and 'Collaboration Ratio'
commit_count = [entry['Team size'] for entry in combined_data]
collaboration_ratio = [entry['Collaboration ratio'] for entry in combined_data]

# Create the scatter plot with different markers for each dataset
plt.figure(figsize=(8, 6))

# Plot data from dict_list_mono with blue markers
plt.scatter(
    [entry['Collaboration ratio'] for entry in dict_list_mono],
    [entry['Team size'] for entry in dict_list_mono],
    marker='o', color='blue', label='Mono Data', s=10
)

# Plot data from dict_list_multi with red markers
plt.scatter(
    [entry['Collaboration ratio'] for entry in dict_list_multi],
    [entry['Team size'] for entry in dict_list_multi],
    marker='o', color='red', label='Multi Data', s=10
)

# Adding labels and title
plt.xlabel('Collaboration Ratio')
plt.ylabel('Team size')
plt.title('Scatter Plot of Team size vs. Collaboration Ratio (Combined Data)')

# Calculate and show the correlation coefficients for each dataset
correlation_coefficient_mono, _ = pearsonr(
    [entry['Collaboration ratio'] for entry in dict_list_mono],
    [entry['Team size'] for entry in dict_list_mono]
)

correlation_coefficient_multi, _ = pearsonr(
    [entry['Collaboration ratio'] for entry in dict_list_multi],
    [entry['Team size'] for entry in dict_list_multi]
)

# Create custom legend labels including dataset identifier and correlation coefficient
legend_labels = [
    f'Mono Data (Correlation: {correlation_coefficient_mono:.2f})',
    f'Multi Data (Correlation: {correlation_coefficient_multi:.2f})'
]

# Add regression lines for each dataset
z_mono = np.polyfit(
    [entry['Collaboration ratio'] for entry in dict_list_mono],
    [entry['Team size'] for entry in dict_list_mono],
    1
)

z_multi = np.polyfit(
    [entry['Collaboration ratio'] for entry in dict_list_multi],
    [entry['Team size'] for entry in dict_list_multi],
    1
)

p_mono = np.poly1d(z_mono)
p_multi = np.poly1d(z_multi)

plt.plot(
    [entry['Collaboration ratio'] for entry in dict_list_mono],
    p_mono([entry['Collaboration ratio'] for entry in dict_list_mono]),
    'b--',
    label=f'Mono Data Line (y={z_mono[0]:.2f}x+{z_mono[1]:.2f})'
)

plt.plot(
    [entry['Collaboration ratio'] for entry in dict_list_multi],
    p_multi([entry['Collaboration ratio'] for entry in dict_list_multi]),
    'r--',
    label=f'Multi Data Line (y={z_multi[0]:.2f}x+{z_multi[1]:.2f})'
)

# Show the legend with custom labels
plt.legend(legend_labels)

# Show the chart
plt.grid(True)
plt.show()





























