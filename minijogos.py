from abc import ABC, abstractmethod
import curses
import random
import time
class Migame(ABC):
    @abstractmethod
    def rodar(self) -> bool:
        pass
    def iniciar(self):
        curses.wrapper(self.rodar)
        return True
    

class Jogo_da_cobrinha(Migame):
    def rodar(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        
        

        altura, largura = stdscr.getmaxyx()

        # Cria a janela do jogo
        win = curses.newwin(altura, largura, 0, 0)
        win.keypad(True)
        win.nodelay(True)
        win.timeout(250)

        # Cobra inicial
        cobra = [
            [altura // 2, largura // 2],
            [altura // 2, largura // 2 - 1],
            [altura // 2, largura // 2 - 2],
        ]

        direcao = curses.KEY_RIGHT

        def nova_comida():
            while True:
                pos = [
                    random.randint(1, altura - 2),
                    random.randint(1, largura - 2),
                ]
                if pos not in cobra:
                    return pos

        comida = nova_comida()
        pontos = 0

        while True:
            win.clear()
            win.border()

            win.addstr(0, 2, f" Pontos: {pontos} ")

            win.addch(comida[0], comida[1], "*")

            for parte in cobra:
                win.addch(parte[0], parte[1], "#")

            tecla = win.getch()

            if tecla in (
                curses.KEY_UP,
                curses.KEY_DOWN,
                curses.KEY_LEFT,
                curses.KEY_RIGHT,
            ):
                opostos = {
                    curses.KEY_UP: curses.KEY_DOWN,
                    curses.KEY_DOWN: curses.KEY_UP,
                    curses.KEY_LEFT: curses.KEY_RIGHT,
                    curses.KEY_RIGHT: curses.KEY_LEFT,
                }

                if tecla != opostos[direcao]:
                    direcao = tecla

            cabeca = cobra[0][:]

            if direcao == curses.KEY_UP:
                cabeca[0] -= 1
            elif direcao == curses.KEY_DOWN:
                cabeca[0] += 1
            elif direcao == curses.KEY_LEFT:
                cabeca[1] -= 1
            elif direcao == curses.KEY_RIGHT:
                cabeca[1] += 1

            # Colisão com parede
            if (
                cabeca[0] == 0
                or cabeca[0] == altura - 1
                or cabeca[1] == 0
                or cabeca[1] == largura - 1
            ):
                break

            # Colisão com a própria cobra
            if cabeca in cobra:
                break

            cobra.insert(0, cabeca)

            if cabeca == comida:
                pontos += 1
                comida = nova_comida()
            else:
                cobra.pop()

        win.nodelay(False)
        msg = f"Game Over! Pontos: {pontos} - Pressione qualquer tecla."
        win.addstr(
            altura // 2,
            max(1, (largura - len(msg)) // 2),
            msg
        )
        win.getch()
        return True
class Jogo_de_desviar(Migame):
    def rodar(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.keypad(True)

        altura, largura = stdscr.getmaxyx()

        jogador_x = largura // 2
        jogador_y = altura - 2

        obstaculos = []
        pontos = 0

        while True:
            tecla = stdscr.getch()

            if tecla == curses.KEY_LEFT and jogador_x > 1:
                jogador_x -= 1
            elif tecla == curses.KEY_RIGHT and jogador_x < largura - 2:
                jogador_x += 1
            elif tecla == ord("q"):
                break

            # Cria obstáculo
            if random.random() < 0.15:
                obstaculos.append([0, random.randint(1, largura - 2)])

            # Move obstáculos
            novos = []
            for y, x in obstaculos:
                y += 1

                # Colisão
                if y == jogador_y and x == jogador_x:
                    stdscr.clear()
                    stdscr.addstr(altura // 2, largura // 2 - 5, "GAME OVER")
                    stdscr.addstr(
                        altura // 2 + 1,
                        largura // 2 - 8,
                        f"Pontos: {pontos}"
                    )
                    stdscr.refresh()
                    stdscr.nodelay(False)
                    stdscr.getch()
                    return

                if y < altura:
                    novos.append([y, x])

            obstaculos = novos

            pontos += 1

            stdscr.clear()

            # Desenha obstáculos
            for y, x in obstaculos:
                stdscr.addch(y, x, "#")

            # Desenha jogador
            stdscr.addch(jogador_y, jogador_x, "A")

            stdscr.addstr(0, 0, f"Pontos: {pontos}")
            stdscr.addstr(1, 0, "← → para mover | q para sair")

            stdscr.refresh()
            time.sleep(0.05)
            


class Spaceinvaders(Migame):
    def rodar(self, stdscr):
        curses.curs_set(0)

        altura, largura = stdscr.getmaxyx()

        win = curses.newwin(altura, largura, 0, 0)
        win.keypad(True)
        win.nodelay(True)
        win.timeout(150)

        # Nave
        nave = [altura - 3, largura // 2]

        # Tiros
        tiros = []

        # Inimigos
        inimigos = []

        for y in range(3, 7):
            for x in range(8, largura - 8, 6):
                inimigos.append([y, x])

        direcao_inimigos = 1

        # controla quando eles descem
        pode_descer = True

        pontos = 0
        vidas = 3

        contador_movimento = 0


        while True:

            win.clear()
            win.border()


            # Informações
            win.addstr(
                0,
                2,
                f"Pontos: {pontos}  Vidas: {vidas}"
            )


            # Desenha nave
            win.addstr(
                nave[0],
                nave[1]-1,
                "<^>"
            )


            # Desenha inimigos
            for inimigo in inimigos:
                win.addch(
                    inimigo[0],
                    inimigo[1],
                    "W"
                )


            # Desenha tiros
            for tiro in tiros:
                win.addch(
                    tiro[0],
                    tiro[1],
                    "|"
                )


            tecla = win.getch()


            # Movimento nave
            if tecla == curses.KEY_LEFT:
                if nave[1] > 2:
                    nave[1] -= 1


            elif tecla == curses.KEY_RIGHT:
                if nave[1] < largura-3:
                    nave[1] += 1



            # Atirar
            elif tecla == ord(" "):

                tiros.append(
                    [
                        nave[0]-1,
                        nave[1]
                    ]
                )



            # Atualiza tiros
            for tiro in tiros[:]:

                tiro[0] -= 1

                if tiro[0] <= 1:
                    tiros.remove(tiro)




            # Colisão tiro/inimigo
            for tiro in tiros[:]:

                for inimigo in inimigos[:]:

                    if tiro[0] == inimigo[0] and tiro[1] == inimigo[1]:

                        tiros.remove(tiro)
                        inimigos.remove(inimigo)

                        pontos += 10

                        break





            # Movimento dos inimigos
            contador_movimento += 1


            # deixa eles mais lentos
            if contador_movimento >= 3:

                contador_movimento = 0

                bateu_parede = False


                # verifica borda
                for inimigo in inimigos:

                    if (
                        inimigo[1] <= 2 and direcao_inimigos == -1
                    ) or (
                        inimigo[1] >= largura-3 and direcao_inimigos == 1
                    ):
                        bateu_parede = True
                        break



                if bateu_parede:

                    # troca direção
                    direcao_inimigos *= -1


                    # desce somente uma vez
                    if pode_descer:

                        for inimigo in inimigos:
                            inimigo[0] += 1

                        pode_descer = False


                else:

                    # anda para os lados
                    for inimigo in inimigos:
                        inimigo[1] += direcao_inimigos

                    pode_descer = True





            # Inimigos chegaram perto da nave
            for inimigo in inimigos:

                if inimigo[0] >= altura-4:

                    vidas -= 1

                    inimigos.remove(inimigo)

                    break




            # Vitória
            if len(inimigos) == 0:

                mensagem = "VOCÊ VENCEU!"

                win.addstr(
                    altura//2,
                    (largura-len(mensagem))//2,
                    mensagem
                )

                win.nodelay(False)
                win.getch()

                return True





            # Derrota
            if vidas <= 0:

                mensagem = f"GAME OVER - Pontos: {pontos}"

                win.addstr(
                    altura//2,
                    (largura-len(mensagem))//2,
                    mensagem
                )

                win.nodelay(False)
                win.getch()

                return False
        








