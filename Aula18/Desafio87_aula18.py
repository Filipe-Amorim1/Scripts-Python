#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
# A matriz tem 3 itens e dentro dos 3 itens temos mais três itens
# para fazer uma varredura em tudo precisamos de um for aninhado
# o primeiro for passará pelos itens 0,1,2 dentro da lista
# o segundo for passará pelos itens dentro do item que no caso são os três zeros
print('\033[1;34m','='*10,'ANÁLISE DE DADOS DA MATRIZ','='*10,'\033[m ')

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Num posição [{l},{c}] :')) # com este comando vamos inserindo os valores em cada lugar que o for aninhado passar
                                                 # vai começar pela var l passando pelo item 0 e vai para o segundo fou passando do 0 ao 2 ,depois var l item 1 e vai para o segundo for passando do 0ao2 no item 1 e assim vai até passar por todos e cada vez que passar vai ser inserido um valor pelo usuário
print('='*30)
for l in range(0,3):  # aqui vai fazer o mesmo esquema acima percorrendo todos os itens da matriz
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='') # ao percorrer será dado print de cada item da matriz no formato [][][]  # :^5 é para ficar com 5 casas e ^ é centrazilar o num
        #print() se o print ficar aqui ficaria um núnmero em baixo do outro
    print() # este print servirá para quebrar a linha após passar pelo primeiro for
somapar = 0
soma_col_3 = 0
maior_col_2 = []
for l in range(0,3) :
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somapar+= matriz [l] [c]
for l in range(0,3):
    soma_col_3+= matriz[l][2]

for l in range(0,3) :
    for c in range(0,3):
        maior_col_2.append(matriz[l][1])
print('='*30)
print(f'A soma dos números pares da matriz é \033[1;33m{somapar}\033[m')
print(f'A soma da coluna 3 da matriz é \033[1;33m{soma_col_3}\033[m')
print(f'O maior valor da coluna 2 é \033[1;33m{max(maior_col_2)}\033[m')












