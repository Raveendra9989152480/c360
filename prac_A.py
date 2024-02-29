import os
from indic_transliteration import sanscript
import pandas as pd
import re

file_path = r'C:\Users\admin\Desktop\R\Schemes\BD'
possible_column_names = ['mobile','contact','phone']
all_folders = os.listdir(file_path)
print('all_folders',all_folders)
beneficiary_names = ['Name of the Beneficiary', 'Beneficiary Name', 'PT_NAME', 'Name', 'BENEFICIARY_NAME','NAME_IN_AADHAR', 'Farmer Name',
                     'Name of the Beneficiary(Nominee of Deceased Farmer)']
PhoneNumbers = ['Mobile Number', 'Contact_Number', 'Contact Number', 'CONTACT_NO','Mobile NO',
                   'Phone Number','MOBILE_NUMBER','MOBILE','Phone number','Mobile No.']
constituency_name = 'Patancheru_40'
for folder in all_folders:
    # print('folder',folder)
    if folder == 'Patancheru_40':
        all_files_in_folder = os.listdir(file_path+'\\'+folder)
        # print(len(all_files_phone_nums))
        result_df = pd.DataFrame()
        for file in all_files_in_folder:
            print('file',file)
            # print('file',file)
            if file.endswith('.xlsx'):
                try:
                    for i in range(1,4):
                        df = pd.read_excel(file_path+'\\'+folder+'\\'+file,header=i)
                        print(file_path+'\\'+folder+'\\'+file)

                        selected_columns = [col for col in df.columns if
                                            col in PhoneNumbers or col in beneficiary_names]
                        filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                        column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                        column_mapping.update({col: 'Names' for col in beneficiary_names})
                        filtered_df.rename(columns=column_mapping, inplace=True)
                        print(filtered_df.columns)
                        # print(filtered_df)

                        if len(filtered_df.columns) == 2:
                            def is_telugu_word(word):
                                telugu_range = range(0x0C00, 0x0C7F)

                                for char in str(word):
                                    if ord(char) in telugu_range:
                                        mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
                                        if 'Ò' or 'È' in mod:
                                            mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
                                            mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
                                            mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
                                            mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
                                            return mod
                                        else:
                                            return mod
                                return word
                            filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)

                            def replace_m_with_n(input_string):
                                # Check if 'M' is at the starting index or next to a space
                                return re.sub(r'(^M|\sM)\b', r'\1', input_string.replace('M', 'n'))
                            filtered_df['Names'] = filtered_df['Names'].apply(replace_m_with_n)
                            def replace_z_with_s(input_string):
                                # Replace both 'Z' and 'z' with 'S' and 's', respectively
                                output_string = input_string.replace('Z', 'S').replace('z', 's')
                                return output_string
                            filtered_df['Names'] = filtered_df['Names'].apply(replace_z_with_s)
                            print(filtered_df)
                            filtered_df = filtered_df.dropna()


                            def replace_X_with_ksh(input_string):
                                # Replace both 'Z' and 'z' with 'S' and 's', respectively
                                output_string = input_string.replace('X', 'ksh').replace('x', 'ksh')
                                return output_string


                            filtered_df['Names'] = filtered_df['Names'].apply(replace_X_with_ksh)

                            def extract_alphabets_and_spaces(values):
                                value = str(values)
                                return re.sub(r'[^a-zA-Z\s]', '', value)
                            filtered_df['Names'] = filtered_df['Names'].apply(
                                extract_alphabets_and_spaces)
                            print(len(filtered_df))
                            result_df = pd.concat([result_df, filtered_df],axis=0, ignore_index=True)

                        else :
                            pass
                except Exception as E:
                    print('exception...', E)
            if file.endswith('.csv'):
                try:
                    df = pd.read_csv(file_path+'\\'+folder+'\\'+file)
                    print(file_path+'\\'+folder+'\\'+file)
                    selected_columns = [col for col in df.columns if
                                        col in PhoneNumbers or col in beneficiary_names]
                    filtered_df = df[selected_columns].copy()  # Create a copy to avoid SettingWithCopyWarning
                    column_mapping = {col: 'Mobile' for col in PhoneNumbers}
                    column_mapping.update({col: 'Names' for col in beneficiary_names})
                    filtered_df.rename(columns=column_mapping, inplace=True)
                    print(filtered_df.columns)
                    # print(filtered_df)
                    if len(filtered_df.columns) == 2:
                        def is_telugu_word(word):
                            telugu_range = range(0x0C00, 0x0C7F)
                            for char in str(word):
                                if ord(char) in telugu_range:
                                    mod = sanscript.transliterate(word, sanscript.TELUGU, sanscript.HK)
                                    if 'Ò' or 'È' in mod:
                                        mod = ''.join(['O' if letter == 'Ò' else letter for letter in mod])
                                        mod = ''.join(['E' if letter == 'È' else letter for letter in mod])
                                        mod = ''.join(['e' if letter == 'è' else letter for letter in mod])
                                        mod = ''.join(['o' if letter == 'ò' else letter for letter in mod])
                                        return mod
                                    else:
                                        return mod
                            return word
                        filtered_df['Names'] = filtered_df['Names'].apply(is_telugu_word)

                        def replace_m_with_n(input_string):
                            # Check if 'M' is at the starting index or next to a space
                            return re.sub(r'(^M|\sM)\b', r'\1', input_string.replace('M', 'n'))
                        filtered_df['Names'] = filtered_df['Names'].apply(replace_m_with_n)
                        def replace_z_with_s(input_string):
                            # Replace both 'Z' and 'z' with 'S' and 's', respectively
                            output_string = input_string.replace('Z', 'S').replace('z', 's')
                            return output_string
                        filtered_df['Names'] = filtered_df['Names'].apply(replace_z_with_s)

                        def replace_X_with_ksh(input_string):
                            # Replace both 'Z' and 'z' with 'S' and 's', respectively
                            output_string = input_string.replace('X', 'ksh').replace('x', 'ksh')
                            return output_string
                        filtered_df['Names'] = filtered_df['Names'].apply(replace_X_with_ksh)

                        print(filtered_df)
                        filtered_df = filtered_df.dropna()
                        print(len(filtered_df))


                        def extract_alphabets_and_spaces(values):
                            value = str(values)
                            return re.sub(r'[^a-zA-Z\s]', '', value)


                        filtered_df['Names'] = filtered_df['Names'].apply(
                            extract_alphabets_and_spaces)
                        result_df = pd.concat([result_df, filtered_df], axis=0,ignore_index=True)

                    else:
                        pass
                except Exception as E:
                    print('exception...',E)
        print("result_df",result_df)

        # result_df['Mobile'] = result_df['Mobile'].apply(lambda x:"{:.0f}".format(x) if 'e' in x else x)
        # result_df['MOBILE_NO'] = result_df['MOBILE_NO'].apply(lambda x: x[:-2 if x.endswith('.0') else x)
        def clean_mobile_number(mobile):
            # Convert scientific notation to normal form
            if 'e' in str(mobile):
                mobile = "{:.0f}".format(mobile)
            # Remove ".0" if it exists at the end
            mobile_str = str(mobile)
            if mobile_str.endswith('.0'):
                mobile = mobile_str[:-2]
            return mobile
        result_df['Mobile'] = result_df['Mobile'].apply(clean_mobile_number)
        result_df['Mobile'] = result_df['Mobile'].astype('str')
        result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
        result_df['Mobile'] = result_df['Mobile'].apply(lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
        result_df = result_df.dropna(subset=['Mobile'])
        result_df = result_df.dropna()
        result_df.to_excel(f'C:\\Users\\admin\\Desktop\\R\\Beneficiary_original\\Medak_34\\{constituency_name}_o_beneficiary_scheme.xlsx',index=False)
        print("success..")
        result_df = result_df.drop_duplicates(subset=['Mobile'])
        result_df = result_df.dropna(subset=['Mobile'])
        result_df = result_df.dropna()
        print("result_df",result_df)
        print("result_df",len(result_df))
        result_df.to_excel(f'C:\\Users\\admin\\Desktop\\R\\Beneficiary_unique\\Medak_34\\{constituency_name}_u_beneficiary_scheme.xlsx',index=False)
        print("success..")

