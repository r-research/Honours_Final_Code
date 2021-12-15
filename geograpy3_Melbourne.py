from geograpy3 import geograpy
import pandas as pd

df_filtered = pd.read_csv('Melb__tokenised.csv', encoding = 'utf-8')
#Running on one smaller file at a time
#df_filtered = pd.read_csv('1.csv', encoding = 'utf-8')

# Splitting dataframe by rows: https://www.geeksforgeeks.org/split-pandas-dataframe-by-rows/
# splitting dataframe by row index
df_1 = df_filtered.iloc[:500,:]
df_2 = df_filtered.iloc[7001:,:]

# For tokenised code:
df_1['place_context'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x) if pd.notnull(x) else x)

df_1['place_context.regions'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).regions if pd.notnull(x) else x)
df_1['place_context.cities'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).cities if pd.notnull(x) else x)
df_1['place_context.other'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).other if pd.notnull(x) else x)

# Advanced
df_1['place_context_countryregions'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).country_regions if pd.notnull(x) else x)
df_1['place_context_countrycities'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).country_cities if pd.notnull(x) else x)
df_1['place_context_addressstr'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).address_strings if pd.notnull(x) else x)

# The above only work for one place per sentence. When there are multiple places then you can break them down by mentions. 
df_1['place_context_countrymentions'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).country_mentions if pd.notnull(x) else x)
df_1['place_context_regionmentions'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).region_mentions if pd.notnull(x) else x)
df_1['place_context_citymentions'] = df_1['tokens'].apply(lambda x: geograpy.get_place_context(text=x).city_mentions if pd.notnull(x) else x)


# #df_1.to_csv('Melb__Geograpy3__tokens.csv', encoding = 'utf-8')
# df_1.to_csv('Melb__Geograpy3_2_tokens.csv', encoding = 'utf-8')

## -----------------------------------------------------------------------------------------------------------------------------
df_1['place_context_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x) if pd.notnull(x) else x)

df_1['place_context.regions_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).regions if pd.notnull(x) else x)
df_1['place_context.cities_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).cities if pd.notnull(x) else x)
df_1['place_context.other_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).other if pd.notnull(x) else x)

# Advanced
df_1['place_context_countryregions_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).country_regions if pd.notnull(x) else x)
#df_1['place_context_countrycities_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).country_cities if pd.notnull(x) else x)
#df_1['place_context_addressstr_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).address_strings if pd.notnull(x) else x)

# The above only work for one place per sentence. When there are multiple places then you can break them down by mentions. 
df_1['place_context_countrymentions_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).country_mentions if pd.notnull(x) else x)
df_1['place_context_regionmentions_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).region_mentions if pd.notnull(x) else x)
df_1['place_context_citymentions_text'] = df_1['text'].apply(lambda x: geograpy.get_place_context(text=x).city_mentions if pd.notnull(x) else x)

df_1.to_csv('Melb__Geograpy3_2_text.csv', encoding = 'utf-8')

