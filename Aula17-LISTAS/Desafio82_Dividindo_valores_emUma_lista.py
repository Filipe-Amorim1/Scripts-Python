#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

print('\033[1;32m===== Lista com pares e ímpares ===== \033[m')

lista = []
lista_pares = []
lista_ímpares =[]
while True:
    try:
        lista.append(int(input('Digite os valores para a lista: ')))
    except:
        print('Valor inválido')
    try:
        resp = str(input('Quer continuar digitando?'))
        if resp in 'Nn':
            break
    except:
        print('Valor Inválido')
for c,v in enumerate(lista):
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_ímpares.append(v)
print(f'A lista completa é {lista}')
print(f' Os números pares da lista são {lista_ímpares}')
print(f'Os números ímpares da lista são {lista_pares}')

