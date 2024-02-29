# import pandas as pd
# df=pd.read_excel(r"C:\Users\admin\Downloads\HH data guntur Nethanna Neshtam.xlsx")
# df["Schemes"]=[ if i  pd.isnull for i in df.columns ]
# print(df.columns)


import pandas as pd

# Load your Excel file into a DataFrame
df = pd.read_excel(r"C:\Users\admin\Downloads\HH Data Guntur.xlsx")

# Select required columns
df = df[['CITIZEN_NAME','MOBILE',
       'Jagananna Vidya Deevena', 'Jagananna Vasathi Deevena',
       'Ryuthu Bharosa', 'Crop Insurance', 'Sunna Vaddi Panta Runalu',
       'Input Subsidy to Farmers', 'Matsyakara Bharosa',
       'YSR Cheyutha', 'Aasara', 'Sunna Vodi',
       'KalyanaMasthu', 'YSR Arogyasri', 'YSR ArogyaAsara', 'Housing (DBT)',
       'YSR Bhima',  'Nethanna Neshtam', 'Chedodu',
       'Covid Assist', 'Jagananna Thodu (Interest)', 'Housesites',
       'VidyaKanuka', 'Tab', 'Gorumudda',
       'YSR SampoornaPoshana']]

# Create an empty list to store scheme names
schemes = []

# Iterate over each row
for index, row in df.iterrows():
    # Initialize an empty list for the current row's schemes
    row_schemes = []
    # Iterate over each column except for 'CITIZEN_NAME' and 'MOBILE'
    for col in df.columns.difference(['CITIZEN_NAME', 'MOBILE']):
        # If the value in the current column is not NaN (not null), add the column name to row_schemes
        if not pd.isnull(row[col]):
            row_schemes.append(col)
    # Join the list of schemes for the current row into a comma-separated string
    schemes.append(', '.join(row_schemes))

# Add the 'Schemes' column to the DataFrame
df['Schemes'] = schemes
df=df[['CITIZEN_NAME','MOBILE','Schemes' ]]
print("l1",len(df))
df.drop_duplicates(subset=["CITIZEN_NAME",'MOBILE'],inplace = True)
# Save the DataFrame to a new Excel file
print("l2",len(df))
df.dropna(subset=['Schemes'],inplace=True)
print("l3",len(df))
df.to_excel("HH_Data_Guntur_Schemes_in_one(2).xlsx", index=False)

