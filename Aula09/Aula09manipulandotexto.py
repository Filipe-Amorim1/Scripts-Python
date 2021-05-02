#
frase = 'Curso em Video Python'
print(frase[3]) # retornara a 4º letra da frase começa a contar em zero por isso 4º
print(frase[:]) # frase toda do início ao fim
print(frase[1:15:2]) # 1 ao 14 pulando de 2 em 2
print('oi')

# Para escrever um texto longo obdecendo as quebras de linhas , não precisa criar um print para cada linha
# Basta colocar 3 aspas no início ''' e 3 no fim '''
print('''  Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join().''')

print(frase.count('o')) # contou quantos o minúsculos tem na var
print(len(frase)) # conta quantos caractere tem na var incluindo espaços tudo.
print(frase.lstrip())
print(frase.split()) # dividiu a frase por palavras

