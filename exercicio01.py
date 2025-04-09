valor = float (input ("Digite o valor do valor do produto: "))
desconto = float (input ("Digite o valor do desconto %: "))

preco_final = valor - (valor * desconto / 100)

if valor >= 100 :
    print ("Desconto aplicado, o preço final foi R$:", preco_final)
else:
    print ("Não foi possivel obter o desconto")
    

