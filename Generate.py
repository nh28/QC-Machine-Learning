import os
from AddElements import AddElements
import pandas as pd
from Model import Model
from Query import Query
from tqdm import tqdm



query = Query()
username = "PCHARSCHN"
password = "White16Pots"
connection, success = query.connect(username, password)
if success:
    
   excel_file_path = os.path.abspath("Phase4&5_all_info.xlsx") 
   excel_sheet = "Sheet1"

   df = pd.read_excel(excel_file_path, sheet_name=excel_sheet)

   # Uncomment this section to fill data from ARKEON
   
   print("Generating data...Please wait")
   for index, row in tqdm(df.iterrows(), total=len(df)):
      type = row['MEAS_TYPE_ID']
      print(row)
      if type == 951:
         df.loc[index] = AddElements.add(query, row, connection, 940, 941, 964, 948, 949, 950, 951, 951, 14910, 15498)
      elif type == 14910:
         df.loc[index] = AddElements.add(query, row, connection, 14899, 14900, 14923, 14907, 14908, 14909, 14910, 951, 14910, 15498)
      elif type == 15498:
         df.loc[index] = AddElements.add(query, row, connection, 15492, 15493, 15494, 15495, 15496, 15497, 15498, 951, 14910, 15498)
   
   df.to_excel('Phase4&5_all_info_2.xlsx', sheet_name=excel_sheet, index=False)
   
   """
   cleaned_df = df.drop(columns = ['STN_ID', 'LOCAL_DATE_VALUE', 'LOCAL_YEAR', 'LOCAL_DAY', 'LOCAL_HOUR', 'LOCAL_MINUTE', 'UTC_DATE_VALUE', 'MEAS_TYPE_ID', 'VALUE', 'FLAG', 'STATUS', 'SPATIAL_LOC_ID'])
   X = cleaned_df.drop(columns = ['Accurate'])
   y = cleaned_df['Accurate']
   """
   # Uncomment to test and train model
   """
   # Method 1
   print('Original')
   model_1 = Model(X.drop(columns = ['Drizzle', 'Rain', 'Freezing Rain', 'Snow', 'Snow Grains', 'Ice Pellets', 'Rain Showers', 'Snow Showers', 'Hail', 'Blowing Snow', 'Thunderstorm', 'Snow Pellet', 'Ice Pellet Showers', 'Snow on Grnd +1', 'Snow on Grnd +2', 'Snow on Grnd +3', 'Snow and Mean Temp']), y)
   model_1.create_model(1)
   
   # Method 2: Add SOG for days after
   print("Add extra SOG")
   model_2 = Model(X.drop(columns = ['Drizzle', 'Rain', 'Freezing Rain', 'Snow', 'Snow Grains', 'Ice Pellets', 'Rain Showers', 'Snow Showers', 'Hail', 'Blowing Snow', 'Thunderstorm', 'Snow Pellet', 'Ice Pellet Showers', 'Snow and Mean Temp']), y)
   model_2.create_model(2)
  
   # Method 3: Add Hourly Data
   print("Add Hourly Data")
   model_3 = Model(X.drop(columns = ['Snow on Grnd +1', 'Snow on Grnd +2', 'Snow on Grnd +3', 'Snow and Mean Temp']), y)
   model_3.create_model(3)

   # Method 4: Add Hourly Data and SOG
   print("Add Hourly Data and SOG")
   model_4 = Model(X.drop(columns = ['Snow and Mean Temp']), y)
   model_4.create_model(4)

   # Method 4 & 5 Add Correlation between Snow and Temp
   X['Snow and Mean Temp'] = X['Mean Temp'] * X['Total Snow']

   print("Correlation + Original")
   model_5 = Model(X.drop(columns = ['Drizzle', 'Rain', 'Freezing Rain', 'Snow', 'Snow Grains', 'Ice Pellets', 'Rain Showers', 'Snow Showers', 'Hail', 'Blowing Snow', 'Thunderstorm', 'Snow Pellet', 'Ice Pellet Showers', 'Snow on Grnd +1', 'Snow on Grnd +2', 'Snow on Grnd +3']), y)
   model_5.create_model(5)

   print("Correlation + extra SOG")
   model_6 = Model(X.drop(columns = ['Drizzle', 'Rain', 'Freezing Rain', 'Snow', 'Snow Grains', 'Ice Pellets', 'Rain Showers', 'Snow Showers', 'Hail', 'Blowing Snow', 'Thunderstorm', 'Snow Pellet', 'Ice Pellet Showers']), y)
   model_6.create_model(6)

   print("Correlation + Hourly")
   model_7 = Model(X.drop(columns = ['Snow on Grnd +1', 'Snow on Grnd +2', 'Snow on Grnd +3']), y)
   model_7.create_model(7)

   print("Correlation + extra SOG + Hourly")
   model_8 = Model(X, y)
   model_8.create_model(8)
   """
   # Uncomment to use the existing model to predict data
   cleaned_df = df.drop(columns = ['Snow and Mean Temp'])
   X = cleaned_df.drop(columns = ['STN_ID', 'LOCAL_DATE_VALUE', 'LOCAL_YEAR', 'LOCAL_DAY', 'LOCAL_HOUR', 'LOCAL_MINUTE', 'UTC_DATE_VALUE', 'MEAS_TYPE_ID', 'VALUE', 'FLAG', 'STATUS', 'SPATIAL_LOC_ID', 'Accurate'])

   cleaned_df['Accurate'] = Model.predict_data(X, 4)
   cleaned_df.to_excel('Phase4&5_ver2.xlsx', sheet_name=excel_sheet, index=False)
   
   

else:
    print("Connection issue.")
