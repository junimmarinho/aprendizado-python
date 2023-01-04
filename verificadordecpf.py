import re
import random

noveDigitos = ''

for name in range(9):
    noveDigitos += str (random.randint(0,9))


cpf = re.sub(
    r'[^0-9]','',
    '746.824.890-70')
nomeDigitos = cpf[:9]
contadorRegressivo = 10
resultado = 0

primeirosequencia = cpf == cpf[0] * len(cpf)

for numero in nomeDigitos:
    resultado += int(numero) * contadorRegressivo
    contadorRegressivo -= 1

digito = ((resultado * 10)%11)
digito = digito if digito <= 9 else 0

cpf2 = '746824890707'
nomeDigitos2 = cpf2[:10]
contadorRegressivo2 = 11
resultado2 = 0

for numero2 in nomeDigitos2:
    resultado2 += int(numero2) * contadorRegressivo2
    contadorRegressivo2 -= 1

digito2 = ((resultado2 * 10)%11)
digito2 = digito2 if digito2 <= 9 else 0
novoCPF = f'{nomeDigitos}{digito}{digito2}'

if novoCPF == cpf:
    print(f'o {cpf} é válido')