import sys
import time
import os
import json
import math
import pandas as pd
import shutil

source_folder = "E://Database Productive/Multi Repository"
# target_folder = "E://Final Database(Collaboration)/Mono Repository"
target_folder = "E://Final Database(Collaboration)/Multi Repository"

# address_folder = "E://Database Productive/Mono Repository"

total_request_count = 0

count = 0
total_count = len(os.listdir(source_folder))
total_commit_count = 0
index = 0

request_count = 0

existing_files = []

error_count = 0


corrupted_files = ['12cesar--frontend-meang-online-shop1--backend-meang-online-shop.json', 'Aashishb4u--deck-cards-front-end--deck-cards-back-end.json',
                   'adwait-thattey--cdr-ipdr-visualizer-ui--cdr-ipdr-visualizer-backend.json', 'ajose-malik--spindle_yarn_frontend--spindle_yarn_backend.json',
                   'ajose-malik--spindle_yarn_frontend--spindle_yarn_backend.json', 'AleksanderTech--influential-people-.json', 'Amiens-bot--maxelec-.json', ''
                                                                                                                                                             'Amiens-bot--maxelec-.json', 'amitgur--hendrix-frontend--hendrix-backend.json', 'amitgur--hendrix-frontend--hendrix-backend.json', 'andersonrms--gobarber-web--gobarber-backend.json', 'andersonrms--gobarber-web--gobarber-backend.json', 'ansaar-in--ansaar.in.frontend--ansaar.in.backend.json', 'ansaar-in--ansaar.in.frontend--ansaar.in.backend.json', 'antonisierakowski--brainhub-form-frontend--brainhub-form-backend.json', 'antonisierakowski--brainhub-form-frontend--brainhub-form-backend.json', 'aota18--nuber-eats-frontend--nuber-eats-backend.json', 'aota18--nuber-eats-frontend--nuber-eats-backend.json', 'ArchivesPortalEuropeFoundation--ape-frontend--ape-backend.json', 'art-sn--chess-online-frontend--chess-online-backend.json', 'art-sn--chess-online-frontend--chess-online-backend.json', 'aurelticot--okato-client-verida--okato-server.json', 'awecode--edusanjal-frontend-archived--edusanjal-backend-archived.json', 'badjin--scraptube_frontend--scraptube_backend.json', 'badjin--scraptube_frontend--scraptube_backend.json', 'badjin--wedcamp_frontend--wedcamp_backend.json', 'badjin--wedcamp_frontend--wedcamp_backend.json', 'Baobah--.json', 'Baobah--.json', 'be-pongit--confac-front--confac-back.json', 'beatrizrms--savingtime-front--savingtime-backend.json', 'beatrizrms--savingtime-front--savingtime-backend.json', 'bentagai--mmmenu-.json', 'bentagai--mmmenu-.json', 'bequipedia--optitask-frontend--optitask-backend.json', 'bequipedia--optitask-frontend--optitask-backend.json', 'Bestfosscord--fosscord-client-cs.json', 'Bestfosscord--fosscord-ui.json',
                   'BogdanCinar--ecomm-frontend--ecomm-backend.json', 'BogdanCinar--ecomm-frontend--ecomm-backend.json', 'BondarOleg98--build-in-system-backend--Analysis-system-backend.json', 'BraianMendes--boilerplate_frontend-app-with-React.js-Redux--boilerplate_backend-app-with-Node.js-Express-Mongodb.json', 'brc-intern--tt_pho_frontend--tt_pho_backend.json', 'brc-intern--tt_pho_frontend--tt_pho_backend.json', 'bynjamin--flow-.json', 'bynjamin--flow-.json', 'caiomestres--rs-gobrb-front--rs-gobrb-back.json', 'caiomestres--rs-gobrb-front--rs-gobrb-back.json', 'ceopaludetto--teste-descomplica-web--teste-descomplica-api.json', 'ceopaludetto--teste-descomplica-web--teste-descomplica-api.json', 'fairandsmart--consent-manager-gui--consent-manager-back.json', 'fairandsmart--consent-manager-gui--consent-manager-back.json', 'haenah--1CL_front.json', 'haenah--1CL_front.json', 'IIP-Design--content-commons-client--content-commons-server.json', 'IIP-Design--content-commons-client--content-commons-server.json', 'JorgeAlejandroAguirreGutierrez--gym-frontend--gym-backend.json', 'JorgeAlejandroAguirreGutierrez--gym-frontend--gym-backend.json', 'JorgeAlejandroAguirreGutierrez--sic-ecuador-frontend--sic-ecuador-backend.json', 'JorgeAlejandroAguirreGutierrez--sic-ecuador-frontend--sic-ecuador-backend.json', 'over55--workery-front--workery-backend.json', 'over55--workery-frontend--workery-backend.json', 'over55--workery-frontend--workery-backend.json', 'Polar-Animal-League--pal-frontend--pal-backend.json', 'Polar-Animal-League--pal-frontend--pal-backend.json', 'rodrigolanes--oqueeoquee-.json', 'rodrigolanes--oqueeoquee-.json', 'SrijitaT--keyafeweb--keyafe-server.json', 'SWCapstoneDesign-Premium--Premium-.json', 'SWCapstoneDesign-Premium--Premium-.json', 'threecommasclub--tcc-.json', 'threecommasclub--tcc-.json', 'TradeDis--.json', 'vanityindia--.json', 'vanityindia--.json']


# percentage = (a / S) * 100

"""**************************************************** Mono Repository *********************************************"""
# for each_file in os.listdir(source_folder):
#     count += 1
#     print(total_count - count)
#
#     if '.json' in each_file and each_file not in existing_files:
#         commit_count = 0
#         with open(source_folder + '/' + each_file, 'r', encoding="utf8") as file:
#             file_content = json.load(file)
#
#             total_contribution_value = 0
#             contributions = []
#
#             mean_value = 0
#             sum_squared_diff = 0
#             standard_deviation = 0
#             coefficient_of_variation = 0
#
#             for each_contributor in file_content['contributors']:
#                 contributions.append(each_contributor['contributions'])
#                 total_contribution_value += each_contributor['contributions']
#
#             if total_contribution_value > 0:
#                 mean_value = total_contribution_value / len(file_content['contributors'])
#
#                 for each_value in contributions:
#
#                     sum_squared_diff += pow((each_value - mean_value), 2)
#
#                     standard_deviation = math.sqrt(sum_squared_diff/len(file_content['contributors']))
#
#                     coefficient_of_variation = (standard_deviation/mean_value) * 100
#
#                 file_content['Average collaboration value'] = coefficient_of_variation
#
#                 json_data = json.dumps(file_content)
#                 jsonFile = open(target_folder + '/' + each_file, "w")
#                 jsonFile.write(json_data)
#                 jsonFile.close()


"""**************************************************** Multi Repository *********************************************"""
for each_file in os.listdir(source_folder):
    count += 1
    print(total_count - count)

    if '.json' in each_file and each_file not in existing_files and each_file not in corrupted_files:
        index += 1
        with open(source_folder + '/' + each_file, 'r', encoding="utf8") as file:
            file_content = json.load(file)

            total_contribution_value = 0
            contributions = []

            mean_value = 0
            sum_squared_diff = 0
            standard_deviation = 0
            coefficient_of_variation = 0

            for each_contributor in file_content['Front Repositories']['contributors']:
                contributions.append(each_contributor)

            for each_contributor in file_content['Back Repositories']['contributors']:
                contributions.append(each_contributor)

            unique_names = set()

            # Create a new list to store dictionaries with unique "name" values
            filtered_data = []

            for item in contributions:
                name = item["login"]
                if name not in unique_names:
                    unique_names.add(name)
                    filtered_data.append(item)

            # contributions = list(set(contributions))

            for each_contributor in contributions:
                total_contribution_value += each_contributor['contributions']

            if total_contribution_value > 0:
                mean_value = total_contribution_value / len(filtered_data)

                for each_value in filtered_data:
                    sum_squared_diff += pow((each_value['contributions'] - mean_value), 2)
                    standard_deviation = math.sqrt(sum_squared_diff / len(filtered_data))
                    coefficient_of_variation = (standard_deviation / mean_value) * 100

            file_content['Average collaboration value'] = coefficient_of_variation

            json_data = json.dumps(file_content)
            jsonFile = open(target_folder + '/' + each_file, "w")
            jsonFile.write(json_data)
            jsonFile.close()

    # if index > 5:
    #     sys.exit()









            #
            # for each_contributor in file_content['Front Repositories']['contributors']:
            #     if each_contributor == 'message':
            #         error_count += 1
            #         corrupted_files.append(each_file)
            #         break
            #     contributions.append(each_contributor['contributions'])
            #     total_contribution_value += each_contributor['contributions']
            #
            # if total_contribution_value > 0:
            #     mean_value = total_contribution_value / len(file_content['Front Repositories']['contributors'])
            #
            #     for each_value in contributions:
            #         sum_squared_diff += pow((each_value - mean_value), 2)
            #         standard_deviation = math.sqrt(sum_squared_diff / len(file_content['Front Repositories']['contributors']))
            #         coefficient_of_variation = (standard_deviation / mean_value) * 100
            #
            #     file_content['Front Repositories']['Average collaboration value'] = coefficient_of_variation

            # # Backend part
            #
            # total_contribution_value = 0
            # contributions = []
            #
            # mean_value = 0
            # sum_squared_diff = 0
            # standard_deviation = 0
            # coefficient_of_variation = 0
            #
            # for each_contributor in file_content['Back Repositories']['contributors']:
            #     if each_contributor == 'message':
            #         error_count += 1
            #         corrupted_files.append(each_file)
            #         break
            #
            #     contributions.append(each_contributor['contributions'])
            #     total_contribution_value += each_contributor['contributions']
            #
            # if total_contribution_value > 0:
            #     mean_value = total_contribution_value / len(file_content['Back Repositories']['contributors'])
            #     for each_value in contributions:
            #         sum_squared_diff += pow((each_value - mean_value), 2)
            #         standard_deviation = math.sqrt(sum_squared_diff / len(file_content['Back Repositories']['contributors']))
            #         coefficient_of_variation = (standard_deviation / mean_value) * 100
            #
            #     file_content['Back Repositories']['Average collaboration value'] = coefficient_of_variation

            # json_data = json.dumps(file_content)
            # jsonFile = open(target_folder + '/' + each_file, "w")
            # jsonFile.write(json_data)
            # jsonFile.close()



print(error_count)
print(corrupted_files)

