import os
os.system("cls")

# função com parametro e com retorno, com media e resultado
def calcular_nota(nota1, nota2):
    calculo=(nota1 + nota2)/2
    return calculo

def verificar_resultado(media):
    if media >=7:
        resultado="Aprovado"
    else:
        resultado="Reprovado"
        return resultado

print(" = Solicitando Dados = ")
nota1=float(input("digite a sua primeria nota:"))
nota2=float(input("digite a sua segunda nota:"))

# usando a função com parametro e
# inserindo o retorno na variavel soma
media=calcular_nota(nota1, nota2)/2
situacao=verificar_resultado(media)
print("= Exebindo dados = ")
print(f"Media:{media}")
print(f"Resultado:{situacao}")
