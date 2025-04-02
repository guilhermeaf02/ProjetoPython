print("A lâmpada não funciona")

lampada = input("A lâmpada estava plugada? S ou N:  ")

if lampada == "N":
    print("Plugue a lâmpada")
else:
    print("Verificar o bulbo")
    bulbo = input("O bulbo queimou? S ou N: ")

    if bulbo == "S":  # Alterei para "S" porque no input foi perguntado "S ou N"
        print("Trocar o Bulbo")
    else:
        print("Trocar a lâmpada")
