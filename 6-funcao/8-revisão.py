import os
os.system("cls")

#função sem retorno com parametro
def logo_senai():
    print("="*20)
    print("     Senai")
    print("="*20)


#função sem retorno com parametro
def mostar_dados(nome, idade):
    print(f"{nome} tem {idade} anos.")
#função sem retorno com parametro
logo_senai()
print(" = Solicitando Dados = ")
nome=input("digite o seu nome:")
idade=input("digite sua idade:")

logo_senai()
print(" = Exebindo dados = ")
#função sem retorno com parametro
mostar_dados(nome ,idade)