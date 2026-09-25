import os
os.system("cls")

media=0

for i in range(4):
    nota=float(input(f"digite a {i + 1}º nota:"))
    media= media + nota


print(f"sua media é: {media / 4}")
