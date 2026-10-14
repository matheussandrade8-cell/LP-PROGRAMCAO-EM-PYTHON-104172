import os
os.system("cls")
print("Exebeindo notas")
vetor_notas=[]
total=0
q=4
# o Q é de quantidade
for i in range(q):
    nota=float(input(f"digite {i+1}º sua nota:"))
    vetor_notas.append(nota)

media=sum(vetor_notas) / q #SOMA TUDO QUE ESTA NO VETOR
menor_nota=min(vetor_notas)
maior_nota=max(vetor_notas)

    #media= sum(vetor_notas) / q
if nota >=7:
    resultado=("aluno aprovado")
elif nota==5:
    resultado=("aluno em recuperação")
else:
    resultado=("alunor reprovado")


print("Exebindo nota")
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f"{posicao}º: {nota}")
    print(f"media: {media}")
    print(f"resultado: {resultado}")

    print(f"menor nota: {menor_nota}")
    print(f"maior nota: {maior_nota}")