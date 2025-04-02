quantidade_nota = int (input("Digite a quantidade de notas: "))
soma_nota = 0

for i in range (1, quantidade_nota + 1) :
    nota = float (input(f"Digite sua nota: {i} "))
    soma_nota += nota

media = soma_nota / quantidade_nota
print (f"A media das notas é {media:.6f}.")