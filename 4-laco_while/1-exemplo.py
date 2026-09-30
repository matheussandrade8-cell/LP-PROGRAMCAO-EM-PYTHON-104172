import os
os.system("cls")

while True:
    numero=int(input("digite o numero entre 1 e 10:"))
    if numero < 1 or numero > 10 :
        print("numero inavalido ou tente novamente!")
    else:
        print("o numero esta entre 1 e 10")
        break #serve para laço de repetiçao

print("f")
