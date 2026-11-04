import os
os.system("cls")

lista_paciente=[]
while True:
    os.system("cls")
    print("""
 == Cadastrar paciente ==
1-Cadastrar paciente
2-Listar pacinte
3-Atualizar paciente
4-Buscar paciente
5-remover paciente
0-sair""")

    opcao=int(input("Escolha uma oção!:"))
#create(inserir)!!!!!!!!!!!!!!!!
    match opcao:
        case 1:
            nome_paciente=input("digite o nome do paciente:").strip().upper()
            sobrenome_paciente=input("digite o sobrenome do paciente:").strip().upper()
            if  nome_paciente== "" or  sobrenome_paciente== "":
                print("o nome ou sobrenome deve ser inseriodo!")
            elif nome_paciente and sobrenome_paciente in lista_paciente:
                print("nome e sobrenome cadastrado")
            else:
                lista_paciente.append(nome_paciente + " " + sobrenome_paciente)
                print("paciente cadastrado com sucesso")
#read(ler\busacar dados\consltar)
        case 2:
            print("== Lista do paciente ==")
            for produto in lista_paciente:
                print(f"- {produto}")
            print(f"total: {len(lista_paciente)}")
            #update(atulizar dados)
        case 3:
            print(" == Atualizar paciente ==")
            nome=input("Qual paciente deseja atualizar:").strip().upper()
            if nome in lista_paciente:
                posicao=lista_paciente.index(nome)
                novo=input("Novo nome:").strip().upper()
                lista_paciente[posicao]=novo
                print("Paciente alterado com sucesso!")
            else:
                print("Paciente não encontrado.")
                #delete(remover dados)
        case 4:
            print("= Remover paciente =")
            nome=input("qual paciente deseja remover?:").strip().upper()
            if nome in lista_paciente:
                lista_paciente.remove(nome)
                print("paciente removido!")
            else:
                print("paciente não encontrado")
                #buscar
        case 5:
            print("= Buscar Paciente =")
            nome=input("qual paciente deseja encontrar?:").strip().upper()
            if nome in lista_paciente:
                print("paciente encontrado!")
            else:
                print("paciente não encontrado")
        case 0:
            print("saindo do programa")
            break
        case _:
            print("opção invalida\n tente novamente")
    input("clique em cutinuar para voltar ao inicio!")


