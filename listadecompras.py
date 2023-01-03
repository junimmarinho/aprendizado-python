listaCompras = []

while True:
    lista = input('q para listar, e para apagar, i para inserir:')

    if lista in ('qei'):
        
        
        
        
        
        if lista in ('q'):
            if len(listaCompras) == 0:
                print('nada para listar')
            
            
            for corredor in enumerate(listaCompras):
                print(corredor)

            continue


        if lista == ('e'):
            listadelete = input('diga o indice que quer eliminar:')
            
                 
            try:
                listadeleteint = int(listadelete)
                del listaCompras[listadeleteint]

            except ValueError:
                print('este indice é inválido')


        if lista == ('i'):
            insira = input('coloque o que quer')
            listaCompras.append(insira)
            continue
        
    else:
        print('digite um caractere válido')
        continue








