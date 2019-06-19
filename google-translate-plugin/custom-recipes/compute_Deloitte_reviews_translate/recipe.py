# -*- coding: utf-8 -*-
import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from google.cloud import translate

#Get config
credential = get_input_names_for_role('folder_of_credentials')[0]
credential = dataiku.Folder(str(credential))
credentials_path = credential.get_path()+credential.list_paths_in_partition()[0]
translate_client = translate.Client.from_service_account_json(credentials_path)

column_to_translate = get_recipe_config()["column_to_translate"]
target = get_recipe_config()["target_language"]
input_data_path=get_input_names_for_role('dataset_to_translate')[0]
output_data_path = get_output_names_for_role('dataset_translated')[0]

####################
# INIT GOOGLE CLIENT
####################
# The target language

def translate_from_google(row,column_to_translate):
    text = row[column_to_translate]
    translation = translate_client.translate(
    text,
    target_language=target)
    row[column_to_translate+'_translated_'+target] = translation['translatedText'] 
    row[column_to_translate+'_detectedSourceLanguage'] = translation['detectedSourceLanguage'] 
    return row

####################
# MANIPULATE DATA
####################

input_data= dataiku.Dataset(input_data_path)
input_data_df = input_data.get_dataframe()

input_data_df[column_to_translate+'_translated_'+target]=''
input_data_df[column_to_translate+'_detectedSourceLanguage']=''

input_data_df= input_data_df.apply(translate_from_google, column_to_translate=column_to_translate, axis=1)
input_data_translated_df = input_data_df

output_translated = dataiku.Dataset(output_data_path)
output_translated.write_with_schema(input_data_translated_df)