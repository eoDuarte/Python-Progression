n = input('Digite os números separados por virgula para saber a média: ')
lista_numeros = [float(n) for numero in n.split(',')]
media = sum(lista_numeros) / len(lista_numeros)

print(media)
