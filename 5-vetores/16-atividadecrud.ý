import os 
os.system("cls")

lista_jogador=[]
while True:
    os.system("cls")
    print("""
1- inscrever jogador
2- lista jogador
3- atualizar jogador
4- remover jogador
0- sair""")
    opcao=int(input("escolha uma opção:"))

    match opcao:
        case 1:
            nome_jogador=input("digite o nome do jogador:").strip().upper()
            numero_jogador=int(input("digite o numero do jogador:"))
            posicao_jogador=input("digite a posiçaõ do jogador:").strip().upper()
            if nome_jogador== "" or  numero_jogador== "" or posicao_jogador== "":
                print("o nome do jogador deve ser inserido!")
            else:
                lista_jogador.append(f"{nome_jogador}\n{numero_jogador}\n{posicao_jogador}")
                input("Jogador com nome no BID com sucesso") 
        case 2:
            print("= Lista de jogador =")
            for jogador in lista_jogador:
                    print(f"{jogador}")# Adicionado \n para separar melhor os jogadores
            print(f"total: {len(lista_jogador)}")
        case 3:
            print("= atualizar jogador =")
            if len(lista_jogador)=="":
                print("jogador não atualizado")
            else:
                nome=input("Qual jogador que atualizar?:").strip().upper
                nome_jogador and numero_jogador and posicao_jogador
                posicao = lista_jogador.index(f"{nome_jogador}\n{numero_jogador}\n{posicao_jogador}")
                alterador=input("atualize o nome do jogador:").strip().upper()
                n2=int(input("atualize o numero do jogador:"))
                muda=input("atualize a posição  do jogador:").strip().upper()
                lista_jogador[posicao] = f"{alterador}\n{n2}\n{muda}"
                print("jogador atualizado com sucesso!")

        case 4:
            print("= Remover o jogador =")
            nome=input("remova o jogador:")
            for item in lista_jogador:
                if nome in item :
                 lista_jogador.remove(nome)
                 print(f"total: {len(lista_jogador)}")
            print("jogador removido!")   
        case 0:
            print("saindo do programa.")
            break
        case _:
            print("Opção invalida\n tente novamente.")
    input("Pressione uma tecla para cutinuar.")
