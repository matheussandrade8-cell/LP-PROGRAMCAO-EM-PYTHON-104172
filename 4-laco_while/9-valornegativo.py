import os
os.system("cls")

soma=0
contador=0

while True:
    numero=int(input("digite um numero:"))
#so vai parar o laço quando for numero negativo
    if numero< 0:
        break
    soma+=numero
    contador+=1

media=soma/contador
print(f"media: {media}")

