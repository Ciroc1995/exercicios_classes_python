class Conta:
    def __init__(self, numero:int, titular:str, saldo = 0):
        self.numero = numero
        self._titular = titular.title()
        self.saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        self._titular = novo_titular.title()

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f'Número: {self.numero} - Titular: {self._titular} - Saldo: R${self.saldo:.2f}')


conta = Conta(123, 'matues')

conta.titular = 'cicero'

conta.deposito(60)

conta.saque(20)

conta.extrato()


