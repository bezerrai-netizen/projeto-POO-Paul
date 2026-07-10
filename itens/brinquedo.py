from itens.item import Item


class Brinquedo(Item):

    def __init__(self, nome, preco, diversao):

        super().__init__(nome, preco)

        self.diversao = diversao

    def usar(self, bicho):

        bicho.status.felicidade += self.diversao
        bicho.status.energia -= 10
        bicho.status.fome += 5

        print(f"{bicho.nome} brincou com {self.nome}.")