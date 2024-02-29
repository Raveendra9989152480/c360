import pandas as pd
import time

start_time = time.time()
df = pd.read_excel(r"C:\Users\admin\Downloads\63-Unguturu.xlsx")
print("****************************************************************Total_Length..",len(df))
new_df = df.loc[:, ['FM_NAME_EN', 'LASTNAME_EN', 'MOBILE_NO']]
new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].fillna('')
new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].astype(str)
new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].astype(str)
new_df['FM_NAME_EN'] = new_df['FM_NAME_EN'].str.strip()
new_df['LASTNAME_EN'] = new_df['LASTNAME_EN'].str.strip()
new_df['Full Name'] = new_df['FM_NAME_EN'] + ' ' + new_df['LASTNAME_EN']
selected_columns = ['Full Name', 'MOBILE_NO']
result = new_df[selected_columns]
result = result.rename(columns={'Full Name': 'Names'})
result.dropna(subset = ['MOBILE_NO'], inplace = True)
result.dropna(subset = ['Names'], inplace = True)
print("******************************************************************After_dropping_of_blank_spaces", len(result))
print(result)
def clean_mobile_number(mobile):
    # Convert scientific notation to normal form
    if 'e' in str(mobile):
        mobile = "{:.0f}".format(mobile)
    # Remove ".0" if it exists at the end
    mobile_str = str(mobile)
    if mobile_str.endswith('.0'):
        mobile = mobile_str[:-2]
    return mobile
result['MOBILE_NO'] = result['MOBILE_NO'].apply(clean_mobile_number)
result['MOBILE_NO'] = result['MOBILE_NO'].astype('str')

result['MOBILE_NO'] = result['MOBILE_NO'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
print("******************************************************************After_valid_mobile_number1", len(result))
result['MOBILE_NO'] = result['MOBILE_NO'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
print("******************************************************************After_valid_mobile_number2", len(result))
#result.to_excel("raw_unguturu_mv.xlsx",index=False)
print("..................................................After_mobile_validation", len(result))

result.dropna(subset = ['MOBILE_NO'],ignore_index = True, inplace = True)

print("***************************************************original", len(result))
# result.to_excel("raw_unguturu_original.xlsx",index=False)
# result.drop_duplicates(subset=["MOBILE_NO"],ignore_index=True,inplace=True)
print("***************************************************after deleting dupicate numbers", len(result))
# result.to_excel("raw_unguturu_unique.xlsx",index=False)

# result = result.drop(df.columns[0], axis=1, inplace = True)
# result.to_excel(f"C:\\Users\\admin\\Desktop\\RAJA\\AP_Assembly_constituency_mobile_count\\ungunturu_original.xlsx",index=False)
# print(".........................................Filed stored successfully....")
# result.drop_duplicates(subset = ['Mobile'],ignore_index = True, inplace =True)
# result.to_excel(f"C:\\Users\\admin\\Desktop\\RAJA\\AP_Assembly_constituency_mobile_count\\ungunturu_unique.xlsx",index=False)
# print("*****************************************************unique", len(result))
# print(".......................................................Filed stored successfully....")
# end_time = time.time()
# print("Time :",end_time-start_time)