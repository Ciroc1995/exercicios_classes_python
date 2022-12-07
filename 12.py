class Conta:
    def __init__(self, saldo:float, taxa_juros:float):
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def adicione_juros(self, taxa_juros):
        self.saldo *= (taxa_juros + 100) / 100
        print(f'Saldo alterado para R${self.saldo:.2f}')

conta = Conta(1000, 10)

conta.adicione_juros(10)
conta.adicione_juros(10)
conta.adicione_juros(10)
conta.adicione_juros(10)
conta.adicione_juros(10)