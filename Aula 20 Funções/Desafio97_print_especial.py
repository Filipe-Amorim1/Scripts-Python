# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

nome = str(input('Nome: '))
curso = str(input('Curso: '))
sigla = str(input('Sigla: '))
def escreva ():
    print('~'*(len(nome)+4))
    print(f'  {nome}')
    print('~'*(len(nome)+4))
    print('~'*(len(curso)+4))
    print(f'  {curso}')
    print('~'*(len(curso)+4))
    print('~'*(len(sigla)+4))
    print(f'  {sigla}')
    print('~'*(len(sigla)+4))
print()

escreva()

'''def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)

escreva('Filipe')
escreva('Curso em Vídeo')
escreva('CEV')'''