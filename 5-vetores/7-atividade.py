import os
os.system("cls")
print("Exebeindo notas")
vetor_numero=[]
total=0

# o Q é de quantidade
for i in range(5):
    numero=int(input(f"digite {i+1}º seu numero:"))
    vetor_numero.append(numero)

#media=sum(vetor_numero) / q #SOMA TUDO QUE ESTA NO VETOR
menor_numero=min(vetor_numero)
maior_numero=max(vetor_numero)

    #media= sum(vetor_notas) / q


print("\n=Exebindo numero")
for posicao, numero in enumerate(vetor_numero, start=1):
    print(f"{posicao}º: {numero}")

print(f"menor numero: {menor_numero}")
print(f"maior numero: {maior_numero}")