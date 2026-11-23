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
        print("="*25)
    #funçao para enviar somente os email.
    def email_marketing(self):
        print(f"nome:{self.nome}")
        print(f"email:{self.email}")
        print("="*25)
    #funçao so para enviar nome e telefone
    def whatsapp_marketing(self):
        print(f"nome:{self.nome}")
        print(f"telefone:{self.telefone}")
        print("="*25)

lista_cliente=[]

print(" = Solicitando Dados = ")
for i in range(1):
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

print(("\n = Exebindo Clientes = "))
for cliente in lista_cliente:
    cliente.mostrar_dados()

print(("\n = Exebindo email marketing = "))
for cliente in lista_cliente:
    cliente.email_marketing()

print(("\n = Exebindo email marketing = "))
for cliente in lista_cliente:
    cliente.whatsapp_marketing()
