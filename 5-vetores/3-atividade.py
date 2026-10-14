import os
os.system("cls")
print("Exebeindo notas")
vetor_notas=[]

for i in range(3):
    nota=float(input(f"digite {i+1}º sua nota:"))
    vetor_notas.append(nota)

print("Exebindo nota")
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f"{posicao}º: {nota}")