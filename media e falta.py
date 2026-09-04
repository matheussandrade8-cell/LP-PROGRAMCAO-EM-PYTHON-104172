import os
os.system("cls")

#inicio>
media=float(input("digite sua media:"))
faltas=int(input("digite quantas faltas voce teve:"))

#process.

if media<7 and faltas>40:
    Resultado= ("voce foi reprovado")
else:
    Resultado= ("voce foi aprovado")

#fim
print(Resultado)