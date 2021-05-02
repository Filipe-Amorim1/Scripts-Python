print("Vamos criar um tabuleiro de tamanho:  N x N")
n=int(input("Valor de N: ") )

for linha in range(n):
    for coluna in range(n):
        print("x  ",end='')
    print()

'''O primeiro laço FOR vai ser responsável por percorrer as linhas.
Ele vai percorrer um intervalo de n linhas, ou seja: range(n)
Dentro de cada linha dessa, precisamos desenhar as colunas, onde cada coluna printamos um "x  ". E quantas vezes isso é feito? n vezes.
Ou seja, vamos usar outro intervalo de valor n: range(n)
Vamos usar uma variação da função print, que não quebra a linha automaticamente. Para isso, basta adicionar o end='' 
na função print, pra definir que no fim dela não fala nada, não coloque nenhum caractere (por padrão ela coloca \n de quebra de linha).
Quando terminar de imprimir cada linha, o que fazemos?
Precisamos dar uma quebra de linha, para o tabuleiro ficar bonitinho, então usamos  print() (isso mesmo, sem nada dentro'''