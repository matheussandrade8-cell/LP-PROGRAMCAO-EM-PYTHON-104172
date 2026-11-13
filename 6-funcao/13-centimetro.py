import os
os.system("cls")

def metros_cm():
    resultado= metros*100
    return resultado
metros=float(input("Digite o quantos metros pra converter:"))

centimetros=metros_cm()
print(" = Exebindo Resultado = ")
print(f"O metro {metros} convertido para centimetro é {centimetros} ")