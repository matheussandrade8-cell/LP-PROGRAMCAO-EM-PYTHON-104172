import os
os.system("cls")


def verificar_par_impar():
    if  numero % 2==1:
        resultado="impar"
    else:
        resultado="par"
    return resultado

numero=int(input("Digite o numero para saber se é impar ou par:"))

impar_par=verificar_par_impar()
print(f" O numero:{numero} é {impar_par}")