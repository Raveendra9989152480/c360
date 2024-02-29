import pandas as pd
import os
import time

start_time = time.time()

file_path = r"C:\Users\admin\Desktop\R\Assembly_unique"
all_folders = os.listdir(file_path)
print(all_folders)
# constituency_name = 'West_Godavari'
for folder in all_folders:
    # print(folder)
    if folder == 'Mahbubnagar_74':
        files = os.path.join(file_path+'\\'+folder)
        print(files)
        file_name = os.listdir(files)
        result_df = pd.DataFrame()
        constituency_name = 'Mahbubnagar_74'
        o_u = 'unique'
        v_b = 'assembly'

        for file in file_name:
            print(file)
            df = pd.read_excel(file_path + '\\' + folder + '\\' + file)
            print(file_path + '\\' + folder + '\\' + file)
            # print(df)
            result_df = pd.concat([result_df,df], axis=0, ignore_index=True)
            print(len(result_df))
        print(result_df)
        print("Total_length", len(result_df))
        l = len(result_df)
        if l > 1000000:
            first_part = result_df.iloc[:1000000, :]
            second_part = result_df.iloc[1000000:, :]

            first_file_path = f"C:\\Users\\admin\\Desktop\\R\\Assembly_MP_unique\\Mahbubnagar_74\\{constituency_name}_MP_{v_b}_first_part_{o_u}.xlsx"
            first_part.to_excel(first_file_path, index=False)

            print("............................................first_part")

            second_file_path = f"C:\\Users\\admin\\Desktop\\R\\Assembly_MP_unique\\Mahbubnagar_74\\{constituency_name}_MP_{v_b}_second_part_{o_u}.xlsx"
            second_part.to_excel(second_file_path, index=False)
            print("............................................second_part")
        else:
            file_path = f"C:\\Users\\admin\\Desktop\\R\\Assembly_MP_unique\\Mahbubnagar_74\\{constituency_name}_MP_{v_b}_{o_u}.xlsx"
            result_df.to_excel(file_path, index=False)
            print("............................................Success")

            print('......................completed.......................')
end_time = time.time()
print("time :",end_time-start_time)
        # result_df.to_excel(f"C:\\Users\\admin\\Desktop\\R\\Beneficiary_MP_original\\Medak_34\\{constituency_name}_original.xlsx",index=False)

