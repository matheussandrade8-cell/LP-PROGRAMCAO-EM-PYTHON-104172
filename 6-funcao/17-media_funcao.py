import os
os.system("cls")

def nota_aluno(nota1):
    nota_media= sum(vetor_nota) /2
    return nota_media

def mostra_resultado(lista_notas):
    for nota in lista_notas:
        print(f"nota:{nota}")

def status_aluno(media):
    if media >=7:
        resultado="aprovado"
    else:
        resultado="reprovado"
    return resultado

vetor_nota=[]
for i in range(2):
    while True:
        nota=float(input(f"Digite a {i+1}° nota: "))
        if nota >= 0 and nota <=10:
            vetor_nota.append(nota)
            break
        else:
            print("Nota invalida")

media = nota_aluno(vetor_nota)
status_aluno=status_aluno(media)

print("Exebindo Resultado")
print(f"Media:{media}")
print(f"Situação do aluno:{status_aluno}")
