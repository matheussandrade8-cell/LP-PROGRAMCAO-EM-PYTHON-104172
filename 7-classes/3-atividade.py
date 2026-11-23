from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class paciente:
    nome:str
    idade:str
    telefoene:str
    endereco:str

    def mostrar_dados(self):
        print(f"nome:{self.nome}")
        print(f"idade:{self.idade}")
        print(f"telefone:{self.telefoene}")
        print(f"endereço:{self.endereco}")
        print("="*25)

    def nome_idade(self):
        print(f"nome:{self.nome}")
        print(f"idade:{self.idade}")
        print("="*25)

    def nome_telefone(self):
        print(f"nome:{self.nome}")
        print(f"telefone:{self.telefoene}")
        print("="*25)

lista_paciente=[]

print(" = Solicitando Dados = ")
for i in range(1):
    dados=paciente(
        nome=input("digite seu nome:"),
        idade=input("digite sua idade:"),
        telefoene=input("digite seu telefone:"),
        endereco=input("digite seu endereço:")
    )

    lista_paciente.append(dados)

    print("Paciente Cadastrado com sucesso")
    input("clique para cutinuar")
    os.system("cls")
os.system("cls")

print("\n = Exebindo status do paciente = ")
for paciente in lista_paciente:
    paciente.mostrar_dados()

print("\n = Exebindo status do nome e idade do paciente = ")
for paciente in lista_paciente:
    paciente.nome_idade()

print("\n = Exebindo status do nome e telefone do paciente = ")
for paciente in lista_paciente:
    paciente.nome_telefone()