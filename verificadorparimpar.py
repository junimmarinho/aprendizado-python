Numero = input('digite o seu numero')

if Numero.isdigit():
    Numero_int = int(Numero)
    Par_impar = Numero_int %2 == 0
    if Par_impar:
        print('este numero é par')
    else:
        print('este numero é impar')
else:
    print('digite um numero inteiro')



