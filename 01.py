class Bola:
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor

    def mostrar_cor(self):
        print(f'Cor: {self._cor}')

bola = Bola('azul', 1000, 'couro')
bola.cor = 'preta'
bola.mostrar_cor()
