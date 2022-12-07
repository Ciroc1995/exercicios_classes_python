class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @base.setter
    def base(self, nova_base):
        self._base = nova_base

    @altura.setter
    def altura(self, nova_altura):
        self._altura = nova_altura

    def calcular_area(self):
        area = self._base * self._altura
        return area

    def calcular_perimetro(self):
        perimetro = (self._base * 2) + (self._altura * 2)
        return perimetro


x_local = float(input('Valor da base do local: '))
y_local = float(input('Valor da altura do local: '))

local = Retangulo(x_local, y_local)

print(f'É necessário uma área de {local.calcular_area()}m² para pisos e perímetro de {local.calcular_perimetro()}m para rodapés')