#Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
# É uma sucessão de números que, misteriosamente, aparece em muitos fenômenos da natureza.
# Descrita no final do século 12 pelo italiano Leonardo Fibonacci, ela é infinita e começa com 0 e 1.
# Os números seguintes são sempre a soma dos dois números anteriores.
# Portanto, depois de 0 e 1, vêm 1, 2, 3, 5, 8, 13, 21, 34…

print('\033[1;33m ------- Sequência de Fibonacci 1.0 -------')
n = int(input('Digite um número: '))
inicial1 = 0
inicial2 = 1
fibo = 0
num =0
cont = 0
print(inicial1,'->',inicial2,end='')

while cont <= n:
    fibo = inicial1 + inicial2
    inicial1 = inicial2
    inicial2 = fibo
    cont = cont + 1
    print('->',fibo,end='')