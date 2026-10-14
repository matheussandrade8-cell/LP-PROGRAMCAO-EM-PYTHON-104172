import os 
os.system("cls")

print("Inserir numero de vetor")
vetor_numero= []
for i in range(3):
    numero=int(input("digite um numero:"))
    vetor_numero.append(numero)


print("exebir numero de vetor")
for i in range(3):
    print(f"posição de vetor: {vetor_numero[i]}")
#sua vez, mostre a ultima posição do vetor.