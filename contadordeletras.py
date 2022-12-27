nome = input(' digite seu primeiro nome')
cont_nome = len(nome)

if cont_nome <= 4:
    print('seu nome é curto')
if cont_nome >= 5 and cont_nome <= 6:
    print(' seu nome é médio')
if cont_nome > 6:
    print('seu nome é longo')