'''
Exercício: Escreva uma função que recebe um obejto de coleção
e retorna o valor do maior número dentro dessa coleção
faça outra função que retorna o menor número dessa coleçao
'''

def maior(coleção):
    maior_item = coleção[0]
    for item in coleção:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(coleção):
    menor_item = coleção[0]
    for item in coleção:
        if item < menor_item:
            menor_item = item
    return menor_item

print(maior([5,50,-40,32,-15]))