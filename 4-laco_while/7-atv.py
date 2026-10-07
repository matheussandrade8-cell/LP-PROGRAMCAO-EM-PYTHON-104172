import os
os.system("cls")

soma=0
for i in range(3):
        nota=float(input(f"digite a {i+1} nota:"))
        media=(soma+nota)
        total=nota /3
while True:
        if nota< 7 or nota> 10:
                print("aprovado")
        elif nota< 5 or nota> 6.9:
                print("recuperação")
        elif nota< 0 or nota> 4.9:
                print("reprovado")
        else:
                print("")
        break