# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
mais_de_mil= 0
cont =0
menor =0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    print('-----------------------------------------------------')
    total = total + preço
    cont = cont + 1
    if preço > 1000:
        mais_de_mil= mais_de_mil +1
    if cont == 1:    # como ja visto em outra aula para fazer o menor de alguns valores . No início criamos um contador que iniciará em 0 e  receberá 1 incdicando que é o primeiro produto a passar se foi o primeiro logo ele é o menor
        menor = preço # então a var menor recebe este preço
        barato = prod
    else:
        preço < menor # depois conforme o laço for rodando se o preço for menor que a var menor

        menor = preço # a var menor ficaram com o preço assim no loop terminará com o menor valor entre os digitados
        barato = prod
    resp = str(input('Quer continuar S ou N')).strip()[0]
    if resp == 'Ss':
        resp = str(input('Quer continuar? S ou N:'))[0]
    elif resp in 'Nn':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Você comprou  {mais_de_mil} itens  que custam mais de R$1000')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')