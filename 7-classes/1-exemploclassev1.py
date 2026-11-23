from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class cliente:
    # Nome da variavel e tipo da variavel
    nome:str
    idade:int

# Solicitando dados
cliente1 = cliente("Marta", 30)
# Solicitando dados de outro cliente
cliente2 = cliente("jose", 40)

print(f"Nome:{cliente1.nome }")
print(f"idade:{cliente1.idade}")

print(f"Nome:{cliente2.nome }")
print(f"idade:{cliente2.idade}")