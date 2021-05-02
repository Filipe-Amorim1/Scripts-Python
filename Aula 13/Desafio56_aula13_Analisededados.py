#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

print('\033[1;33m----- Análise de Dados pessoais -----')

soma_idade = 0
media_idade = 0
for dados in range(1,5):
    print('----- {}ª pesssoa -----'.format(dados))
    nome =str(input('Nome: ')).strip()
    idade =int(input('Idade: ').strip())
    sexo = str(input('Sexo M/F: ')).strip()
    soma_idade = soma_idade +idade
media_idade = soma_idade/4

