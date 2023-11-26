import pandas as pd

# Nahrání CSV souboru do pandas DataFrame
df = pd.read_csv('Vypujcky_jazyk_radek.csv')

# Zjištění duplikátních řádků
duplicate_rows = df[df.duplicated()]

# Uložení duplikátních řádků do výstupního CSV souboru
duplicate_rows.to_csv('duplikaty.csv', index=False)
