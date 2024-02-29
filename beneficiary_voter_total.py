import pandas as pd
import time
start_time = time.time()

df1= pd.read_excel(r"C:\Users\admin\Desktop\R\Assembly_MP_unique\Mahbubnagar_74\Mahbubnagar_74_MP_assembly_unique.xlsx")
df2=pd.read_excel(r"C:\Users\admin\Desktop\R\Beneficiary_MP_unique\Mahbubnagar_74\Mahbubnagar_74_MP_beneficiary_unique.xlsx")
#df3 =pd.read_excel(r"C:\Users\admin\Desktop\R\Beneficiary_MP_original\Mahabubabad_102\Mahabubabad_102_MP_beneficiary_second_part_unique.xlsx")
constituency="Mahbubnagar_74"


print(len(df1))
print(len(df2))
#print(len(df3))

df = pd.concat([df1,df2],ignore_index=True)
print("l1", len(df))
df.dropna(subset=['Mobile','Names'], ignore_index=True,inplace=True)
print("l2", len(df))
df.drop_duplicates(subset=['Mobile'], ignore_index=True,inplace=True)
#print("l3", len(df))

l = len(df)
if l > 1000000:
    first_part = df.iloc[:1000000, :]
    second_part = df.iloc[1000000:, :]

    first_file_path = f"C:\\Users\\admin\\Desktop\\R\\Beneficiary_voter_mp_data\\Mahbubnagar_74\\{constituency}_Total_data_part1.xlsx"
    first_part.to_excel(first_file_path, index=False)

    print("............................................first_part")

    second_file_path = f"C:\\Users\\admin\\Desktop\\R\\Beneficiary_voter_mp_data\\Mahbubnagar_74\\{constituency}_Total_data_part2.xlsx"
    second_part.to_excel(second_file_path, index=False)
    print("............................................second_part")
else:
    file_path =f"C:\\Users\\admin\\Desktop\\R\\Beneficiary_voter_mp_data\\Mahbubnagar_74\\{constituency}_Total_data.xlsx"
    df.to_excel(file_path, index=False)
    print("............................................Success")

    print('......................completed.......................')
