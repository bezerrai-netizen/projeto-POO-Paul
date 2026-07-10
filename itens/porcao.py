from itens.item import Item


class Pocao(Item):

    def __init__(self, nome, preco, atributo, valor):

        super().__init__(nome, preco)

        self.atributo = atributo
        self.valor = valor

    def usar(self, bicho):

        atual = getattr(bicho.status, self.atributo)

        setattr(
            bicho.status,
            self.atributo,
            atual + self.valor
        )

        print(f"{bicho.nome} usou {self.nome}.")