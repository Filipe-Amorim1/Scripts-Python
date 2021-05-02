# Valor a ser pago CONSIDERANDO PREÇO normal e condição de pgto
# Preço normal e condição de pagamento
# à vista no dinheiro 10% desc
# a vista no cartão 5% desc
# Até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

print('\033[35m ---------VALOR TOTAL DE PAGAMENTO ----------')
preço = float(input('\033[1;34mDigite o Preço do produto:R$ '))
pgto = int(input('Digite o número de parcelas x '))
formapgto =int(input('Digite [ 1 ] para dinheiro ou [ 2 ] para cartão : '))
avdin = float(preço-(preço*0.1))
avcartao =  float(preço - (preço*0.05))

if formapgto == 1 and pgto == 1:
    print('\033[1;33mR$',avdin)
elif formapgto == 2 and pgto == 1:
    print('\033[1;36mR$',avcartao)
elif formapgto == 2 and pgto == 2 :
    print('\033[1;31mR$',preço)
elif formapgto == 1 and pgto > 2:
    print('Não parcelamos a compra no dinheiro')
elif  2 != formapgto != 1:
    print('\033[1;31mForma de pagamento inválida, Digite [ 2 ] para pagamento no cartão ou [ 1 ] para pagaer em Dinheiro.')
elif pgto > 12 or pgto < 1:
    print('Opção de parcelamento inválida, parcelamos a compra de 2 até 12 x no cartão.')
else:
    print('\033[1;34mR$',preço+(preço*0.2))

