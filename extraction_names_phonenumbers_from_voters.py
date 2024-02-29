import pandas as pd
import time
import os
start_time = time.time()

file_path = r"C:\Users\admin\Desktop\R\Assembly_MP_Data"
all_folders = os.listdir(file_path)
print(all_folders)

# pattern = r'^[6-9]\d{9}$'
# constituency = 'West_Godavari'
for folder in all_folders:
    # print(folder)
    if folder == 'Mahbubnagar_74':
        files = os.path.join(file_path+'\\'+folder)
        print(files)
        file_name = os.listdir(files)
        c = 0
        for file in file_name:
            print(file)
            constituency_name = file
            df = pd.read_excel(file_path + '\\' + folder + '\\' + file)
            print(file_path + '\\' + folder + '\\' + file)
            # print(df)
            new_df = df.loc[:, ['First Name', 'Last Name', 'Mobile' ]]
            new_df['Last Name'] = new_df['Last Name'].fillna('')
            new_df['First Name'] = new_df['First Name'].astype(str)
            new_df['Last Name'] = new_df['Last Name'].astype(str)
            new_df['First Name'] = new_df['First Name'].str.strip()
            new_df['Last Name'] = new_df['Last Name'].str.strip()
            new_df['Full Name'] = new_df['First Name'] + ' ' + new_df['Last Name']
            selected_columns = ['Full Name', 'Mobile']
            result = new_df[selected_columns]
            result = result.rename(columns={'Full Name': 'Names'})
            print("l1", len(result))
            result.dropna(subset = ['Mobile'], inplace = True)
            result.dropna(subset = ['Names'], inplace = True)
            print("length", len(result))
            def clean_mobile_number(mobile):
                # Convert scientific notation to normal form
                if 'e' in str(mobile):
                    mobile = "{:.0f}".format(mobile)
                # Remove ".0" if it exists at the end
                mobile_str = str(mobile)
                if mobile_str.endswith('.0'):
                    mobile = mobile_str[:-2]
                return mobile
            result['Mobile'] = result['Mobile'].apply(clean_mobile_number)
            result['Mobile'] = result['Mobile'].astype('str')
            result['Mobile'] = result['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
            result['Mobile'] = result['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
            print("m", len(result))
            result.dropna(subset = ['Mobile'],ignore_index = True, inplace = True)
            print("original", len(result))
            # result = result.drop(df.columns[0], axis=1, inplace = True)
            result.to_excel(f"C:\\Users\\admin\\Desktop\\R\\Assembly_original\\Mahbubnagar_74\\{constituency_name}.xlsx",index=False)
            print("Filed stored successfully....")
            result.drop_duplicates(subset = ['Mobile'],ignore_index = True, inplace =True)
            result.to_excel(f"C:\\Users\\admin\\Desktop\\R\\Assembly_unique\\Mahbubnagar_74\\{constituency_name}.xlsx",index=False)
            print("unique", len(result))
            print("Filed stored successfully....")
            c = c+1
            print('*************************************************************************file_number',c)
end_time = time.time()
print("time :",end_time-start_time)





