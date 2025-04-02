print ("A lampada não acende")

while True:
    lampada = input ("A lampada estava plugada? S | N:")

    if lampada == "N":
        print ("Plgue a lampada")
    
    else:
        print ("Verificar o Bulbo")
    
    bulbo = input ("O bulbo está queimando?")
    
    if bulbo == "S":
        print ("Trocar o bulbo")
    else:
        print ("Trocar a lampada")
        break
