from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    @abstractmethod
    def usar(self, bicho):
        pass

    def __str__(self):
        return self.nome
    
class Brinquedo(Item):

    def __init__(self, nome, preco, diversao):

        super().__init__(nome, preco)

        self.diversao = diversao

    def usar(self, bicho):

        bicho.status.felicidade += self.diversao
        bicho.status.energia -= 10
        bicho.status.fome += 5

        print(f"{bicho.nome} brincou com {self.nome}.")

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