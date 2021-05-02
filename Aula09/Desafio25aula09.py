# Ler uma frase pelo teclado e mostera
# Quantas vezes aparece a letra A
# posição que a letra A aparece a 1ª vez
# e a ultima vez que a letra a aparece

frase = str(input('Digite uma frase:')).strip()
n = frase.lower()  # Crimamos a variável n para não ter problemas se for digitado letra maiúsculas ou minúsculas .
                   # O comando na var n, sera para tranformar td em minusculas ,poderia ser tudo em maiu.
                   # Assim o python vai contar certo todos as letras pois se fossem misturadas
                   # (ex letras a e A o python contaria só a descrita
                   # obs nesse caso lembrar de colocar as letras procuraddas em minusculas já que o python transformará a var em minúscula
                   # frase = str(input('Digite uma frase:')).lower() PODERIA SER USADO ESTE MEDOTO DIRETO NA 1ª VAR .lower  (ou  .upper para mius)
print('A frase possui {} letra(s) A'.format(n.count('a')))
print('A primeira letra A aparece na posição {}'.format(n.find('a')+1)) # +1 pois o python começa a contar do zero
print('A última letra A aparece na posição {} '. format(n.rfind('a')+1))# rfind começou a procurar da esquerda (procura da esquerda mais retorna a posição começando a contar do inicio direita .Botamos tb o +1 pois começa a contar do zero



