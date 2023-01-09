import re
import random

for p in range(200):
    
    senhas = ''

    for y in range(10):
        senhas += str(random.randint(0,9))
        if len(senhas) == 10:
            print(senhas)
