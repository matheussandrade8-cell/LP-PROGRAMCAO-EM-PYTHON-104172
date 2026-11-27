from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class fornecedor:
    nome:str
    email:str
    telefone:str
    endereço:str

lista_fornecedor=[]

print(" = coletando dados = ")

for  i in range(2):
    novo_fornecedor = fornecedor(
        nome=input("Digite seu nome:"),
        email=input("Digite seu email:"),
        telefone=input("Digite seu telefone:"),
        endereço=input("Digite seu endereço:",)
    )
    lista_fornecedor.append(novo_fornecedor)

arquivo= "dados_fornecedor.csv"
with open(arquivo, "a") as arquivo_fornecedor:
    for fornecedor in lista_fornecedor:
        arquivo_fornecedor.write(f"{fornecedor.nome}, {fornecedor.email}, {fornecedor.telefone}, {fornecedor.endereço}\n")

print(" = Dados do fornecedor salvo = ")