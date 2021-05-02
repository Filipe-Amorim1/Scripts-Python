# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print('\033[1;34m-='*5,'Contador de Vogais','=-'*5,'\033[m')

tupla = ('Palavra','Casa','grátis','Apartamento','Rua', 'mulher','cachorro')
vogal = ('a','e','i','o','u')
for c in tupla:     # for vai passar pela var tupla e printar cada item , 0,1,2,3......
    print(f'\nNa palavra \033[1;32m{c}\033[m temos as vogais: ',end='' )
    for letra in c:  # este for aninhado vai receber no loop osw itens da var c que passou pela var tupla e pegar os elementos que a compoem no caso as letras .Cada letra é 0,1,2,3....( exemplo palavra 0=p , 1=a 2=l ......) e vai printar em sweguida a letra.
        if letra.lower() in 'áàââaeéêiíoôóuúü': #  No caso não vai printar todas as letras e sim vai agir conforme o if , que pede para printar apenas o que estiver em (aeiou" as vogais.
            print('\033[1;32m',letra,',\033[m',end='')




'''tupla = ('Palavra','Casa','Apartamento','Rua')

vogal = ('a','e','i','o','u')

for x in tupla:
    print(f'Na palavra {x}, existem as vogais:', end='')
    for y in vogal:
        if y in x:
            print (f' {y}',end='')
    print('.')'''