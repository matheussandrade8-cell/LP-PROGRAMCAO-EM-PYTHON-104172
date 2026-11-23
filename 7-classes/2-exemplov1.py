from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome:str
    telefone:str
    email:str

lista_cliente=[]

for i in range(2):
    dados = cliente(
        nome=input("\nDigite seu nome:"),
        telefone=input("Digite seu numero:"),
        email=input("Digite seu email:")
    )
    lista_cliente.append(dados)

    print("cliente cadastrado com sucesso")
    input("clique para cutinuar")
    os.system("cls")
os.system("cls")
print(("\nExebindo Clientes"))
for cliente in lista_cliente:
    print(f"nome:{cliente.nome}")
    print(f"telefone:{cliente.telefone}")
    print(f"email:{cliente.email}")