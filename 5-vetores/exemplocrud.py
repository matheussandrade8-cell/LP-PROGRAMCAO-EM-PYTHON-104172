import os
os.system("cls")

lista_contrato=[]
while True:
    os.system("cls")
    print("""
    = Al-Hilal SFC =
    1- contratar jogador
    2- listar contrato
    3- atualizar contrato
    4- vender jogador""")
    opcao=int("escolha uma opção:")

    match opcao:
        case 1:
            print("buscar jogador")
            buscar=input("Pesquise o nome do jogador:")
            
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
