# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
print('\033[1;32m='*10,'CADASTRO DE TRABALHOR ','='*10,'\033[m')

from datetime import date
cadastro ={'Nome':'','PIS':'','Idade':''}
dataatual = date.today().year
nome = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
pis = input('PIS: ')
idade = dataatual - ano_nasc

cadastro['Nome'] = nome
cadastro['PIS'] = pis
cadastro['Idade'] = idade
if pis == '0':
    for k , v in cadastro.items():
        print(f'\033[1:32m{k} tem o valor \033[1:31m{v}\033[1:33m')

else:
    ano_contrato = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
    aposentadoria = int(input('Anos trabalhado: '))
    cadastro['Contratação'] = ano_contrato
    cadastro['Salário'] = salario
    cadastro['Aposentadoria'] = ((35 - aposentadoria) + idade)

    for k,v in cadastro.items():
        print(f'\033[1:33m{k} tem o valor \033[1:31m{v}\033[1:33m')




