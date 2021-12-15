import pandas as pd
# import geograpy3 : When this was run in October this worked with geograpy3 but updates to the repository changed the code slighlty. 
from geograpy3 import geograpy
import json
df_col_merged = pd.read_csv('Seroja__tokenised.csv', encoding = 'utf-8')
#x = {"text":"Two tropical cyclones off the coast of Western Australia, Seroja and Odette, moved clockwise around and approached each other to merge into a single system","hello":"1"}
#data_items = x.items()
#data_list = list(data_items)
#df_col_merged = pd.DataFrame(data_list)
# TEST:
# df_col_merged = pd.DataFrame({"text":"Two tropical cyclones off the coast of Western Australia, Seroja and Odette, moved clockwise around and approached each other to merge into a single system","hello":"1"}, index =['One','Two'])
# print(df_col_merged)
df_col_merged['place_context'] = df_col_merged['text'].apply(geograpy3.get_place_context(text = 'text'))  
df_col_merged['place_context.country'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).countries if pd.notnull(x) else x)
#df_col_merged['geoPlace_context'] = df_col_merged['text'].apply(lambda x: geograpy3.get_geoPlace_context(text=x) if pd.notnull(x) else x)
#df_col_merged['city'] = df_col_merged['text'].apply(lambda x: geograpy3.locateCity(text=x) if pd.notnull(x) else x)
df_col_merged['place_context.regions'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).regions if pd.notnull(x) else x)
df_col_merged['place_context.cities'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).cities if pd.notnull(x) else x)
df_col_merged['place_context.other'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).other if pd.notnull(x) else x)

# Advanced
df_col_merged['place_context_countryregions'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).country_regions if pd.notnull(x) else x)
df_col_merged['place_context_countrycities'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).country_cities if pd.notnull(x) else x)
df_col_merged['place_context_addressstr'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).address_strings if pd.notnull(x) else x)

# The above only work for one place per sentence. When there are multiple places then you can break them down by mentions. 
df_col_merged['place_context_countrymentions'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).country_mentions if pd.notnull(x) else x)
df_col_merged['place_context_regionmentions'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).region_mentions if pd.notnull(x) else x)
df_col_merged['place_context_citymentions'] = df_col_merged['text'].apply(lambda x: geograpy3.get_place_context(text=x).city_mentions if pd.notnull(x) else x)


df_col_merged.to_csv('Seroja__place_context.csv', encoding = 'utf-8')
#print(df_col_merged)

# ------------------------------------------------- NEW METHOD ------------------------------------------------------------------------------------------------------------
df_col_merged = pd.read_csv('Seroja__tokenised.csv', encoding = 'utf-8')

df_randomised = df_col_merged.sample(frac = 0.0093, replace = False, random_state = 1,axis = 0) #Collecting 0.93% of the 10,800 tweets - this is approximately 100 tweets

# For text code:
df_randomised['place_context.text'] = df_randomised['text'].apply(lambda x: geograpy.get_place_context(text=x) if pd.notnull(x) else x)

# Saving:
df_randomised.to_csv('Seroja__place_context_100randrows.csv', encoding = 'utf-8')
