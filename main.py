import csv
from meu_bicho import Bicho
from loja import Loja
import os


SAVE = "saves/save.csv"

if os.path.exists(SAVE):
    pet = Bicho.carregar(Bicho, SAVE)
else:
    pet = Bicho("Paul")

loja = Loja()



while True:

    print("\n===== MENU =====")
    print("1 - Status")
    print("2 - Loja")
    print("3 - Inventário")
    print("4 - Brincar")
    print("5 - Banho")
    print("6 - Dormir")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        pet.mostrar_status()

    elif opcao == "2":

        loja.listar()

        nome = input("Qual item deseja comprar? ")

        loja.vender(nome, pet)

    elif opcao == "3":

        pet.inventario.listar()

        usar = input("Usar algum item? (s/n): ")

        if usar.lower() == "s":
            nome = input("Nome do item: ")
            pet.comer(nome)

    elif opcao == "4":
        pet.brincar()

    elif opcao == "5":
        pet.banho()

    elif opcao == "6":
        pet.dormir()

    elif opcao == "0":
        pet.salvar(SAVE)
        break

    else:
        print("Opção inválida.")


import csv

