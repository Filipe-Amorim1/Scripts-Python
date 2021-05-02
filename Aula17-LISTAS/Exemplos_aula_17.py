# As listas ficam entre [] e são mutavéis diferente das tuplas entre() que são imutaveis
num =[2,5,9,1]
print(num)
num[2] = 3   # aqui o item 2 no caso o 9 mudaria para 3
print(num)
# para adicionar um valor não podemos botar num[4] = 7 , daria erro pois não tem essa posição na lista
# tem que . append() no caso de add mais um item a partir do final da lista
num.append(7)
print(num)
# colocar a lista em ordem A à Z
num.sort()
print(num)
#Ordem Z à A
num.sort(reverse=True)
# SAber quantos elementos tem a lista:
print(len(num))
# Inserir um valor em qualquer posição
num.insert(2,0)  # add o 0 na posisão dois # como no excel add coluna as outras col vão para frente # no caso o 0 na pos 2 a pos 2 vira 3 em assim por diante
print(num)
num.pop() # elimina o ultimo item
print(num)
num.pop(2)  # elimina o item na pos 2
print(num)
del num[2] # elimina o item na pos 2
print(num)
num.remove(2)#vai remomer a primeira ocorrência deste item # vai remover exatamente o que esta entre parenteses we estiver na lista(caso n estiver é erro)
# para evitar dar erro
if 2 in num:
    num.remove(2)
else:
    print('Não tem número 2 ')
print(num)
num.insert(2,6,)
print(num)