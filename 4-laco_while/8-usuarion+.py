import os
os.system("cls")
soma=0
contador=0
continue_com_a_nota="s"

#laço repetição
while continue_com_a_nota =="s":
    nota=float(input(f"digie a {contador+1}ª sua nota: "))
    soma+=nota
    contador+=1

    continue_com_a_nota=input("deseja insirir mas uma nota s ou n?")
#verificaçao das notas e somas
    if contador >0:
        media=nota/contador
        print(f"total de notas inseridas: {contador}")
        print(f" A media das notas é: {media}")
    else:
        print("nenhuma nota informada")