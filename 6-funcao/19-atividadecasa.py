import os
os.system("cls")

def verificar_peso(peso, altura):
    imc= peso/ (altura*altura)
    return imc

def verificar_indice(indice):
    indice= indice
    return indice

def verificar_recomendacao(recomendacao):
    recomendacao= recomendacao
    return recomendacao

#inicio
peso= float(input("digite seu peso: "))
altura= float(input("digite sua altura: "))

#Processo.
imc = verificar_peso(peso, altura)

if imc < 18.5:
    indice=("abaixo do peso")
    recomendacao="consulte um nutricionista para orientação"
elif imc < 75.9:
    indice=("peso ideal parabens")
    recomendacao="mantenha habitos saudaveis"
elif imc < 90.9:
    indice=("levemente acima do peso")
    recomendacao="considere uma dieta balanceada e atividade fisica"
elif imc < 120.9:
    indice=("obesidade grau 1")
    recomendacao="procure orientação de um profissional de saude"
elif imc < 150.0:
    indice=("obesidade grau 2 ")
    recomendacao="consulte um medico para orientação e avaliação"
else:
    indice=("obesidade morbida")
    recomendacao="busque assistencia medica imediatamente"

situacao=verificar_peso(peso, altura)
verificacao=verificar_indice(indice)
comentario=verificar_recomendacao(recomendacao)

print(f"sua altura é {situacao:.2f} e o seu indice é de {verificacao} proponho essa recomendação {comentario}")