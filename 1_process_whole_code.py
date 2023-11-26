from utility import read_legenda, upravit_csv_soubor

# Vytvoření slovníku pro legendy
legenda_jazyk = read_legenda("LegendaLanguage.csv")             ## pro jazyk-misto.csv
legenda_obor = read_legenda("LegendaObor.csv")                  ## pro obory.scv
legenda_ctenar = read_legenda("LegendaStatusCtenare.csv")       ## pro ctenari.csv
legenda_zeme = read_legenda("LegendaCountry.csv")               ## pro jazyk-misto.csv

# Přidání hlaviček sloupečkům
jazyk_misto_header = ["bibli_sysno", "publ_place", "lang"]  ## pro spuštění se musí přidat dva řádky z utility
obory_header = ["bibli_sysno", "code_field"]
ctenari_header = ["date_birth", "sex", "date_registr_valid", "reader_status", "Id_No", "Id_type"]
vazba_bib_admin_header = ["bibli_sysno", "admin_sysno"]

# Vytvoření nového CSV souboru
upravit_csv_soubor("0_jazyk-misto.csv", "0_jazyk-misto_fixed.csv", jazyk_misto_header,
                  col_1_index=1, legend_1=legenda_zeme,
                  col_2_index=2, legend_2=legenda_jazyk
)

upravit_csv_soubor("0_obory.csv", "0_obory_fixed.csv", obory_header, 1, legenda_obor)
upravit_csv_soubor("0_ctenari.csv", "0_ctenari_fixed.csv", ctenari_header, 3, legenda_ctenar)
upravit_csv_soubor("0_vazba_bib_adm.csv", "0_vazba_bib_fixed.csv", vazba_bib_admin_header, -1, {})   ## není potřeba legenda

