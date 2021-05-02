filme = {'Titulo':'star wars','Ano':1977,'Diretor':'George Lucas' }

print(filme.values())
print(filme.keys())
print(filme.items())
print()
# usando o for para interagir com a var filme
# esse comando é igual o enumerate para listas e tuplas
for k,v in filme.items():
    print(f'O {k} é {v}')
del filme ['Diretor'] # apaga a chave Diretor
print(filme)
filme['Diretor'] = 'FiLipe'  # trocando os valores dentro das chaves no dicionário
filme['Ano'] = '1984'
filme['lançamento'] = 1986 # adicionando uma chave e valor ao item
for k,v in filme.items():
    print(f'O {k} é {v}')
print()

# LISTAS com Dicionários

brasil = []
estado1 = {'uf': 'Rio de janeiro','sigla':' RJ'}
estado2= {'uf':'São paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

# Usando o for e input para adicionar dados ao dicionãrios

estado = {}
brasil1 = []

for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado[' sigla'] = str(input('Sigla do estado:'))
    brasil1.append(estado.copy())  # .copy para copiar os dados para o dicio cada vez que passar no laço é semelahnte ao colocar na lista[:] , se não fizer este comando no caso o print sairia 3 vezes com o mesmo estado e sigla
print(brasil1)

# no for abaixo o 1º for é para percorrer os itens na lista brasil
# O  2º for passara pelas chaves e valores nos itens dos dicionário estado
for e in brasil1:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')

