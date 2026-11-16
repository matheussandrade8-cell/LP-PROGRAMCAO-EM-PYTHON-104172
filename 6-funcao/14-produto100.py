import os
os.system("cls")


def inflacionar_preco(preco_produto):
    if preco_produto<=100:
        resultado=preco_produto *1.10
    else:
        resultado=preco_produto *1.20
        return resultado

print(" = Solicitando = ")
preco_produto=int(input("digite o preço do produto:"))

preco_inflacionado=inflacionar_preco(preco_produto)

print(f"Preço inicial:{preco_produto}")
print(f"Preço inflacionado:{preco_inflacionado}")