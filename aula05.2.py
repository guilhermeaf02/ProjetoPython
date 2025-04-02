print ("A lampada não funciona")

lampada = input ("A lampada estava plugada? S ou N:  ")

if lampada == "N":
    print ("Plugue a lampada")

else:
    print ("Verificar o bulbo")
    bulbo = input ("O bulbo queimou? S ou N: ")

    if bulbo == "S": 
         print ("Trocar o Buldo")
    else:
         print ("Trocar a lampada")
