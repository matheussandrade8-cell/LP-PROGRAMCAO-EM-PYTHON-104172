import os
os.system ("cls")
#Inicio
maças = int(input("quantas maças voce quer:"))

#Processo
if maças <12:
    custo=maças*1.30
else:
    custo=maças*1
#fim
print(f"valor total {custo} reias")
