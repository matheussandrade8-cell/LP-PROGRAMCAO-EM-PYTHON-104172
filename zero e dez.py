import os 
os.system("cls")
#inicio
Nota=float(input("digite sua nota:"))
notamax=10
notamin=0
#P
if Nota>=notamin and Nota <=notamax:
    mostre=(f"sua nota é {Nota} esta entre 10 e 0")
else:
    mostre=(f"sua nota {Nota} esta invalida deve estar entre 10 e 0")
#f
print(mostre)

