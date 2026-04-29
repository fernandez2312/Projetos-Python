'''
Exercício: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar cliente e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limte, sacar, depositar e consultar saldo
'''

from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Fe', '123.456.789-99','25')


conta_do_fe = Conta(cliente1, 15.00)

print(conta_do_fe.cliente.nome, conta_do_fe.consulta_saldo())

conta_do_fe.depositar(2500.5)

print(conta_do_fe.consulta_saldo())

conta_do_fe.sacar(1000)

print(conta_do_fe.consulta_saldo())

conta_do_fe.sacar(1000)

print(conta_do_fe.consulta_saldo())