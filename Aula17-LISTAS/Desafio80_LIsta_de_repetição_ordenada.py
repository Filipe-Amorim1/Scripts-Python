#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
for c in range(0,5):
    n = (int(input('Digite os números para a lista:')))
    if c == 0 or n > lista[-1]:  # Se for o primeiro valor a var lista receberá o valor ,pois como é o primeiro vai ser o maior e menor ao mesmo tempo
        lista.append(n)          # Ou se o valor for maior que o último da lista a var tb recebe normalmente e colocará na  última posição que é o normal do comando.
    else:
        pos = 0
        while pos < len(lista):
            if n<= lista[pos]:
                lista.insert(pos,n)
                break
            pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram{lista}')




