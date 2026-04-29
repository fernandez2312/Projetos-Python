class Conta:

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print("Foi depositado:", quant)
        else:
            print("Erro no depósito")

    def consulta_saldo(self):
        return self.saldo

    def sacar(self, quant):
        if self.saldo - quant < 0:
            print("Saldo insuficiente")
        else:
            self.saldo -= quant
            print("Foi sacado:", quant)