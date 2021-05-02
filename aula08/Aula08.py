import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

#impotando a bibliotéca math(módulo mmatemática)
#na Var raiz colocamos a função raiz quadrada (sqrt)
#após o math colocar um ponto e selecionar a função
#na hora do  comando format podemos fazer o arredondamento
#math.ceil arrdonda pra mima
#math.floor arredonda para baixo
#print('A raiz de {} é igual a {}'.format(num,math.floor(raiz)))
#print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

