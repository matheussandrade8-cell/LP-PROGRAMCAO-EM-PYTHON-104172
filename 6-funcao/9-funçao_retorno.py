import os
os.system("cls")

# função com parametro e com retorno com soma 
def calcular_nota(nota1, nota2):
    calculo=nota1 + nota2
    return calculo

print(" = Solicitando Dados = ")
nota1=float(input("digite a sua primeria nota:"))
nota2=float(input("digite a sua segunda nota:"))

# usando a função com parametro e
# inserindo o retorno na variavel soma
soma=calcular_nota(nota1, nota2)

print("= Exebindo dados = ")
print(f"soma: {soma}")