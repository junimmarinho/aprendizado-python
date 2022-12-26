numero = input ('digite um numero')
numero2 = input ('digite outro numero')

try:
    int_numero = int(numero)
    int_numero2 = int(numero2)
    int_resultado = int_numero * int_numero2
    print(f'o resultado da sua conta é {int_resultado}')
except:
    print('digite os numeros certos')




