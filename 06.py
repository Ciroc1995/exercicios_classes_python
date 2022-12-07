class TV:
    def __init__(self, canal = 0, volume = 0):
        self.canal = canal
        self.volume = volume

    def selecionar_canal(self, canal):
        if canal > 0 and canal < 100:
            self.canal = canal
        else:
            print('Canal inválido')

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def mostrar_tv(self):
        print(f'Canal: {self.canal} - Volume: {self.volume}%')

tv = TV()
tv.selecionar_canal(50)

tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()

tv.mostrar_tv()