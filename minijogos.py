from abc import ABC, abstractmethod
import curses
import random
class Migame(ABC):
    @abstractmethod
    def rodar(self) -> bool:
        pass
    

class Jogo_da_cobrinha(Migame):
    def rodar(stdscr):
        curses.curs_set(0)

        altura = 20
        largura = 40

        janela = curses.newwin(altura, largura, 0, 0)
        janela.keypad(True)
        janela.timeout(100)   # atualiza a cada 100 ms

        cobra = [
            [10, 15],
            [10, 14],
            [10, 13]
        ]

        direcao = curses.KEY_RIGHT

        comida = [5, 20]
        janela.addch(comida[0], comida[1], "*")

        while True:

            tecla = janela.getch()

            if tecla in [curses.KEY_UP,
                        curses.KEY_DOWN,
                        curses.KEY_LEFT,
                        curses.KEY_RIGHT]:
                direcao = tecla

            cabeca = cobra[0].copy()

            if direcao == curses.KEY_RIGHT:
                cabeca[1] += 1

            elif direcao == curses.KEY_LEFT:
                cabeca[1] -= 1

            elif direcao == curses.KEY_UP:
                cabeca[0] -= 1

            elif direcao == curses.KEY_DOWN:
                cabeca[0] += 1

            # bateu na parede
            if (
                cabeca[0] == 0 or
                cabeca[0] == altura-1 or
                cabeca[1] == 0 or
                cabeca[1] == largura-1
            ):
                break

            cobra.insert(0, cabeca)

            if cabeca == comida:

                while True:
                    comida = [
                        random.randint(1, altura-2),
                        random.randint(1, largura-2)
                    ]

                    if comida not in cobra:
                        break

                janela.addch(comida[0], comida[1], "*")

            else:
                cauda = cobra.pop()
                janela.addch(cauda[0], cauda[1], " ")

            janela.addch(cabeca[0], cabeca[1], "#")

        return len(cobra) - 3

    pontos = curses.wrapper(jogo)

    print(f"Fim de jogo! Pontuação: {pontos}")
    
class Jogo_de_desviar(Migame):
    def rodar(self):
        return True

class Spaceinvaders(Migame):
    def rodar(self):
        return True
    


        








