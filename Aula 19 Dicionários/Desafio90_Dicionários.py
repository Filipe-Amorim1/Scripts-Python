# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

print('\033[1;32m===== Situação Escolar dos Alunos =====\033[m')

nome = str(input('Nome: '))
media = float(input('Média: '))
ficha = {'Nome':'','Média':'','Situação':''}
if media >= 7:
    ficha['Situação'] = 'Aprovado'
elif media <7 and media >= 6:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado'
ficha['Nome'] = nome
ficha['Média'] = media
print('\033[1;34m')
for k,v in ficha.items():
    print(f'{k} é igual a {v}')


