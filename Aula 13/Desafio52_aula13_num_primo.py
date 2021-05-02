# Ler um número inteiro
# Dizer se é ou não um número primo
# Nºprimo  é aquele divisivel apenas por 1 e por ele mesmo

print('\033[1;32m------------  Números Primos  ------------\033[m')

num = int(input('Digite um número para saber se é primo: '))
s = 0
tot = 0 # var criada paras somar qunatas vezes o número foi dividido com resto zero
for c in range(1,num+1,1):
    if num % c == 0:  # Se o resto da divisão for zero ele pintará de amarelo
        print('\033[1;32m',end=' ')  # end = (' ') esse comando é para colocar os resultados em linha sem quebra
        tot = tot + 1  # Se o num for divisivél então a var tot que começa em zero contará mais 1 cada vez que o laço encontrar um divisão resto zero .
                       # Assim se o número passando pelo laço até chegar nele mesmo tiver só duas divisão será primo pois
                       # todo número é dividido duas vezes por ele mesmo e por 1 mas apenas os primos somente são divisiveis por 1 e por ele mesmo.
    else:
        print('\033[1;34m',end=(' ')) # Se não for Zero pintara de azul
    print('{}'.format(c),end=(' '))
print('\n O número {} foi divisível {} vezes.'.format(num,tot))
if tot == 2:
    print(" E por isso ele é PRIMO")
else:
    print(' E por isso ele não é PRIMO')

