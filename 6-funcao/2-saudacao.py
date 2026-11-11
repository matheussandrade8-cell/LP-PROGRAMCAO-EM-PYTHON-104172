import os
os.system("cls")

def mostrar_saudacao(nome, idade):
    print(f"{nome} tem {idade} anos. ")

print("= Solicitando Dados = ")
nome=input("digite o nome:")
idade=input("digite sua idade:")

print(" = Exebindo o dados =")
mostrar_saudacao(nome, idade)#chamando a funçaão
