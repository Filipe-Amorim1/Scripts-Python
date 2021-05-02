# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
print('\033[1;34m='*10,'Maior e Menor valor em umqa Tupla','='*10,'\033[m')

from random import randint
tupla = ()
cont = (randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000))

for c in range (1,6,1):
    tupla = cont
print(tupla)
print(f'O maios valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
