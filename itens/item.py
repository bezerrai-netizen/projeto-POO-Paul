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