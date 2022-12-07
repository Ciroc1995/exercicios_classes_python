class Macaco:
    def __init__(self, nome):
        self.nome = nome.title()
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def ver_bucho(self):
        print(f'{self.nome} contém {self.bucho} dentro de seu estômago')

    def digerir(self):
        comida_permitida = ['banana', 'laranja', 'melancia']
        for i in range(len(comida_permitida)):
            if self.bucho[i] in comida_permitida:
                print(f'{self.bucho[i]} foi digerido pelo macaco {self.nome}')
            else:
                print(f'{self.bucho[i]} não foi digerido pelo macaco {self.nome}')

macaco = Macaco('Xito')

macaco2 = Macaco('Xita')

macaco.comer('banana')
macaco.comer('melancia')
macaco.comer('abacaxi')

macaco2.comer('laranja')
macaco2.comer('banana')
macaco2.comer('acerola')

macaco.ver_bucho()
macaco2.ver_bucho()