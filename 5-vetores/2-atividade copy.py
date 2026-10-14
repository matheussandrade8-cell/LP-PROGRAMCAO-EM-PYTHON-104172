import os 
os.system("cls")

print("\n Inserir numero de vetor")
vetor_livro= []
for i in range(5):
    livro=input(f"digite {i+1}ª o nome do livro:")
    vetor_livro.append(livro)


print(  "Exebir 5 livros" )
for indice, livro in enumerate(vetor_livro, start=1):
    print(f"{indice}º: {livro}")