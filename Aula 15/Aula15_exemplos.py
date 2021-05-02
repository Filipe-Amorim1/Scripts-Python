'''n=0
soma = 0
while n != 999:
    n=int(input('Digite um número:'))
    soma = soma +n
print('Fim',soma-999)  '''

n = 0
soma = 0
while True:  # loop infinito do laço que só vai para no break
    n = int(input('Digite um número: '))
    if n == 999:  # aqui o laço para quando digitar 999 e esse valor não será somado
        break
    soma = soma + n
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma} ')  # nova forma alternativa ao .format
                               # colocar o f mínúsculo e a var dentro das chaves