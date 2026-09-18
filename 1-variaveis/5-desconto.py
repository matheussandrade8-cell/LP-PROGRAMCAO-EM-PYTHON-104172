import os

#Limpa o terminal.
os.system("cls")

print("= SOLICITANDO DADOS = ")
valor = float(input("digite o valor: "))

#Calculando.
#Desconto 10%
Desconto = valor *0.10
valor_com_desconto = valor - Desconto

print("\n= EXEBINDO DADOS =")
print("valor com desconto de 10%: ", valor_com_desconto)
