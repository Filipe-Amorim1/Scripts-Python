#Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
print('\033[1;33m------- CONTAGEM COM FUNÇÂO PYTHON -------')
print()

from time import sleep
def contador(i,f,p):
    for c in range(i,f,p):
        sleep(0.5)
        print(f' {c}',end='')
print('Contagem de 1 até 10 de 1 em 1:')

contador(1,11,1)
print()
print('-='*25)
print('Contagem regressiva de 10 até 0 pulando de 2 em 2:')
contador(10,-2,-2)
print()

print('-='*20)
print('Agora digite sua contagem: ')
i = int(input('Ínicio: '))
f =int(input('final: '))
p =int(input('passo: '))

contador(i,f,p)
print()
print('FIM!!')




