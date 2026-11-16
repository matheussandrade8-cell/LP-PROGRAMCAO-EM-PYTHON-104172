import os
from datetime import date
os.system("cls")

def idade_atual(ano_nascimento):
    ano_atual= date.today()
    idade= ano_atual  - ano_nascimento
    return idade

ano_nascimento=int(input("digite seu ano de nascimento:"))
idade=idade_atual(ano_nascimento)

print(f"seu ano de nascimento é {ano_nascimento}")
print(f"sua idade é {idade} anos")