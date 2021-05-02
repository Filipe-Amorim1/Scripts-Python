# Ler o peso de 5 pessoas
# Mostrar o maior e menor peso lidos
# https://www.cursoemvideo.com/course/python-3-mundo-2/aulas/repeticoes-em-python-for/modulos/exercicio-55-maior-e-menor-da-sequencia/

print('\033[1;35m--------- Classificação de peso ---------')
maior = 0
menor = 0
for pessoas in range(1,6):
    peso=float(input('Digite o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:           # Nessa estrutura if indica que se a pessoa for igual a 1ª ou seja o primeiro laço
        maior = peso       # Logo obvio que teremos o menor peso igual ao meior pois só tem um peso digitado
        menor = peso
    else:                  # em seguida começa a passar os px pesos das pessoas no laço
        if peso > maior:       # Assim se o peso lido for maior que o numero que temos no 1º laço
           maior = peso       # maior receberá o peso
        if peso < menor:    # se o peso for menor que o menor peso o menor peso passa a ser o peso
            menor = peso
print('\033[1;36mO maior peso lido foi de \033[1;32m{}Kg\033[m'.format(maior))
print('\033[1;36mO menor peso lido foi de \033[1;31m{}Kg'.format(menor))



print( 'NOvo teste de peso ')
m = 0
ma = 0
for p in range(1,6):
    pe=float(input('dg:'))
    if p == 1:
        m = pe
        ma = pe
    else:
        if pe > ma:
            ma = pe
        if pe < m:
            m = pe
print(m)
print(ma)
