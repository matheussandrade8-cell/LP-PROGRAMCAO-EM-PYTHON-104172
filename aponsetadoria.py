import os 
os.system("cls")

codigo=str(input("digite seu codigo de trabalho:"))
idade=int(input("digite sua idade:"))
tempo_de_trabalho=int(input("digite seu tempo de trabalho:"))

if codigo=="123" and idade>=65 and tempo_de_trabalho>=30:
    mostre=("voce pode se aposentar")
else:
    mostre=("voce nao pode se aposentar")
print(mostre)

