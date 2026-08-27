import os
os.system("cls")

print(" = Solicitando dados = ")

#Entrada
primeiro_numero = int(input("digite o primerio numero: "))
segundo_numero  = int(input("digite o segundo numero: "))

#Processamento
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

#saida
print("\n= Exebindo dados = ")
print("soma: ", soma)
print("subtracao: ", subtracao)
print("multiplicacao: ", multiplicacao)
print("divisao: ", divisao)
