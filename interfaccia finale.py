from guizero import *
import matplotlib.pyplot as plt
def get_file():
    global filename
    filename = app.select_file()



def grafico():
    f = open("dati.txt", 'r')

    coordX = [f]
    coordY = [f]

    # da notare che posso fare un ciclo all'interno di un file
    # direttamente sulle righe

    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    print("liste ordinate:") 
    print ("X: ",coordX)
    print ("Y: ",coordY)

    # stampo il tipo di dati delle coordinate
    print(type(coordX))
    print(type(coordY))

    # ora sono pronte per essere usate anche nei grafici

    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()
app = App(title="INTERFACCIA GRAFICA")
output = TextBox(app, width=80, height=10, multiline=True)
etichettaA = Text(app, text="scrivi dati.txt")
paramA = TextBox(app)

pushB = PushButton(app, text="apri file",command=get_file)
pushA = PushButton(app, text="Genera grafico",command=grafico)
app.display()