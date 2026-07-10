class Status:

    def __init__(self):
        self.__saude = 100
        self.__fome = 0
        self.__sono = 0
        self.__energia = 100
        self.__felicidade = 100
        self.__sujeira = 0
        self.__vivo = True

    @property
    def saude(self):
        return self.__saude

    @saude.setter
    def saude(self, valor):
        self.__saude = max(0, min(100, valor))

    @property
    def fome(self):
        return self.__fome

    @fome.setter
    def fome(self, valor):
        self.__fome = max(0, min(100, valor))

    @property
    def sono(self):
        return self.__sono

    @sono.setter
    def sono(self, valor):
        self.__sono = max(0, min(100, valor))

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        self.__energia = max(0, min(100, valor))

    @property
    def felicidade(self):
        return self.__felicidade

    @felicidade.setter
    def felicidade(self, valor):
        self.__felicidade = max(0, min(100, valor))

    @property
    def sujeira(self):
        return self.__sujeira

    @sujeira.setter
    def sujeira(self, valor):
        self.__sujeira = max(0, min(100, valor))
    @property
    def vivo(self):
        return self.__vivo
    @vivo.setter
    def vivo(self, valor):
        self.__vivo = valor

    def __str__(self):

        return (
            f"❤️ Saúde: {self.saude}\n"
            f"🍖 Fome: {self.fome}\n"
            f"😴 Sono: {self.sono}\n"
            f"⚡ Energia: {self.energia}\n"
            f"😊 Felicidade: {self.felicidade}\n"
            f"🛁 Sujeira: {self.sujeira}"
        )