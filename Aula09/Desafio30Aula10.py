#Criar um problema para ver se é par ou ímpar
num = int(input('Digite um número para saber se é par ou ímpar:').strip())
if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))