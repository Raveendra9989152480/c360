import pandas as pd
from indic_transliteration import sanscript
import time
import re
start_time = time.time()

# # constituency = "Nizamabad"
df = pd.read_excel(r"C:\Users\admin\Desktop\ravi\left_over_data\Adilabad_7\Adilabad_7_leftoverdata.xlsx")
print(df)
# print(len(df))
# df.dropna(subset = ['Names'],ignore_index=True, inplace=True)
# print(len(df))
# df.drop_duplicates(subset = ['Mobile'],ignore_index=True, inplace=True)
df["Names"]=df["Names"].astype(str)
df["Names"]=df["Names"].str.lower()

def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)

# Apply the function to the "name" column
df['Names'] = df['Names'].apply(extract_alphabets_and_spaces)

def replace_z_with_s_q_with_k(input_string):
    # Replace both 'Z' and 'z' with 'S' and 's', respectively
    output_string = input_string.replace('z', 'j').replace('q', 'k')
    return output_string

df['Names'] = df['Names'].apply(replace_z_with_s_q_with_k)

def add_h_after_f(name):
    if name.startswith('f'):
        name = 'ph'+name[1:]
        return name
    else:
        return name

df['Names'] = df['Names'].apply(add_h_after_f)

# Function to transliterate English names to Telugu script
def transliterate_to_telugu(name):
    telugu_name = sanscript.transliterate(name, sanscript.ITRANS, sanscript.TELUGU)
    return telugu_name

# Apply the transliteration function to the 'Names' column and create a new 'Telugu_Names' column
df['Telugu_Names'] = df['Names'].apply(transliterate_to_telugu)

df = df[['Names','Telugu_Names','Mobile']]

# print("final",df)
# df.to_excel(f"C:\\Users\\jaswa\\Desktop\\TS\\LOD_to telugu_names\\Nizamabad\\{constituency}_english_to_telugu.xlsx", index=False)

# print("################################################CONSTITUENCY", constituency)
df["Names"]=df["Names"].str.title()
df.to_excel("t1.xlsx",index=False)
end_time  = time.time()
print(end_time-start_time)


#path = 'siddipet_leftover_data.xlsx'
#selected_columns.to_excel(path, index=False)
# Display the DataFrame with the new column

#lod = pd.read_excel(r"C:\Users\admin\Desktop\siddepet_constituency\LeftOverData.xlsx")
# unn = pd.read_excel(r"C:\Users\admin\Desktop\siddepet_constituency\Uniques_English_Telugu_Phone.xlsx")
#
# #lod_1 = lod[['Names','Telugu_Names','Mobile_Numbers']]
# unn_1 = unn[['Names','Telugu_Names','Mobile_Numbers']]
#
# l_u = pd.concat([unn_1,selected_columns], ignore_index=False)
#
# l_u = l_u.drop_duplicates(subset = ['Mobile_Numbers'],keep = 'first')







