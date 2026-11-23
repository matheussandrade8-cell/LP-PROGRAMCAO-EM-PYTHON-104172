from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    # Nome da variavel e tipo da variavel
    nome:str
    idade:int
    altura:float
lista_cliente= []

# Solicitando dados

lista_cliente.append(cliente(nome="Marta", idade=30 , altura=1.55))
lista_cliente.append(cliente("jose", 40, altura=1.78))

# Solicitando dados de outro cliente
for cliente in lista_cliente:
    print("="*10)
    print(f"Nome:{cliente.nome}")
    print(f"idade:{cliente.idade}")
    print(f"altura:{cliente.altura}")
    print("="*10)