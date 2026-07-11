import csv
from meu_bicho import Bicho
from loja import Loja
import os
from minijogos import Jogo_da_cobrinha


SAVE = "saves/save.csv"
SAVE_INVENTARIO = "saves/inventario.csv"
if os.path.exists(SAVE):
    pet = Bicho.carregar(Bicho, SAVE)
    pet.carregar_inventario(SAVE_INVENTARIO)
else:
    pet = Bicho("Paul")

loja = Loja()

while True:

    pet.atualizar_status()

    print("\n===== MENU =====")
    print("1 - Status")
    print("2 - Loja")
    print("3 - Inventário")
    print("4 - Brincar")
    print("5 - Banho")
    print("6 - Dormir")
    print("7 - jogar minijogo")
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
    
    elif opcao == "7":
        Jogo_da_cobrinha.rodar
        if Jogo_da_cobrinha.rodar:
            pet.carteira += 30
            pet.status.sono += 20
        

    elif opcao == "0":
        pet.salvar(Bicho, SAVE)
        pet.inventario.salvar_inventario(SAVE_INVENTARIO)
        break

    else:
        print("Opção inválida.")


import csv

