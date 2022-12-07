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

funcionario = Funcionario('cicero', 1000)

print(funcionario.nome)
print(funcionario.salario)

