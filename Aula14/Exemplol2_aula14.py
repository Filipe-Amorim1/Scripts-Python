'''for c in range(1,5):                          # Neste comando for o usuário digitará 4 valores e após digitar os 4 treminará
    int(input('Digite um valor: '))
print('FIM')'''

n = 1  # aqui poderiamos começar o n com qualquer valor diferente de zero s
       #  e começar com zero ele já vai começar encerrando o programa pois enquanto n for diferente de zero (n!= 0 ) o laço sera infinito e terminara qnd digitar 0
'''while n != 0:
    n = int(input('Digite um número: '))
print('FIM')    '''

r = 's'
while r == 's':
    n = int(input('Digite um número:'))
    r = str(input('Quer continuar [S/N] ')).lower()
print('FIM')
