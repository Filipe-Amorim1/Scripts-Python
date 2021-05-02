# ler uma frase e dizer se éla é um palindromo
# LEr de trás pra frente e de frente pra trás e dar na mesma
# Ana , Anotaram a data da maratona , A torre da derrota , A sacada de casa, Apos a sopa
# desconsiderando os espaços
print('\033[1;32m---------- TESTE DE PALINDRO ----------')

frase = str(input('Digite uma frase:').strip().upper())  # strip para não ter problemas de o usuario dar espaços no começo  # Upper para transformar tudo em maiuscula para não ter problemas de reconhecimento das letrars mmin e mai
palavras = frase.split() # var criada para dividir a var frase em palavras
junto = ''.join(palavras)  # ''.join  esse comando junta a frase com o que colocarmos entre as aspas , no caso como queremos colar a frase , colocamos aspas sem nada no meio .
inverso = ''

# Após os comandos acima onde usamos o split para dividir a frase em palavras depois o join sem nada entre as aspas para juntar as palavras
# Faremos um laço de repetição onde a frase sera analisada com o comando len
# a frase esta toda junta na var junto
# O laço nomeado de letra usara o comando len -1 para começar da ultima letra , -1 para ir até o começo , e -1 para pular letra de uma em um de trás para frente
for letra in range (len(junto)-1,-1,-1):
    inverso = inverso+junto[letra]  # A  var inverso foi criada vazia , e aqui entrou somando a str que conforme o laço foi feito juntara as letras uma a uma de trás para frente para depois verificarmos  se é palindro
print(junto,inverso)
if junto == inverso:
    print('\033[1;33mTemos um Palindro')
else:
    print('\033[1;034mNão temos um Palindro')