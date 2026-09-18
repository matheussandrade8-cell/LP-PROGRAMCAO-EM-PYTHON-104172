import os
os.system("cls")

nome=input("Digite o nome do produto:")
quantidade=int(input("digite a quantidade adquirida:"))
preco=float(input("digite o preço unitariio:"))

total= quantidade * preco

if quantidade <=5:
    desconto=total *0.02
elif quantidade <=10:
    desconto=total *0.03
else:
    desconto=total *0.05

total_pagar= total - desconto

print(f"produto {produto}")
print(f"total da compra {total}")
print(f"Desconto R$ {desconto}")
print(f"total a pagar: R$ {total_pagar}")

