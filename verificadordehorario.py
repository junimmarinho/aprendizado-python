horario = input('digite o seu horario')
horario_int = int(horario)
if horario.isdigit():

    
    if 0 <= horario_int < 12:
        print('bom dia')
    if 12<= horario_int < 18:
        print('boa tarde')
    if 18 <= horario_int < 25:
        print('boa noite')
    if horario_int >= 25 or horario_int < 0:
        print (' horario invalido')
else:
    print('digite um horario valido')

    
