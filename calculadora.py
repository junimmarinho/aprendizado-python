while True:
    numero1 = input('digite um numero: ')
    numero2 = input('digite outro numero: ')
    operador = input('qual operador? (+-/*):')
    numeros_validos = None
    numero1_float = 0
    numero2_float = 0
    
    operadores_permitidos = '+-/*'
    
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True




    except:
        numeros_validos = None

    if numeros_validos is None:
        print('numeros invalidos')
        continue
    
   
   
    if operador not in operadores_permitidos:
        print('operadores invalidos')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
    
        continue

    
    if operador is '+':
       print (f'{numero1_float} + {numero2_float} =',numero1_float + numero2_float)
    
    if operador is '-':
        print(f'{numero1_float} - {numero2_float} =',numero1_float - numero2_float)
        
    
    if operador is '*':
        print(f'{numero1_float} * {numero2_float} =',numero1_float * numero2_float)
    
    
    if operador is '/':
        print(f'{numero1_float} / {numero2_float} =',numero1_float / numero2_float)
        ...
    


     


    
    
    sair = input('quer sair? s[sim]').lower().startswith('s')
    
    if sair:
        break
    print(sair)

