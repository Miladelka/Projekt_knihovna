## Vezme soubor se spojenými sloupci, odstraní sloupec field_code, a pak odstraní duplikátní řádky
## slouží i pro rezervace a výpůjčky


# line_number,admin_serial,date_borrow,hour_borrow,date_deadline,date_return,hour_return,unit_satus,Id_No,admin_sysno,serial_No,bibli_sysno,publ_place,lang,field_code,field_code2
# 1,000545258000010,20230628,0946,20230707,20230628,1828,Studovna,00176105543566,000545258,000010,000545258,Czech Republic,Czech,Beletrie,Beletrie
# 2,001642258000010,20230424,1144,20230505,20230506,1633,Studovna,00055836240542,001642258,000010,001606468,Czech Republic,Czech,Sociologie,"Sociologie, Vychova a vzdelavani"

import csv

# Načtení výsledného CSV souboru "spojene_obory.csv"
with open('36_rezervace_duplicity.csv', 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    data = list(reader)

# Odstranění sloupce 'field_code'
for row in data:
    del row['field_code']

# Odstranění duplikátních řádků
unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]

# Seřazení výsledných dat podle sloupce 'line_number'
sorted_data = sorted(unique_data, key=lambda x: int(x['line_number']))

# Uložení výsledného seznamu slovníků do nového CSV souboru "vysledek.csv"
fieldnames = reader.fieldnames[:-1] + ['field_code2']  # Přidání 'field_code2' do seznamu názvů sloupců
with open('Rezervace_komplet.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sorted_data)



