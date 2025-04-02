ano_nascimento = int (input("Digite o ano que nasceu: "))
ano_atual = 2025

idade = ano_atual - ano_nascimento  
if idade >= 16:
    print ("Pode votar")
else:
    print ("Não pode votar")