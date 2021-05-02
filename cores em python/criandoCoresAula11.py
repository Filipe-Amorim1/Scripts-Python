nome = 'Filipe'
cores = { 'limpa':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretoebranco':'\033[7;30m'}

print('Olá muito prazer em te conhecer {}{}{}!!'.format(cores['pretoebranco'],nome,cores['limpa']))

# Podemos criar uma variável com as formatoções que queremos
# podemos botar o nome da cor e formatação na var
# depois usamos elas com o comando format como no exemplo