## Tento skript secte vsechny stejne tituly dohromady na základě rpzdělení na admin_sysno
## a připíše počet řádků, pro které se to počítalo
## To se pak ještě musí zprůměrovat v dalším skriptu

# admin_sysno,DayDifference,line_count
# 000680703,1980,937
# 001674701,9292,125
# 001309593,3093,113

import pandas as pd

data = pd.read_csv('C:/Users/milad/Desktop/Projekt Knihovna/Python Data/vysledek.csv')

# Převést sloupce "admin_serial" na řetězce
data['admin_serial'] = data['admin_serial'].astype(str).str.zfill(15)

# Extrahujte prvních 9 číslic z 'admin_serial' a pojmenujte je 'admin_sysno'
data['admin_sysno'] = data['admin_serial'].astype(str).str[:9]

# Převedení sloupce 'DayDifference' na číselný formát, pokud není již číselný
data['DayDifference'] = pd.to_numeric(data['DayDifference'], errors='coerce')

# Seskupte data podle 'admin_sysno' a sečtěte 'DayDifference' a 'line_count'
vysledek = data.groupby('admin_sysno').agg({'DayDifference': 'sum', 'line_count': 'sum'}).reset_index()
vysledek = vysledek.sort_values(by=['line_count', 'DayDifference'], ascending=[False, False])

# Uložte výsledek do CSV souboru
vysledek.to_csv('sectene_tituly.csv', index=False)

print(f"Výsledek byl uložen do souboru {'sectene_tituly.csv'}")
