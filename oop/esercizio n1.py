'''
Python3
Programmazione ad oggetti
'''

class computer:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, colore):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.colore = colore
        
        

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n colore: {self.colore}\n assicurazione: ' 
    
giovanni = computer("giovanni","asus","PC portatile", "nero")

marco = computer("marco","acer","PC fisso",  "verde")

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)

print("\nLa singola scheda è:")
print (giovanni.scheda())
print (marco.scheda())
print("\ncomputer totali: ")

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(giovanni.__dict__)
print(marco.__dict__)