import os
os.system("cls")
print("Exebeindo notas")
vetor_notas=[]
total=0
q=3
# o Q é de quantidade
for i in range(q):
    nota=float(input(f"digite {i+1}º sua nota:"))
    vetor_notas.append(nota)

    soma=sum(vetor_notas) #SOMA TUDO QUE ESTA NO VETOR
    media= total/q
    #media= sum(vetor_notas) / q
print("Exebindo nota")
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f"{posicao}º: {nota}")
    print(f"soma: {soma}")
    print(f"media: {media}")