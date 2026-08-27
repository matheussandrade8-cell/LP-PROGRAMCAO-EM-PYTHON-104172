import os
os.system("cls")

#Inicio
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

#Process
soma = numero1 + numero2
media = soma / 2
produto = numero1 * numero2

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

#fim
print(f"Soma:, {soma}")
print(f"produto: ,{produto}")
print(f"Média:", {media})
print(f"Maior número:, {maior}")
print(f"Menor número:, {menor}")
