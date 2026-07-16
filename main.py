import csv
from meu_bicho import Bicho
from loja import Loja
import os
from minijogos import Jogo_da_cobrinha, Spaceinvaders, Jogo_de_desviar
import time
import curses
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
    pet.verificar_estado()
    
    print("\n===== MENU =====")
    print("1 - Status")
    print("2 - Loja")
    print("3 - Inventário")
    print("4 - Brincar")
    print("5 - Banho")
    print("6 - Dormir")
    print("7 - jogar minijogo")
    print("8 - Ver Paul")
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
        print("\n=== ESCOLHA UM JOGO ===")
        print("1 - Jogo da Cobrinha")
        print("2 - Space Invaders")
        print("3 - Jogo de desviar")

        opcao = input("Escolha: ")

        if opcao == "1":
            jogocobra = Jogo_da_cobrinha()

            if jogocobra.iniciar():
                pet.ganhar_dinheiro(30)
                pet.status.sono += 20
                pet.status.felicidade += 30
                print("Você ganhou 30 moedas!")

        elif opcao == "2":
            jogo_space = Spaceinvaders()

            if jogo_space.iniciar():
                pet.ganhar_dinheiro(100)
                pet.status.sono += 20
                pet.status.felicidade += 30
                print("Você ganhou 100 moedas!")
        
        elif opcao == "3":
            jogo_desvio = Jogo_de_desviar()

            if jogo_desvio.iniciar():
                pet.ganhar_dinheiro(100)
                pet.status.sono += 20
                pet.status.felicidade += 30
                print("Você ganhou 100 moedas!")

        else:
            print("Jogo inválido!")
                
    elif opcao == "8":

        
        curses.wrapper(pet.animar)
            

    elif opcao == "0":
        pet.salvar(SAVE)
        pet.inventario.salvar_inventario(SAVE_INVENTARIO)
        break

    else:
        print("Opção inválida.")


import csv

