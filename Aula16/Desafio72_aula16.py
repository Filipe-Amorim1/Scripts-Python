#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('\033[1;35m='*15,'NÙMEROS POR EXTENSO','='*15,'\033[m',          '-1 para SAIR')

tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','teze','catorze','quinze','dezesseis','dezessete ','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite o número que você que por extenso de 0 até 20: '))
    if num > 20 or num < -2: # botei -2 para liberar o - 1 para encerrar o programa
        print('número inválido')
        continue# A instrução continue interrompe a execução do ciclo sem interromper a execução do laço de repetição.
    elif num == -1:
        print('\033[1;31mPROGRAMA ENCERRADO')
        break
    print('\033[1;32m',tupla[num],'\033[m')





