'''
Exercício:
Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exército
Para entrar no exército é preciso ter mais de 18 anos
pesar mais ou igual a 60 kilos
e medir mais ou igual a 1,70 metros
'''

idade = int(input('Escreva sua idade:'))
peso = float(input('Escreva seu peso:'))
altura = float(input('Escreva sua altura:'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto a servir o exército')
else:
    print('Você não está apto a serviro exército')