## Vezme soubor sectene_tituly.csv, počet řádků, celkové dny a zprůměruje to. 
## Jsou to  tituly
## taky se to může řadit dle různých sloupců

# admin_sysno,DayDifference,line_count,average
# 000093868,359,1,359.0
# 000898736,357,1,357.0
# 001766938,355,1,355.0

import pandas as pd

data = pd.read_csv('C:/Users/milad/Desktop/Projekt Knihovna/Python Data/5_sectene_tituly.csv')

# Převést sloupce "admin_sysno" na řetězce
data['admin_sysno'] = data['admin_sysno'].astype(str).str.zfill(9)

# Vytvoření sloupce 'average' s průměrem hodnot z 'DayDifference' a 'line_count'
data['average'] = (data['DayDifference'] / data['line_count']).round()

# Seřazení DataFrame podle sloupce: DayDifference,line_count = request,average od nejvyššího
data = data.sort_values(by='DayDifference', ascending=False)

# Uložení změn zpět do souboru, pokud chcete
data.to_csv('prumer_DayDifference.csv', index=False)

print(f"Výsledek byl uložen do souboru.")
