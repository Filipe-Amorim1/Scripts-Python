# Tupla é entre parenteses ()
# Lista é entre [] colchetes
# Dicionário é entre {} chaves

###########    TUPLAS  ##########
# tuplas são imutavéis

lanche = ('hamburguer','suco','pizza','pudim','alface')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3]) # nesse caso como vimos , ele vai do 1 até o 2 desconsiderando o final
print(lanche[0:4])# printar elementos 0,1,2,3
print(lanche[:2]) # mostrar do ínicio até o elemento 2
print(lanche[-2:])

for c in lanche:  # Aqui o laço vai passar uma a uma das palavrar na tuple
    print(f'Estou com fome eu vou comer {c}') # e colocar no lugar do c aqui printando cada vez que passar ( print dentro da indentação

for cont in range (0, len(lanche)):
    print(f'Estou com fome eu vou comer {cont}')

for c in enumerate (lanche):
    print(f'Estou com fome eu vou comer {c}')
print('Comi muito to cheio!!')  # este printa só depois que sair do laço devido a indentação

print( sorted(lanche))  # sorted coloca em ordem A-Z

#Juntando Tuplas
a = (1,2,3,4,5)
b = (5,6,6,7,8)
c = a+b

print(a)
print(b)
print(c)
print(b+a)
print(c.count(5)) # var.count   aqui mostra qunatas vezes temos o número 5 na var c ( quie é a junção das var a e b)
print(c.index(4)) # var.index mostra a primeira ocorrência do número na tupla
print(c.index(5,))
