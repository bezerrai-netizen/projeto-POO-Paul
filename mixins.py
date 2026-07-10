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

class CarregarMixin:
    
  
    
    def carregar(self, arquivo):

        with open(arquivo, "r", newline="", encoding="utf-8") as csvfile:

            reader = csv.reader(csvfile)

            dados = next(reader)

        pet = self(dados[0])

        pet.idade = float(dados[1])

        pet.status.saude = int(dados[2])
        pet.status.fome = int(dados[3])
        pet.status.sono = int(dados[4])
        pet.status.energia = int(dados[5])
        pet.status.felicidade = int(dados[6])
        pet.status.sujeira = int(dados[7])
        pet.carteira.saldo = int(dados[8])
        pet.status.vivo = int(dados[9]) == 1
        
        return pet