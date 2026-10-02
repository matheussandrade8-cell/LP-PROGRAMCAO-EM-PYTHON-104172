import os
os.system("cls")


soma=0

for i in range(2):
    while True:
        nota=float(input(f"digite a {i+1} sua nota:"))
        if nota < 0 or nota > 10:
            print("nota invalida")
            print("tente novamente! \n")
        else:
            soma += nota
            break

media=soma /2

print(f"media: {media}")