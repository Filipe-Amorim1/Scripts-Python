#  Crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999,
#  que é a condição de parada. No final,
#  mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
import math
fim = 0
cont =0
num = 0
while num != 999:
    num =int(input('Digite um número: '))
    cont = cont + num
    if num == 999:
        print('FIM')
print(cont-999)