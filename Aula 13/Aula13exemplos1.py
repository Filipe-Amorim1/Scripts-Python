for c in range (0,6): # para c (c é o nome do laço pode ser qquer nome ) in (no) range (intervalo) 0 até 6 ,
    print('oi')                  # sempre no útimo número o python vai parar ou sair do laço para o px comando. vai contar de 0 a 5 ou seja 6x saira ou parara no 7
print('Fim') # O print com a indentação mais recuada indicando a saida do laço , se tivesse alinhado abaixo do print acima entraria no laço e repetiria Oi e Fim 6x

for c in range (0,6):
    print(c)  # nesse caso ele vai printar o laço que nomeamos como c . 0,1,2,3,4,5 , o último o python ignora , se quizer até seis tem que colocar (0,7)
print('FIM')

for c in range (6,0,-1): # para contar de trás para frente colocar o -1 para contagem regressiva de um em um , se quiser regressiva de 2 em dois coolcar - 2 e assim sucessivamente
       print(c)
print('FIM')

n = int(input('Digite um número:'))
for c in range(1,n+1): # Nesse caso a contagem sera de 1 até o número digitado pelo usuário , o +1 é para contar até o número que o usuário digitou ,
                       # pois se não contaria 1 a menos pois no ultimo número o pythin não conta ele tem como a saída do laço
    print(c)


