import os
import time
os.system("cls")

print("ㅤㅤㅤㅤㅤMenuㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
print("Selecione uma peça automotiva")
print("1 - Twitter = R$270,00")
print("2 - Cabo 15M = R$150,00")
print("3 - Medio Grave = R$136,00")
print("4 - Mesa = R$85,00")
print("5 - Pen drive = R$50,00")

while True:
    Som=int(input("Selecione a peça automotiva de interesse!:"))
    if Som ==1:
        print("comprar Twitter = R$270,0")
        print(" obrigado pela preferencia!")
        break
    elif Som== 2:
        print("comprar Cabo 15M = R$150,00")
        print(" obrigado pela preferencia!")
        break
    elif Som==3:
        print("comprar Medio Grave = R$136,00")
        print(" obrigado pela preferencia!")
        break
    elif Som==4:
        print("comprar Mesa = R$85,00")
        print(" obrigado pela preferencia!")
        break
    elif Som==5:
        print("comprar Pen drive = R$50,00")
        print(" obrigado pela preferencia!")
        break
    else:
        print("opção invalida")
        time.sleep(1)
        os.system("cls")
