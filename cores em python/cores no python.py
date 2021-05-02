print('\033[1;31;43m Olá mundo')
print('\033[1;31;43m Olá mundo\33[m') #Colocar o código no final antes do fechamento da aspas para não repetir a formatação para o restante
# O código para colocar cores é \33[ m
# No espaço entre o [ e m   colocaremos os códigos separados por ;
print('\033[1;32;41m Olá mundo')
print('\033[1;32;42m Olá mundo')
print('\033[1;34;43m Olá mundo')
print('\033[4;35;44m Olá mundo')
print('\033[0;36;45m Olá mundo\33[m')
print('\033[4;37;40m Olá mundo\33[m')
print('\033[4;32;46m Olá mundo\33[m')
print('\033[1;30;47m Olá mundo\33[m')

a = 1
b = 2
print('O valores das var são \33[32m{}\33[m e \33[31m{}\33[m  '.format(a,b))
# colorimos as var com o comando no início das chaves o comando para a cor e no final o comando para encerrar a formatação
nome ='Filipe'
print('Olá muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))
# Com o comando format podemos fazer a formatação temos que criar as chaves para cada formatação
# note que se não encerrar a formatação as !!! ficariam da mesma cor