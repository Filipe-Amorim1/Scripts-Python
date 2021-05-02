#dizer se tem silva no nome
nome = str(input('Digite um nome:')).strip()# para eliminar os espaõs a frete e atras
print(nome.find('Silva'))
print("Silva" in nome)

# Outro jeito se tem Filipe no primeiro nome
nome = str(input('Digite um nome:')).strip()
print(nome[:6].upper() == 'FILIPE') # .upper foi para resolver o problema de botarem letras maiúsculas e minúsculas e o python não reconhcer ,
                                    # então .upper jogará tudo para maiúscula e reconhecerá pela escrita do nome independente da escrita em mai. ou min.
                                    # ESCREVER A PALAVRA PROCURADA EM MAIÚSCULA NA FÓRMULA  print(nome[:6].upper() == 'FILIPE')



