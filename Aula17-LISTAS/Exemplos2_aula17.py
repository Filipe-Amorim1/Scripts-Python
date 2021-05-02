valores = []  # criando lista vazia
valores1 = list # ou assim

print(valores1)
print(valores)

valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
print()
#print('Os valores são:',end='')
#for v in valores:
    #print(',',v,end='')

for cont in range (0,5):  # adicionando valores a lista usando range com .append
    valores.append(int(input('Digite os valores: ')))

for c,v in enumerate(valores):  # o for com o enumerate ela além da chave ele pega a posisão do item , no caso o c vai retornar a posição (0,1,2,3,4....) e v vai retornar o valor da posição no caso os número da lista
    print(f'Na posição {c} encontrei o valor {v}')
print('cheguei ao final da lista')

'''    IPORTANTE   '''
a = [1,5,8,9]   #''' Ao criar uma lista e fazer '''
b = a    #''' E fazer uma receber a outra'''
print(a)  # fazemos uma ligação entre as listas
print(b)   # se alterar uma vai alterar outra
b[2] = 8  # neste caso a posição 2 na var a também receberia 8
print(a)
print(b)
'''Para resolver isto se necessário podemos fatiar a lista'''
a1 =[1,2,3,6,88,5]
b1 = a1[:]  # assim ela recebe todos os elementos de a1 e quando alterar algo em b1 não mudará em a1 ( como no excel o comando colar apenas os valores retira o vinculo)
print(a1)
print(b1)
b1[2] = 8
print(a1)
print(b1)