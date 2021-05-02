# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
#DEsafio 61 = lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# https://www.youtube.com/watch?time_continue=319&v=BWAWq7n6PCk&feature=emb_title

primeiro = int(input('Digite o número inicial: ')) # Var para digitar o 1 termo de onde deve ser feita a contagem
razão = int(input('Digite a razão da progressão: ')) # var que indicarar de qunatas en quantas casas(númeors) vai pular a progressão
termo = primeiro
cont = 1 # var de contagem para o laço
total = 0
mais = 10
while mais != 0 : #Enquanto a var mais que aparecera no final do laço dentro do laço perguntando quantos termos queremos ver a mais( além dos 10 que estão no laço ) não for 0 ( se o usuário digitar zero termina o laço
    total = total + mais # Var mais foi criada para manter o programa do ex 61 começando com 10 progressões , então a var total
    while cont <= total :
        print('{} ->'.format(termo),end='')
        termo=termo + razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM')








