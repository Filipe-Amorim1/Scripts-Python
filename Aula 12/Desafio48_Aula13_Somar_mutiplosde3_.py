#Somar os multiplos de 3 entre 1 e 500 somente os números ímpares
import math
s = 0
for c in range(1,501,2): # colocar para pular de 2 em 2  apartir do 1 , assi só pega os números impares
    print(c)
    if c% 3 == 0:
        s=s+c
print('A soma dos multiplos de 3 é:',s)