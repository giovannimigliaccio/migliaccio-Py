#Nome=input("come ti chiami?")
#print(Nome)

#cognome=input("dimmi il tuocognome")
#print(Nome, cognome)

#print("carrateri del nome",len(Nome))
#print("caratteri del cognome",len(cognome))


#numero1=input("dimmi la prima cifra: ")
#numero2=input("dimmi la seconda cifra: ")
#if numero1>numero2:
 #   print(numero2, numero1)
#else:
    #print(numero1, numero2)


#nome=input("dimmi il tuo nome: ")
#for x in range(3):
    #print(nome)


import json 

libri = {

    "scienze" : {"titolo":"La_nuova_biologia","autore":"David_Sadava","casa editrice":"Zanichelli"},
    "matematica" : {"titolo":"matematica_multimeddiale","autore":"Massimo Bergamini","casa editrice":"Zanichelli"},
    "poesia" : {"titolo":"leggere_a_colori","autore":"Alberta_Mariotti","casa editrice":"G_D_ANNA"},
    "geostoria" : {"titolo":"le_pietre_parlano","autore":"Mauro_Reali","casa editrice":"ldscher"},
    "latino_di_seconda" : {"titolo":"mirum_iter","autore":"Angelo_Diotti","casa editrice":"pearson"},
    "latino_di_prima" : {"titolo":"mirum_iter","autore":"Angelo_Diotti","casa editrice":"pearson"},
    "inglese_madre_lingua" : {"titolo":"gold_preliminary","autore":"Sally_Burges","casa editrice":"pearson"},
    "inglese" : {"titolo":"perfomer_B1","autore":"Marina_Tavella","casa editrice":"pearson"},
    "geostoria" : {"titolo":"le_pietre_parlano","autore":"Mauro_Reali","casa editrice":"Zanichelli"},
    "scritura" : {"titolo":"leggere_a_colori","autore":"Alberta Mariotti","casa editrice":"G_D_ANNA"},   
}

#json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
#allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

with open("data.json", "w") as f:
    json.dump(libri, f)

f.close()


with open("data.json", "r") as f:
    libri_da_file = json.load(f)

f.close()

print("stampa il file intero: ",libri_da_file)



