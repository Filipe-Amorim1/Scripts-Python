# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
valor = 0

for c in range(0, 6):
    valor=int(input('Digite um número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram{lista[1]}')



'''lista = []
par = []
ímpar = []
listafinal = []

for c in range (0,6):
    lista.append(int(input('Digite um número: ')))
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        ímpar.append(lista[c])
        
par.sort()
ímpar.sort()
listafinal.append(par[:])
listafinal.append(ímpar[:])
print(listafinal)  '''

