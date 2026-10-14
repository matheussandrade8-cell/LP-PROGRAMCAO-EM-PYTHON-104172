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

    #media= sum(vetor_notas) / q
if nota >=7:
    print("aluno aprovado")
elif nota>=5 or nota<=6.9:
    print("aluno em recuperação")
else:
    print("alunor reprovado")


print("Exebindo nota")
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f"{posicao}º: {nota}")

    print(f"media: {media}")