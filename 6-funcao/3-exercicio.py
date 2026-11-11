import os
os.system("cls")

def logo_senai():
    
    print("="*20)
    print("     Senai Bahia")
    print("="*20)
def mostrar_dados(nome,telefone, email):
    print(f"Nome:{nome}")
    print(f"Telefone:{telefone}")
    print(f"E-mail:{email}")

print(" = solicitando dados =")
logo_senai()
nome=input("digite seu nome:")
telefone=input("digite seu telefone:")
email=input("digite seu email:")
os.system("cls")
logo_senai()
print(" = exebindo dados = ")
mostrar_dados(nome,telefone, email)
