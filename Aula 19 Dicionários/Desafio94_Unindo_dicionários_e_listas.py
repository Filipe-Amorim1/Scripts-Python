# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

print( '\033[1;32m-='*10,'Relatório das Pessoas Cadastradas','=-'*10,'\033[m')
dicio = {}
lista =[]
somaidades = 0
cont = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ').upper()[0]) #.upper()[0]) colocará td para muiúscula e pegara apenas a 1ª letra
    idade = int(input('Idade: '))
    cont+=1
    somaidades+= idade
    dicio['Nome'] = nome
    dicio['Sexo'] = sexo.upper()
    dicio['idade'] = idade

    lista.append(dicio.copy())
    dicio.clear()
    resp = ''.strip()
    resp = str(input('Quer continuar? S/N'))
    if resp in 'Nn':
        break
    if resp not in 'NnSs':
        print('ERRO! responda S ou N')
        resp = str(input('Quer continuar? S/N'))
print()
print(lista)
print( '\033[1;32m-='*40,'\033[m')
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas .')
print(f'B) A média de idade é {somaidades/cont:5.2f} anos.') # :5.2f formatação 5 casas ,número float , 2 casas decimais.
media = somaidades/cont
print(f'C) As mulheres cadastradas foram ', end='')
for c in lista:
    if c['Sexo'] in 'Ff':
        print(f' {c["Nome"]}',end='')
print()
print('D) A lista de pessoas a cima da média:')
for d in lista:   # neste for o d percorre a lista onde cada chave é um dicionário
    if d['idade'] >= media: # se a chave d idade for maior ou igual a média
        for k,v in d.items(): # este for dentro do for acima vai pecorrer os dicionários dentro da lista caso o if acima seja verdadeiro
            print(f' {k} = {v} ',end= '')
        print()
print( '\033[1;32m-='*40,'\033[1;31m')
print('<<ENCERRADO >>')


