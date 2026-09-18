import os

#Limpa o terminal.
os.system("cls")

print("= SOLICITANDO DADOS =")
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
primera_nota = float(input("digite a primera_nota: "))
segunda_nota = float(input("digite a segunda_nota: "))

media = (primera_nota + segunda_nota) /2

print("\n= EXEBINDO DADOS =")
print("nome: ", nome)
print("idade: ", idade)
print("primera_nota: ", primera_nota)
print("segunda_nota: ", segunda_nota)
print("media: ", media)