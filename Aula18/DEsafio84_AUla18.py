# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dados =[]
pessoas = []
totalpessoas = 0
maior = 0
menor =0
while True:
    dados.append(str(input('NOme:')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    totalpessoas += 1
    resp =''
    resp = str(input(' Quer continuar [S/N] ? '))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {totalpessoas} pessoas. ')
for p in pessoas:
    if p[1] == maior:
        print(f'A pessoa mais pesada é  {p[0]} com {p[1]}Kg ')
    elif p[1] == menor:
        print(f'A pessoa mais leve é  {p[0]} com {p[1]}Kg ')


