import os
#limpa o terminal>

os.system("cls")

#SOLICITANDO DADOS
# intput adiciona o que for digitado no terminal na variavel como texto.
nome= input("digite seu nome: ")
sobrenome=input("digite seu sobrenome: ")

#int() converte o que foi digitado em inteiro (numero inteiro)
idade= int(input("digite sua idade: ") )

#float() converte o que foi digitado em float (numero reais)
peso= float(input("digite seu peso: "))
altura=float(input("digite sua altura: "))

#MOSTRANDO DADOS.
print("nome:  ", nome)
print("sobrenomw: ", sobrenome)
print("idade: ", idade)
print("peso: ", peso)
print("altura: ", altura)