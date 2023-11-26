## Spojení tabulek sectene_tituly s bibli_sysnem a názvy oborů, jazyky

# admin_sysno,DayDifference,line_count,bibli_sysno,unit_status,publ_place,lang,field_code2
# 000181916,311,1126,000181916,Studovna periodik,Czech Republic,Czech,
# 000680703,1980,937,,Skupinova studovna,,,
# 000181893,386,757,000181893,Studovna periodik,Czech Republic,Czech,


import pandas as pd

# Načtení dat z CSV souborů do DataFrame
df1 = pd.read_csv('C:/Users/milad/Desktop/Projekt Knihovna/Python Data/5_sectene_tituly.csv')
df2 = pd.read_csv('C:/Users/milad/Desktop/Projekt Knihovna/Python Data/0_Rezervace_vypujcky_kombi.csv')

# Spojení na základě sloupce admin_sysno
merged_df = pd.merge(df1, df2[['admin_sysno', 'bibli_sysno', 'unit_status', 'publ_place', 'lang', 'field_code2']], on='admin_sysno', how='left')

# Odebrání případných duplikátů
merged_df = merged_df.drop_duplicates(subset='admin_sysno', keep='first')

# Specifikace formátu sloupce admin_sysno při exportu
merged_df['admin_sysno'] = merged_df['admin_sysno'].apply(lambda x: f"{int(x):09d}" if pd.notna(x) else x)

# Specifikace formátu sloupce bibli_sysno při exportu
merged_df['bibli_sysno'] = merged_df['bibli_sysno'].apply(lambda x: f"{int(x):09d}" if pd.notna(x) else x)

# Exportování spojených dat do CSV souboru
merged_df.to_csv('vystup00.csv', index=False)

print(f"Výsledek byl uložen do souboru.")