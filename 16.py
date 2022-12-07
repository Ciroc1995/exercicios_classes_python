class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self._nome = nome.title()
        self._fome = fome
        self._saude = saude
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def fome(self):
        return self._fome

    @property
    def saude(self):
        return self._saude

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @fome.setter
    def fome(self, nova_fome):
        self._fome = nova_fome

    @saude.setter
    def saude(self, nova_saude):
        self._saude = nova_saude

    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

    def alimenta_tamagushi(self, quantidade):
        if quantidade > 0 and quantidade <= 100:
            self._fome -= self._fome * (quantidade / 100)

    def brinca_bichinho(self, quantidade):
        if quantidade > 0 and quantidade <= 100:
            self._saude += self._saude * (quantidade / 100)

    def humor(self):
        return self._fome * self._saude


    def __str__(self):
        print(f'Nome: {self._nome}')
        print(f'Fome: {self._fome}')
        print(f'Saúde: {self._saude}')
        print(f'Idade: {self._idade}')

tamagushi = Tamagushi('cicero', 20, 20, 20)

tamagushi.alimenta_tamagushi(50)

tamagushi.brinca_bichinho(20)

tamagushi.__str__()