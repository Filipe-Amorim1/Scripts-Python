# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
digite = (int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')))
print(digite)
print(f'O número 9 apareceu {digite.count(9)} vezes')
if 3 in digite:
    print(f'O número 3 está na posição:{(digite.index(3)+1)}')
else:
    print('Não tem número 3')
print('Os valores pares digitados foram:')
for c in digite:
    if c%2==0:
        print(c,' ',end='')





