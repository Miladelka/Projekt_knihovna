## toto spojí obory sice, ale neodstraní duplikáty, protože řádky nejsou duplikátní. 
## je rozdíl ve sloupci field_code

import csv
from collections import defaultdict

input_filename = "34_rezervace_obor_duplicity.csv"
output_filename = "36_rezervace_duplicity.csv"

# Čtení dat ze vstupního CSV souboru
with open(input_filename, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# Vytvoření nového sloupce "field_code2"
field_code2_dict = defaultdict(list)

for row in rows:
    field_code2_dict[row['line_number']].extend(filter(None, row['field_code'].split(', ')))

# Přidání sloupce "field_code2" zpět k původním řádkům
for row in rows:
    row['field_code2'] = ', '.join(field_code2_dict[row['line_number']])

# Uložení výsledných dat do nového CSV souboru
fieldnames = reader.fieldnames + ['field_code2']
with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)