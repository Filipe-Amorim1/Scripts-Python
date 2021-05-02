#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
c = 0
while True:
    lista.append(int(input('Digite os valores:')))
    c +=  1
    if  -1 in lista :
        break

print(f'Foram digitados {c-1} números na lista ')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente são {lista}')
if 5 in lista[:]:
    print('O número 5 esta na lista')
else:
    (f'O número 5 não esta na lista')


