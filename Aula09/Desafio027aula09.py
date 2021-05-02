# Leia o nome completo de uma pessoa , mostrando em seguida
# o primeiro e o último nome separadamente
# Só o 1º e o último independente

nome = str(input('Digite seu nome:')).strip()
n = nome.split()
print('O primeiro nome é {} , o último nome é {}'.format(n[0],n[-1])) # 0 vai ler a primeira, -1 vai ler a ultima - 2 a penultima
# do zero pra cima vai lendo subindo , do -1 negativamente -2, - 3 ..... vai voltando as letras no caso as palavras fatiadas pelo comando strip
