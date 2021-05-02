# Escreva um programa que leia dois números inteiros e compare-os
# Mostrando na tele uma msg
# O primeiro valor é maior
# O segundo valor é maior
# Os dois são iguais

print('-'*6,'\033[1;31mComparação de dois números\033[m','-'*6)
num1 = (int(input('Digite o primeiro número: ')))
num2 = (int(input('Digite o segundo número: ')))
if num1 > num2:
    print('O primeiro número digitado é maior')
elif num2 > num1:
    print('O segundo número digitado é maior')
else:
    print("Os numeros são iguais")