import pandas as pd

def compare_csv(file1, file2):
    # Načtení CSV souborů do pandas DataFrame
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Porovnání DataFrame
    are_equal = df1.equals(df2)

    if are_equal:
        print("CSV soubory jsou stejné.")
    else:
        print("CSV soubory nejsou stejné.")

# Nastavte cesty k souborům
file_path1 = 'spojene_obory1a.csv'
file_path2 = 'spojene_obory1b.csv'

# Porovnejte soubory
compare_csv(file_path1, file_path2)
