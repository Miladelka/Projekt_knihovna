import csv

from utility import read_legenda

def upravit_csv_soubor(input_file, output_file, columns, col_index, legend):
    # Otevření vstupního souboru CSV pro čtení
    with open(input_file, mode="r", errors="ignore") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="@")
        next(csv_reader)
        
        # Seznam pro ukládání nových řádků
        new_line_list = []

        for row in csv_reader:
            if len(row) != len(columns):
                continue
            new_line = {}
            for index, column in enumerate(columns):
                if column.startswith("hour"):
                    value = row[index].strip().zfill(4)
                else:
                    value = row[index].strip()
                                            
                new_line[column] = value
                
                if column =="adSys_serNo":
                    new_line["admin_sysno"] = value[:9]
                    new_line["serial_No"] = value[9:]
               
                
                if index == col_index:
                    value_new = legend.get(value, value)
                else:
                    value_new = value
                new_line[column] = value_new
                 
            new_line_list.append(new_line)
            
    # Otevření výstupního souboru CSV pro zápis
    with open(output_file, mode='w', newline='') as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=columns + ["admin_sysno", "serial_No"],
            delimiter=";"
        )

        # Zápis nových dat do výstupního souboru
        csv_writer.writeheader()
        for row in new_line_list:
            csv_writer.writerow(row)
    print("Soubor zapsán.", output_file)

vypujcky_header = ["adSys_serNo", "date_borrow", "hour_borrow", "date_deadline", "date_return", "hour_return", "unit_satus", "Id_No"]


# Vytvoření slovníku pro legendy
legenda_vypujcky = read_legenda("LegendaStatusJednotky.csv")

# Vytvoření nového CSV souboru
upravit_csv_soubor("0_vypujcky.csv", "0_vypujcky_fixed.csv", vypujcky_header, 6, legenda_vypujcky)   
  
 
                  
