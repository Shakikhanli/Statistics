import os
import json
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

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

            if file_content['Productivity'] == 'Low' and len(file_content['contributors']) > 3:

                index += 1

                dict1 = {'Branch count': len(file_content['branches']),
                         'Collaboration ratio': file_content['Average collaboration value']}

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
#             developers = []
#
#             for each_dev in file_content['Front Repositories']['contributors']:
#                 developers.append(each_dev['login'])
#
#             for each_dev in file_content['Back Repositories']['contributors']:
#                 developers.append(each_dev['login'])
#
#             unique_developers = list(set(developers))
#
#             if len(unique_developers) > 3 and each_file not in corrupted_files and \
#                     (file_content['Front Repositories']['Productivity'] == 'Low' and file_content['Back Repositories']['Productivity'] == 'Low'):
#
#                 index += 1
#
#                 if file_content['Average collaboration value'] <= 50:
#                     less_than_50 += 1
#                 if 50 < file_content['Average collaboration value'] <= 100:
#                     between_50_100 += 1
#                 if 100 < file_content['Average collaboration value'] < 200:
#                     between_100_200 += 1
#                 if file_content['Average collaboration value'] > 200:
#                     more_than_200 += 1
#
#                 dict1 = {'Repo Type': 'Multi Repository',
#                          'Collaboration ratio': file_content['Average collaboration value']}
#
#                 dict_list.append(dict1)
#                 dict_list_multi.append(dict1)


""" **************************************************************************************************************** """
dict_list_mono = sorted(dict1, key=lambda x: x['Branch count'])

x = [entry['Branch count'] for entry in dict_list_mono]
y = [entry['Collaboration ratio'] for entry in dict_list_mono]

# Create a line chart
plt.plot(x, y, marker='', linestyle='-')

# Adding labels and title
plt.xlabel('Collaboration Ratio')
plt.ylabel('Branch count')
plt.title('Correlation Ratio vs. Branch Count')

# Show the chart
plt.grid(True)
plt.show()
