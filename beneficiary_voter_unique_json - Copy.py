import pandas as pd
import time
import json
start_time = time.time()
df1 =pd.read_excel(r"C:\Users\admin\Desktop\R\Beneficiary_MP_unique\Medak_34\Medak_34_MP_unique.xlsx")
df2 = pd.read_excel(r"C:\Users\admin\Desktop\R\Assembly_MP_unique\Medak_34\Medak_34_MP_unique.xlsx")
unique = pd.read_excel(r"C:\Users\admin\Desktop\R\Final_Uniques_File.xlsx")

print(len(df1))
print(len(df2))

df = pd.concat([df1,df2],ignore_index=True)
print("l1", len(df))
print(df.info())
df.dropna(subset=['Mobile','Names'], ignore_index=True,inplace=True)
print("l2", len(df))
df.drop_duplicates(subset=['Mobile'], ignore_index=True,inplace=True)
print("l3", len(df))
# file_path = 'siddipet_beneficiary+voters_data.xlsx'
# df.to_excel(file_path, index = False )
print(df.info())
#print(unique.info())

# df = df.dropna(subset = ['Names'])
#print(df.info())

# df_main = df.drop_duplicates(subset=['Names','Mobile_Numbers'], keep='first')
# print(df_main.info())
#
df['Names'] = df['Names'].str.lower()
df['Names'] = df['Names'].astype(str)
df['Names'] = df['Names'].str.strip()
print(df)

count = 0
result_dict = {}
#Iterate through unique names in df2
for unique_name in unique['Unqiue_names']:
    count = count + 1
    print('count',count)
    result = df[df['Names'].apply(lambda x: unique_name in x if x is not None else False)]
    # Check if there are any matching names
    if len(result) > 0:
        # Store Mobile_Numbers in the dictionary with Unique_name as key
        result_dict[unique_name] = list(result['Mobile'])
    df = df[~df['Names'].isin(result['Names'])]

# Print the result dictionary
print('result_dict', result_dict)
output_file_path = 'Medak_34_unique_Names_Numbers.json'
# Save the dictionary to a JSON file
with open(output_file_path, 'w') as json_file:
     json.dump(result_dict, json_file, indent=2)


df.to_excel('Medak_34_LeftOverData.xlsx')

# if len(df) < 1000:
#     df.to_excel('Medak_34_LeftOverData.xlsx')
# else:
#     df[:1000].to_excel('Medak_34_LeftOverData.xlsx')


# df_main = df_main[:10000]
# print(df_main.head())
# print(len(df_main))
#print(df_main.info())


# first_beneficiary = df_main.iloc[:1000000, :]
# second_beneficiary = df_main.iloc[999999:, :]
#
# first_beneficiary_file_path = 'wanted_voters_data_1.xlsx'
# first_beneficiary.to_excel(first_beneficiary_file_path,index = False)
#
# print(f"First beneficiary part saved to file '{first_beneficiary_file_path}'")
#
# second_beneficiary_file_path = 'wanted_voters_data_2.xlsx'
# second_beneficiary.to_excel(second_beneficiary_file_path,index = False)
#
# print(f"Second beneficiary part saved to file '{second_beneficiary_file_path}'")'''

# count = 0
# result_dict = {}
# #Iterate through unique names in df2
#
# for unique_name in unique['Unqiue_names']:
#     count = count + 1
#     print('count',count)
#     result = df_main[df_main['Names'].apply(lambda x: unique_name in x if x is not None else False)]
#     # Check if there are any matching names
#     if len(result) > 0:
#         # Store Mobile_Numbers in the dictionary with Unique_name as key
#         result_dict[unique_name] = list(result['Mobile_Numbers'])
#     df_main = df_main[~df_main['Names'].isin(result['Names'])]'''

# print(len(df_main))
# # Print the result dictionary
# print('result_dict', result_dict)
# output_file_path = 'unique_Names_Numbers.json'
#
# # Save the dictionary to a JSON file
# with open(output_file_path, 'w') as json_file:
#     json.dump(result_dict, json_file, indent=2)
#
# # if len(df_main) < 1000:
# df_main.to_excel('LeftOverData.xlsx')
# else:
#     df_main[:1000].to_excel('LeftOverData.xlsx')

end_time = time.time()
print('time : ', end_time-start_time)