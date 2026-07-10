from itens.item import Item


class Comida(Item):

    def __init__(self, nome, preco, saciedade):

        super().__init__(nome, preco)

        self.saciedade = saciedade

    def usar(self, bicho):

        bicho.status.fome -= self.saciedade
        bicho.status.sujeira += 2

        print(f"{bicho.nome} comeu {self.nome}")

    def __int__(self):
        return self.saciedade