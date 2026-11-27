from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    nome:str
    idade:int
    altura:float


lista_cliente=[]


#lendo arquivo
arquivo= "dados_cliente.csv"
with open(arquivo, "r") as arquivo_cliente:
    for linha in arquivo_cliente:
        nome, idade,altura = linha.strip().split(",")
        lista_cliente.append(cliente(
            nome=nome,
            idade=int(idade),
            altura=float(altura)
        ))

print(" = Exebindo Dados = ")
for cliente in lista_cliente:
    print(f"Nome:{cliente.nome}")
    print(f"idade:{cliente.idade}")
    print(f"altura:{cliente.altura}")
    print("==========================")