import os
os.system("cls")

media=0
t=0
for i in range(3):
    nota=float(input(f"digite a {i + 1}º nota:"))
    media= media + nota
    t=media /3

    if  t>= 7:
        resultado="aprovado"
    elif t>=4:
        resultado="recuperação"
    else:
        resultado="reprovado"

print(f"sua media é: {t}")
print(f"{resultado}")
