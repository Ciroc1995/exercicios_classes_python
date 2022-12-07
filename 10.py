class Bomba:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        quantidade_litros = valor / self.valor_litro
        self.__abastecer_se_possivel(valor, quantidade_litros)

    def __abastecer_se_possivel(self, valor, quantidade_litros):
        if quantidade_litros > self.quantidade_combustivel:
            print(f'Faltam {quantidade_litros - self.quantidade_combustivel:.2f} litros na bomba')
        else:
            self.quantidade_combustivel -= quantidade_litros
            print(f'Foram abastecidos {quantidade_litros:.2f} litros a um valor de R${valor:.2f}')
            print(f'Sobraram {self.quantidade_combustivel:.2f} litros na bomba')

    def abastecer_por_litro(self, quantidade_litros):
        valor = quantidade_litros * self.valor_litro
        self.__abastecer_se_possivel(valor, quantidade_litros)

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, quantidade_litros):
        if quantidade_litros > 0:
            self.quantidade_combustivel += quantidade_litros
            print(f'Quantidade de combustível alterada para {self.quantidade_combustivel:.2f} litros')
        else:
            print('Não é possível retirar combustível da bomba')


bomba = Bomba('gasolina', 4.69, 100)

bomba.abastecer_por_valor(50)

bomba.abastecer_por_litro(50)

bomba.alterar_quantidade_combustivel(-100)

