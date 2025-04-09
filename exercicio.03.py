ano_nascimento = int (input("Digite o seu ano de nascimento: "))
ano = 2025
idade = ano - ano_nascimento

if idade <= 12:
    print ("Criança")
elif idade >= 12 and idade <= 17: 
    print ("Adolescente")
elif idade >= 18 and idade <= 64:
    print ("Adulto")
else:
    print ("Terceida Idade")


