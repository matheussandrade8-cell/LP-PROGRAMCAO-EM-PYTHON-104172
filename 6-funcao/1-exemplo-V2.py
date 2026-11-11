import os
os.system("cls")

#criando uma função
def cabecalho():#parametro
    print("="*15)
    print("     Senai Bahia")
    print("="*15)

cabecalho()#usando função
nome=input("Digite seu nome:")

cabecalho()#usando função
idade=input("digite sua idade:")

cabecalho()#usando função
print(f"nome:{nome}")
print(f"idade:{idade}")