class Quadrado:
    def __init__(self, lado:float):
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, novo_lado):
        self.__lado = novo_lado

    def calcular_area(self):
        area = self.__lado ** 2
        print(f'Área: {area:.2f}m²')
        return area

quadrado = Quadrado(8)
quadrado.lado = 12
quadrado.calcular_area()
