# Ler o nome de uma pessoa e mostrar
# nome com todas letras maiúsculas
# todas minúsculas
# letras ao todo sem considerar espaços
# letras tem o primeiro nome

nome = str(input('Digite seu nome completo:')).strip() # o .strip no final é para eliminar os espaços no ínicio e no fim para não conta-los
print('Analisando seu nome...')
print('Seu nome tem letras maiúsculas é {}'.format(nome.upper())) # upper todas maiúsculas
print('Seu nome tem letras minúsculas é {}'.format(nome.lower())) #lower todas minúsculas
print('Seu nome tem {} letra'.format(len(nome)- nome.count(' '))) # len para analisar todo nome , -nome.count(' ') para contar os espaços e subtrailos ]
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#EM python podemos ter outras formas de resolver os problemas
# Para contar as letras do primeiro nome usamos a função find para retornar o primeiro espaço que encontrar
# Como o python começa a contar do zero ele vai contar até o espaço e nos dará quantas letras tem no primeiro nome
separa = nome.split()
print('Seu primeiro nome  é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
# Criamos a var separa  recebendo a var nome e separando cada pedaço com o comando split
# Depois mandamos printar a var separa com o primeiro pedaço que é zero ( o comando split corta em pedaços e esses pedaços recebem a numeração começando em zero
# o comando len analisou a parte zero e nos deu o número de letras



