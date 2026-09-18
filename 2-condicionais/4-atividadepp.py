import os
os.system("cls")

morango=float(input("digtite a quantidade de morango (kg):"))
maca=float(input("digite a quantidade de maça (kg):"))

if morango <=5:
    preco_morango= morango *2.50
else:
    preco_morango= morango *2.20
if maca <=5:
    preco_maca=maca *1.80
else:
    preco_maca=maca *1.50

valor_total = preco_morango + preco_maca

quantidade_total = morango + maca

if quantidade_total >= 10:
    desconto = valor_total * 0.10
    valor_total = valor_total - desconto
else:
    if valor_total > 15:
        desconto = valor_total * 0.10
        valor_total = valor_total - desconto
    else:
        desconto = 0

print("Quantidade de morangos:", morango, "Kg")
print("Quantidade de maçãs:", maca, "Kg")
print("preço dos morangos: R$", preco_morango)
print("preços das maçãs: R$", preco_maca)
print("Desconto: R$", desconto)
print("Valor total a pagar: R$", valor_total)
