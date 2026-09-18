import os
os.system("cls")

#inicio
idade = int(input("digite sua idade:"))

#Process
if idade < 16:
    voto= ("não pode voltar")
elif idade <=17:
    voto= ("voto opcional")
else:
    voto=("voto obrigatorio")

if idade >= 65:
    voto= ("voto opcional")

#fim.
print(voto)


