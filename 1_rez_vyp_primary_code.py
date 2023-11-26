# Skript pro výpočet celkového počtu dnů pro každou vyzvednutou rezervaci - výtisky
# Přidán sloupec s celkovým počtem požadavků pro jednotlivý výtisk

# admin_serial,line_count,DayDifference
# 001663038000020,33,5108
# 001802549000020,30,4189
# 001841124000020,24,2837

import pandas as pd

# use , as separator
data = pd.read_csv('C:/Users/milad/Desktop/Projekt Knihovna/Python Data/Rezervace_vypujcky_kombi.csv', delimiter=',')

# convert columns to datetime
data['date_request'] = pd.to_datetime(data['date_request'], format='%Y%m%d')
data['date_borrow'] = pd.to_datetime(data['date_borrow'], format='%Y%m%d')

# Převést sloupce "admin_sysno" a "admin_serial" na řetězce
data['admin_sysno'] = data['admin_sysno'].astype(str).str.zfill(15)
data['admin_serial'] = data['admin_serial'].astype(str).str.zfill(15)

result = data[data['date_request'] <= data['date_borrow']]
result = result[result['Id_No'] != "XXXXXX"]

result["diff"] = (result['date_borrow'] - result['date_request']).dt.days
result = result.loc[result.groupby(['Id_No', 'admin_serial', 'date_borrow'])['diff'].idxmin()]
result = result.loc[result.groupby(['Id_No', 'admin_serial', 'date_request'])['diff'].idxmin()]

# Přidání sloupce "pocet_requestu" s počtem řádků v každé skupině
result['pocet_requestu'] = result.groupby(['Id_No', 'admin_serial', 'date_borrow'])['diff'].transform('count')

# Uložíme do souboru 'mezi_vysledek.csv'
result.to_csv('mezi_vysledek.csv', index=False)

# Skupinový výpočet DayDifference a uložení do 'vysledek.csv'
result_grouped = result.groupby('admin_serial').agg({'date_borrow': 'count', 'DayDifference': 'sum'})
result_grouped = result_grouped.rename(columns={'date_borrow': 'line_count'})
result_grouped = result_grouped.reset_index()

result_grouped = result_grouped.sort_values(by='DayDifference', ascending=False)

result_grouped.to_csv('vysledek.csv', index=False)

print(f"Výsledek byl uložen do souboru")



    