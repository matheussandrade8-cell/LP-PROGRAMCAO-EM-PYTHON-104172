from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome:str
    telefone:str
    email:str
    # Função dentro da classe
    def mostrar_dados(self):
        print(f"nome:{self.nome}")
        print(f"telefone:{self.telefone}")
        print(f"email:{self.email}")

lista_cliente=[]

print("Solicitando Dados")
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
    cliente.mostrar_dados()
