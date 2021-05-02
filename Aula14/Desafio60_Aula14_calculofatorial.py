#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex fatorial de 10 =  10*9*8*7*6*5*4*2*1 = 3628800

# MÉTODO SE FUNÇÃO FACTORIAL
print('-='*10,'Calculo de Fatorial ','=-'*10)

n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    f = f*c
    c=c-1
print(f)

# MÉTODO COM A FUNÇÃO
print('-='*10,'Calculo de Fatorial com função ','=-'*10)
from math import factorial
n =int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é igual a: {}'.format(n,f))


