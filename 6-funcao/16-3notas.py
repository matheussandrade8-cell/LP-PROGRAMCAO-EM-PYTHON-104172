import os
os.system("cls")

def nota_aluno(nota1):
    nota_media= sum(vetor_nota) /3
    return nota_media

def mostra_resultado(lista_notas, media):
    for nota1 in lista_notas:
        print(f"nota:{nota1}")

    print(f"A media do Aluno é {media}")


vetor_nota=[]
for i in range(3):
    nota1=float(input(f"Digite a {i+1}° nota: "))
    vetor_nota.append(nota1)

media = nota_aluno(vetor_nota)
mostra_resultado(vetor_nota, media)