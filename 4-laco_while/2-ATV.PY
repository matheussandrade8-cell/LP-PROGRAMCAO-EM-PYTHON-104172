import os
os.system("cls")
media=0
for i in range(2):
        notas=float(input(f"digite{i+1} sua nota:"))
        media=(media+notas)
        total= media /2
while True:
    if notas <0 or notas >10:
        print("notas invalida")
    else:
        print(f"sua media é {total}")
        break
