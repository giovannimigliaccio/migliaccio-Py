stringa = input (“qual è la parola di cui vuoi sapere le lettere? = “)
stringa1 = list(stringa)
print(stringa1)
alphabet = (‘abcdefghijklmnopqrstuwxyz’)
alphabet1 = list(alphabet)

lista = {}
for alphabet1 in stringa1:
      if stringa1.count(alphabet) > 0:
           lista[(alphabet1, stringa1.count(alphabet))]= 0
print(“le lettere della tua parola sono:” , lista)


