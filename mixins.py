from abc import ABC
import csv


class DormirMixin:

    def dormir(self):
        print(f"{self.nome} foi dormir.")

        self.status.sono = 0
        self.status.energia = 100
        self.status.saude += 10
        self.status.fome += 15
        self.verificar_estado()


class LogMixin:

    def log(self, mensagem):
        print(f"[LOG] {mensagem}")


class SalvarMixin(ABC):

    def salvar(self, arquivo):
        """
        Salva o objeto em um CSV.
        O objeto deve possuir o método dados_csv().
        """

        with open(arquivo, "w", newline="", encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(self.dados_csv())