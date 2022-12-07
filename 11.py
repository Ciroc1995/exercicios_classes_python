class Carro:
    def __init__(self, consumo:float, nivel_combustivel = 0):
        self.consumo = consumo
        self.nivel_combustivel = nivel_combustivel

    def adicionar_gasolina(self, quantidade_litros):
        self.nivel_combustivel += quantidade_litros
        print(f'Abasteceu {quantidade_litros} litros no tanque')

    def andar(self, distancia):
        gasto_gasolina = distancia / self.consumo
        self.nivel_combustivel -= gasto_gasolina

    def obter_gasolina(self):
        print(f'Nível de combustível alterado para {self.nivel_combustivel:.2f} litros')


carro = Carro(15)
carro.adicionar_gasolina(20)
carro.andar(100)
carro.obter_gasolina()