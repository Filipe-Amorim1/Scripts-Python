# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)
valor = int(input('Qual o valor do saque: '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced: # enquanto o saque for maior ou igual a 50
        total = total -ced  # vai diminuindo 50 do total  até ele ser menor que 50
        totalced = totalced +1  # a var total de ced vai contando quantas vezes diminui que é o número de cédulas
    else:
        if totalced > 0:  # esse if é para não printar as células que não foram usadas (não vai aparecer 0 cédulas )
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50: 
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('Volte Sempre!!!')
