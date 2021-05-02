#tabuada 2.0
# faça a tabuada do número digitado
print('\033[1;34m-=-=-=-=--=- Tabuada 2.0 -=-=-=-=-=-=')
n = int(input('Digite o número para saber a tabuada :'))
for c in range (1,11,1): # este laço contará de 1 até 10 ( começa em 1 , 11 é pq o ultimo não conta pois é a saida do laço em for , o ultimo 1 indica para contar de 1 em um progressivamente , se fosse -1 era contagem de trás para frente
    print('\033[1;35m',n,'x',c,'=',c*n)

