import csv

def read_legenda(file_path):  ## Toto je fce pro csv legendy, vytvoří se z nich slovník
    legenda_status = {}
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:  ## neprování se konverze na znak nového řádku
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # Přeskočení hlavičky
        
        for row in csv_reader:  ## projde každý řádek v souboru
            status_id, status_name = row  ## rozložení aktuálního řádku na dvě hodnoty
            
            # if len(status_id) == 2:           ## tyto dva řádky se spouští jen pro jazyk-misto.csv
            #     status_id = status_id + "-"
            legenda_status[status_id] = status_name  ## Přidání páru "status_id" jako klíče a "status_name" jako hodnoty do slovníku legenda_status
               
    return legenda_status  ## Vrací vytvořený slovník legenda_status
    

def upravit_csv_soubor(input_file, output_file, columns, col_1_index, legend_1, col_2_index=None, legend_2=None):
    # Otevření vstupního souboru CSV pro čtení
    with open(input_file, mode='r', errors="ignore") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="@")
        next(csv_reader)
        
        # Seznam pro ukládání nových řádků
        row_dictionaries = []

        for row in csv_reader:
            row_dict = {}
            
            for index, column in enumerate(columns):
                if index >= len(row):
                    break
                if column.startswith("hour"):
                    value = row[index].strip().zfill(4)
                else:
                    value = row[index].strip()
                    
                if column == "serial_No":
                    value = row[index].strip().zfill(6)       
                                                              
                if index == col_1_index and legend_1:
                    value = legend_1.get(value, value)
                if index == col_2_index and legend_2:
                    value = legend_2.get(value, value)
                #     
                row_dict[column] = value
                
            if "admin_serial" in columns:
                row_dict["admin_serial"] = row_dict["admin_sysno"] + row_dict["serial_No"]
                
            row_dictionaries.append(row_dict)

    # Otevření výstupního souboru CSV pro zápis
    with open(output_file, mode='w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=columns, delimiter=";")
    
        # Zápis nových dat do výstupního souboru
        csv_writer.writeheader()
        for row_dict in row_dictionaries:
            csv_writer.writerow(row_dict)
    print("Soubor zapsán.", output_file)