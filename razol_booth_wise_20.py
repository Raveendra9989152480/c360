import pandas as pd
from googletrans import Translator
df=pd.read_excel(r"C:\Users\admin\Downloads\Razole-45-AC- iToC Voter Data.xlsx",usecols=["B#","First Name","Age","Mobile"])
#print("no of columns",len(df))
def clean_mobile_number(mobile):
    # Convert scientific notation to normal form
    if 'e' in str(mobile):
        mobile = "{:.0f}".format(mobile)
    # Remove ".0" if it exists at the end
    mobile_str = str(mobile)
    if mobile_str.endswith('.0'):
        mobile = mobile_str[:-2]
    return mobile


df['Mobile'] = df['Mobile'].apply(clean_mobile_number)
df['Mobile'] = df['Mobile'].astype('str')
df['Mobile'] = df['Mobile'].apply(lambda x: x[2:] if len(x) > 10 and x.startswith('91') else x)
df['Mobile'] = df['Mobile'].apply(
    lambda x: x[:] if x.startswith(('6', '7', '8', '9')) and len(x) == 10 else None)
df.dropna(subset=['Mobile'], ignore_index=True, inplace=True)
df.dropna(subset=["Mobile"],inplace=True)
#print("no of columns after deleting blank spaces",len(df))
df.drop_duplicates(subset="Mobile",inplace=True)
df=df.groupby("B#").head(20)
def translate_to_telugu(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='te')
    return translated.text
df["Telugu_name"]=df["First Name"].apply(translate_to_telugu)
#df.to_excel("razol_booth_wise_data_1.xlsx",index=False)



