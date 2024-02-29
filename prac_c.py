from indic_transliteration import sanscript
import pandas as pd
import re

file_path =r"C:\Users\admin\Desktop\RAJA\Schemes\BD\Medak_34\MEDAK_98836_RB_BenfData_Rytu Bandhu.xlsx"
for i in range(1, 4):
    df = pd.read_excel(file_path,header=i, usecols=['Name of the Beneficiary','Mobile Number'])
    if 'Unnamed' in df.columns.to_list():
        pass
    else:
        break
print(df.columns)
print(df)
def is_telugu_word(word):
    telugu_range = range( 0x0C00, 0x0C7F)

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

df['Name of the Beneficiary'] = df['Name of the Beneficiary'].apply(is_telugu_word)
print(df)

def replace_m_with_n(input_string):
    # Check if 'M' is at the starting index or next to a space
    return re.sub(r'(^M|\sM)\b', r'\1', input_string.replace('M', 'n'))
df['Name of the Beneficiary'] = df['Name of the Beneficiary'].apply(replace_m_with_n)


def replace_z_with_s(input_string):
    # Replace both 'Z' and 'z' with 'S' and 's', respectively
    output_string = input_string.replace('Z', 'S').replace('z', 's')
    return output_string
df['Name of the Beneficiary'] = df['Name of the Beneficiary'].apply(replace_z_with_s)

def extract_alphabets_and_spaces(values):
    value = str(values)
    return re.sub(r'[^a-zA-Z\s]', '', value)
df['Name of the Beneficiary'] = df['Name of the Beneficiary'].apply(extract_alphabets_and_spaces)
print(df)