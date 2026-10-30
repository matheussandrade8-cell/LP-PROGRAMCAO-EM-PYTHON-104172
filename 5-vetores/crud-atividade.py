import os
#Crud

lista_produto=[]

while True:
    os.system("cls")
    print("""
 == Mercadinho Dendenzeiro ==
1- Cadastrar produto
2- Listar todos os produto
3- Atualizar produto
4- Remover produto
5- Buscar produto
0- Sair
""")

    opcao=int(input("Escolha uma opção:"))
#create(inserir)
    match opcao:
        case 1:
            print(" = Cadastrar Produto = ")
            nome_produto=input("Digite o nome do novo produto:").strip().upper()
            if nome_produto=="":
                print("O nome do produto deve ser inserido")
            elif nome_produto in lista_produto:
                print("Produto ja cadastrado")
            else:
                lista_produto.append(nome_produto)
                print("Produto cadastrado com sucesso!")

#read(ler\busacar dados\consltar)
        case 2:
            print("== Produto no estoque ==")
            for produto in lista_produto:
                print(f"- {produto}")
                print(f"total: {len(lista_produto)}")

#update(atulizar dados)
        case 3:
            print(" == Atualizar produto ==")
            nome=input("Qual produto deseja atualizar:")
            if nome in lista_produto:
                posicao=lista_produto.index(nome)
                novo=input("Novo nomme:")
                lista_produto[posicao]=novo
                print("Produto alterado com sucesso!")
            else:
                print("Produto não encontrado.")

#delete(remover dados)
        case 4:
            print("== Remover o produto ==")
            nome= input("Qual produto voce deseja remover?:")
            if nome in lista_produto:
                lista_produto.remove(nome)
                print("Produto excluido com sucesso")
            else:
                print("Produto não encontrado.")
                
#read(filtrar)
        case 5:
            print("== Encontrar Produto ==")
            nome=input("Qual produto deseja buscar?:")
            if nome in lista_produto:
                print("Produto encontrado!")
            else:
                print("Este produto não esta no estoque.")

        case 0:
            print("saindo do programa.")
            break
        case _:
            print("Opção invalida\n tente novamente.")
    input("Pressione uma tecla para cutinuar.")
    