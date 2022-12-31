while True:
    senha = int(123456)
    senha_digitada = input('digite sua senha')    
    senha_digitada_int = int(senha_digitada)


    if senha == senha_digitada_int:
        while True:
            numero1 = input('digite um numero:')
            numero2 = input('digite outro numero:')
            operador = input('digite um operador:')
            operafloat = None
            

            try:
                numero1_float = float(numero1)
                numero2_float = float(numero2)
                operafloat = True
            except:
                operafloat = None
            
            if operafloat == None:
                print('digite um numero válido')
                continue

            if operador in ('+-/*'):
                if operador is ('+'):
                    print(f'o resultado é:{numero1_float + numero2_float}')
                
                if operador is ('-'):
                    print(f'o resultado é:{numero1_float - numero2_float}')
                
                if operador is ('*'):
                    print(f'o resultado é:{numero1_float * numero2_float}')
                
                if operador is ('/'):
                    print(f'o resultado é:{numero1_float / numero2_float}')
                
                saida = input(' você deseja sair? sim ou não?')
                saidas = saida.lower
                
                if saidas is ('sim'):
                    break

                if saidas is ('não'):
                    continue


    
    if senha != senha_digitada_int:
        print('senha incorreta')
        continue
    

                       

    

    