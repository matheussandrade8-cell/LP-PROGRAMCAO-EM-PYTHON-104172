from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome:str
    idade:int
    altura:float

quantidade_cliente=2
lista_cliente=[]

for i in range(quantidade_cliente):
    novo_cliente = cliente(
        nome=input("digite seu nome:"),
        idade=int(input("digite sua idade:")),
        altura=float(input("digite sua altura:"))
    )
    lista_cliente.append(novo_cliente)

#salvando arquivo
arquivo= "dados_cliente.csv"
with open(arquivo, "a") as arquivo_cliente:
    for cliente in lista_cliente:
        arquivo_cliente.write(f"{cliente.nome}, {cliente.idade}, {cliente.altura}\n")

print("cliente Salvo com sucesso")