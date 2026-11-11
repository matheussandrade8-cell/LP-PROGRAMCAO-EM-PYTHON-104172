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
while True:
    print("""
= Menu =
1- Cadastrar
2-listar cadastro
3-sair""")

    opcao=int(input("selecione a opção que deseja:"))
    match opcao:
        case 1:
            print(" = solicitando dados =")
            logo_senai()
            nome=input("digite seu nome:")
            telefone=input("digite seu telefone:")
            email=input("digite seu email:")
            print("cadastrado com sucesso")
            print("clique na tecla para voltar ao menu!")
        case 2:
            logo_senai()
            mostrar_dados(nome,telefone, email)
            print("clique na tecla para voltar ao menu")
        case 3:
            print("fim do programa.")
            break
        case _:
            print("opção não encontrado")