class Funcionario:
    def __init__(self, nome:str, salario:float):
        self._nome = nome.title()
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def aumentar_salario(self, percentual_aumento):
        self._salario *= (percentual_aumento + 100) / 100
        print(f'Salário aumentou para R${self._salario:.2f}')

funcionario = Funcionario('cicero', 25000)
funcionario.aumentar_salario(10)



