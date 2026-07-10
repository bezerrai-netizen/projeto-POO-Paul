from mixins import DormirMixin, LogMixin, SalvarMixin, CarregarMixin
from status import Status
from carteira import Carteira
from inventario import Inventario
import csv
from abc import ABC
import os

class Bicho(DormirMixin, LogMixin, SalvarMixin, CarregarMixin):

    def __init__(self, nome):

        self.nome = nome
        self.idade = 0

        self.status = Status()
        self.carteira = Carteira()
        self.inventario = Inventario()

    def comer(self, nome_comida):

        if self.inventario.usar(nome_comida, self):
            self.verificar_estado()

    def brincar(self):

        self.status.fome += 10
        self.status.sujeira += 5
        self.status.sono += 10
        self.status.energia -= 15
        self.status.felicidade += 20
        self.idade += 0.1
        

        self.log(f"{self.nome} brincou.")

    def banho(self):

        if self.status.sujeira == 0:
            print(f"{self.nome} já está limpo.")
            return

        self.status.sujeira -= 40
        self.status.felicidade += 5

        self.log(f"{self.nome} tomou banho.")

    def mostrar_status(self):

        print(f"\n===== {self.nome.upper()} =====")
        print(f"Idade: {self.idade:.1f} anos")
        print(f"Dinheiro: {self.carteira}")
        print(self.status)

    def verificar_estado(self):

        if self.status.fome >= 100:
            self.status.saude -= 10

        if self.status.sono >= 100:
            self.status.saude -= 10

        if self.status.sujeira >= 100:
            self.status.saude -= 10

        if self.status.saude <= 0:
            self.status.saude = 0
            self.status.vivo = False

    def dados_csv(self):

        return [

            self.nome,

            self.idade,

            self.status.saude,
            self.status.fome,
            self.status.sono,
            self.status.energia,
            self.status.felicidade,
            self.status.sujeira,
            self.carteira.saldo,
            1 if self.status.vivo else 0,
            

            "|".join(item.nome for item in self.inventario)
        ]

    def __str__(self):

        return self.nome

