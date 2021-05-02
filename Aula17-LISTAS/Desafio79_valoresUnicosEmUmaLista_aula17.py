#: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valor =[]
while True:
    try:
        n =int(input('Digite um número: '))
    except:
        print('Valor inválido:')
    else:
        if n not in valor:
            valor.append(n)
            print('Valor adicionado')
        else:
            print('Valor duplicado')
        r = str(input('Quer continuar [S/N]: ').strip())
        if r in ('Nn'):
            break
print()
print(f'Os valores digitados foram {valor}')
