import os
os.system("cls")

lista_produtos = []
while True:
    #LIMPA O TERMINAL.
    os.system("cls")
    #menu do programa
    print("= Mercadinho Dendenzeiro =")
    print("1- cadastrar o produto")
    print("2- lista de produto")
    print("3- sair")

    opcao=int(input("Escolha uma opção:"))
    match opcao:
        case 1:
            print("=Cadastrar un produto=")
            #strip() retira o espaço vazio no final
            #upper()todas letras maiuscula
            nome=input("Novo produto:").strip().upper()
            if nome == "":
                print("o nome não pode fica vazio.")
            elif nome in lista_produtos:
                print(f"{nome} ja esta cadastrado")
            #append()adiciona o produto na lista.
            else:
                lista_produtos.append(nome)
                print("produto cadastrado com sucesso")
            input("pressione uma tecla para cutinuar")
        case 2:
            print("\n =Lista todos os produto=")
            for i, produto in enumerate(lista_produtos):
                print(f"{i+1}. {produto}")
                #len(lista_produto) mostra a quantidade de produto na lista
                print(f"total de produtos: {len(lista_produtos)}")
                input("pressione uma tecla para cutinuar")
        case 0:
            print("fim do progama")
            input("pressione uma tecla para cutinuar")
            break
        case _:
            print=("opção invalida")
            input("pressione uma tecla para cutinuar")
