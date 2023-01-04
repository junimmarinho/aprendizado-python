import re
import random

for generator in range(100):
    

    noveDigitos = ''

    for name in range(9):
        noveDigitos += str (random.randint(0,9))
        if len(noveDigitos) == 9:
        
            print(noveDigitos)
    



