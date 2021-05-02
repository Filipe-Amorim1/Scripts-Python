# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# https://www.youtube.com/watch?v=7xrCJnniqMw&t=552s

lista = []


while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('NOta 2: '))
    média = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],média])
    resp = str(input('Quer continuar S/N: '))
    if resp in 'Nn':
        break
print('='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÈDIA":>8}' ) # formatação 4 casas esquerda 10 casas esq , 8 casas a dir
print('='*30)
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print(f'{" Digite 999 para sair":>40}')
    opc= int(input("mostrar notas de qual aluno : "))
    if opc == 999:
        print('Finalizado')
        break
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('Volte sempre!!!!')

