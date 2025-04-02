print ("Meu Sitema")
print ("1 - Cliente")
print ("2 - Vendas")
print ("3 - Produtos")
print ("4 - Sair")

while True:
    opcao = input ("Digite a opção desejada: ")

    if opcao == "1":
        print ("Cliente")
        continue
   
    elif opcao == "2":
        print ("Vendas")
        continue

    elif opcao == "3":
        print ("Produtos")
        continue
    
    elif opcao == "4":
        print ("Sair")
        break
    else:
        print ("Opção Invalida")
        break

