# https://www.youtube.com/watch?v=Qp2cXfCHk2I&t=351s
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('lápis', 1.75,            # Criado a lista em tupla
            'caderno', 5.00,
            'Estojo', 25,
            'borracha', 2,
            'Mochila', 3.25,
            'canetas', 1,
            'livro', 24.90)
print('-'*30)
print('Listagem de Preço')
print('-'*30)

for item in range (0,len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}',end='')# item é o contador que contará apenas os pares dentro do range que no caso é a posição dos itens na lista , como na lista os produtos ficam na posição par começando em 0,2,4,6... vai printar apenaas os pares
                                      # :.<30 formatação criara 30 pontos alinhados a esquerda
    else:
        print(f'R${listagem[item]:>7.2f}') # :>7. Alinhar 7 espaços a direita
                                           # 2f para os numeros ficarem com duas casas decimais




'''
Mateus Santos
há 1 ano
não precisei dessa parte se eh par ou impar, pulei de dois em dois msm:


produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)'''
