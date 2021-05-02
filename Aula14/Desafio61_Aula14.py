# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input('Digite o número inicial: '))  # digitou o número para começar a contagem
razão = int(input('Digite a razão da progressão: ')) # n que sera o tamanho da progressão
cont = 1  # var que para controlar o laço

while cont <= 10 :  # o cont vai recebendo abaixo + 1 para fazer 10x (conforme enunciado) a progressão
    print('{} -> '.format(primeiro), end='') # vai printando a var primeiro  cada vez que ele somar mno laço .  end='' é para colocar tudo na mesma linha sem quebra de linha na visuaçizasão do interpretador
    primeiro= primeiro + razão  # primeiro vai recebendo + a razão cada vez que passar no laço fazendo a progressão conforme o incicio e o fim que o usu digitou
    cont = cont + 1   # contador de controle para o laço while
print('FIM')













