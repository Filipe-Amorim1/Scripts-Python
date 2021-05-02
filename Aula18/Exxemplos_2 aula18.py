dados =[]
galera = []
totalmai= 0
totalmen = 0

for c in range (0,3):
    dados.append(str(input('Nome:')))
    dados.append(int(input('Idade:')))
    galera.append((dados[:]))  # aqui a var list galera vai recebendo a var lista dados  cada vez que que passa no laço , formando um listas(no caso com dois itens 0 e 1 ) dentro da lista galera
    dados.clear() # apagar a var dados para voltar no laço vazia , caso contrário(sem esse comando) ia acontecer isso na var galera: [['filipe', 111], ['filipe', 111, 'bruna ', 1], ['filipe', 111, 'bruna ', 1, 'ff', 544]]
print(galera)
print(dados)

for p in galera:
    if p[1] >= 21:
        totalmai += 1
        print(f'{p[0]} é maior de idade. ')
    else:
        totalmen+=1
        print(f'{p[0]} é menor de idade.')


print(f'Temos o toral de {totalmen} pessoas menor de idade')
print(f' Temos um total de {totalmai} pessoas maior de idade')
