conversor_minutos = int (input ("Digite os minutos: "))

hora = conversor_minutos // 60
minutos = conversor_minutos % 60

if conversor_minutos < 60 :  
    print ("É menos de uma hora")
else:
    print (f" horario {hora}h:{minutos}")



