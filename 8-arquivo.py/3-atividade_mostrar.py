from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str


lista_fornecedor=[]

arquivo="dados_fornecedor.csv"
with open (arquivo, "r" ) as arquivo_fornecedor:
    for linha in arquivo_fornecedor:
        nome, email, telefone, endereco= linha.strip().split(",")
        lista_fornecedor.append(fornecedor(
            nome=nome,
            email=email,
            telefone=telefone,
            endereco=endereco
        ))

print(" = Exebindo Dados = ")
for fornecedor in lista_fornecedor:
    print(f"nome:{fornecedor.nome}")
    print(f"email:{fornecedor.email}")
    print(f"telefone:{fornecedor.telefone}")
    print(f"endereço:{fornecedor.endereco}")
    print("================================")

