import os
os.system("cls")
lista_produto=[]

def mostrar_dados(lista_produto):
    for i in range(3):
        print(f"{i+1}-{lista_produto[i]} ")
def pedir_dados():
    for i in range(3):
        produto=input("digite o nome do produto:")
        lista_produto.append(produto)

print("= Solicitando dados =")
pedir_dados()

print(" = Exebindo dados = ")
mostrar_dados(lista_produto)