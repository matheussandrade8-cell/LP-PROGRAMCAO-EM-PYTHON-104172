from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    # Nome da variavel e tipo da variavel
    nome:str
    idade:int
    altura:float
    peso:float
lista_cliente= []

print("Solicitando dados")
for i in range(2):
    dados_do_cliente=cliente(
        nome=input("\ndigite seu nome:"),
        idade=int(input("digite sua idade:")),
        altura=float(input("Digite sua altura")),
        peso=float(input("Digite seu peso:"))
    )
    input("toque para cutinuar")
    lista_cliente.append(dados_do_cliente)
    os.system("cls")
print("Exebindo dados")
for cliente in lista_cliente:
    print("="*10)
    print(f"Nome:{cliente.nome}")
    print(f"idade:{cliente.idade}")
    print(f"altura:{cliente.altura}")
    print(f"peso:{cliente.peso:.2f}")
    print("="*10)