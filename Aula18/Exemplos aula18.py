'''dados = []
pessoas = []

dados.append('Pedro')
dados.append(25)
print(dados)

pessoas.append(dados[:])
print(pessoas)'''

teste = []
teste.append('Filipe')
teste.append(36)
galera = []
#galera.append(teste) # se fizer desta forma toda alteração na lista testa na parte que foi copiada vai ser alterada na lista que copiou e vice versa pois fazendo assim haverá uma ligação entre as listas (como no excel copiar e colar fica o vincula a naõ ser que escolhemos a opção copiar apenas valores)
galera.append(teste[:]) # Desta forma copia os valores sem o víncula
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#              item 0         item 1       item 2       item 4
pessoas = [[ 'Maria',23],['Filipe',36],['Aline',20],['Juliana',30]]
#              0:0  0:1     1:0   1:1     2:0   2:1    3:0     3:1

# abaixo o for vai percorrendo todos os itens da lista
# no print enquanto passar por cada elemento ele printa o elementos 0 ( nomes) e 1 (idades) de cada item.
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
