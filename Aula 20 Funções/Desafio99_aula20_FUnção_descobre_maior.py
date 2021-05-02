#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maiornum(* n):
    cont =maior = 0
    print('='*60)
    print('Analisando os valores passados...')
    for valor in n:
        print(f'{valor} ',end='',flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram imformados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maiornum(22,9,10,8,6,12)
maiornum(5,6,7,11,8,99)
maiornum(2,1,3,4)
maiornum(1,45,2,26,46,16)
