import os 
os.system("cls")

#inicio>

numero1 = int(input("digite o numero1:"))
numero2 = int(input("digite o numero2:"))

#process.

media = (numero1 + numero2)/2
soma = numero1 + numero2
multiplicacao = numero1 * numero2

if numero1 > numero2:
    print("o maior valor é {} e o menor valor é {}".format(numero1 , numero2))
elif numero1 == numero2:
    print("o numero1 {} é igual ao numero2: {}".format(numero1, numero2))
else:
    print("o numero é {} é menor que o numero {}".format(numero1,numero2))

#fim
print("\n= Exbindo dados")
print(" A media entre {} e {} da {}".format(numero1, numero2,media))
print("A soma entre {} e {} o resultado é {}".format(numero1, numero2, soma))
print(" A multiplicacao entre {} e {} o resultado é {}".format(numero1, numero2, multiplicacao ))

