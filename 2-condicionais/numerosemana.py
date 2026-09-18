import os
os.system("cls")

dia =int(input("digite o numero do dia:"))

match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda-feira dia util")
    case 3:
        print("terça-feira dia util")
    case 4:
        print("quarta-feira dia util")
    case 5:
        print("quinta-feira dia util")
    case 6:
        print("sexta-feira dia util")
    case 7:
        print("sábado")
    case _:
        print("dia invalido")
print(dia)
