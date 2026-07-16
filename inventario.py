import csv
class Inventario:

    def __init__(self):
        self.__itens = []

    @property
    def itens(self):
        return self.__itens

    def adicionar(self, item):
        self.__itens.append(item)


    def listar(self):

        if not self.__itens:
            print("Inventário vazio.")
            return

        print("\n===== INVENTÁRIO =====")

        for i, item in enumerate(self.__itens, start=1):
            print(f"{i}. {item.nome} - {item.preco} moedas")

    def procurar(self, nome):

        for item in self.__itens:

            if item.nome.lower() == nome.lower():
                return item

        return None

    def usar(self, nome, bicho):

        item = self.procurar(nome)

        if item is None:
            print("Item não encontrado.")
            return False

        item.usar(bicho)
        self.__itens.remove(item)

        return True
    
    def __iter__(self):
        return iter(self.itens)
    
    def salvar_inventario(self, arquivo):
        with open(arquivo, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["tipo", "nome", "preco"])

            for item in self.__itens:
                writer.writerow([
                    item.__class__.__name__,
                    item.nome,
                    item.preco
                ])
    
    def animar(self, stdscr):
        import curses
        import time

        curses.curs_set(0)

        altura, largura = stdscr.getmaxyx()

        normal = [
            "   _____   ",
            "  /     \\  ",
            " |  o o  | ",
            " |   ^   | ",
            " | \\___/ | ",
            "  \\_____/  "
        ]

        feliz = [
            "   _____   ",
            "  /     \\  ",
            " |  ^ ^  | ",
            " |  \\_/  | ",
            " | \\___/ | ",
            "  \\_____/  "
        ]

        fome = [
            "   _____   ",
            "  /     \\  ",
            " |  o o  | ",
            " |   .   | ",
            " |  ___  | ",
            "  \\_____/  "
        ]

        fome2 = [
            "   _____   ",
            "  /     \\  ",
            " |  - -  | ",
            " |   .   | ",
            " |  ___  | ",
            "  \\_____/  "
        ]

        quadro = 0

        while True:

            # Escolhe animação pelo estado
            if self.status.fome >= 80:
                animacao = [fome, fome2]

            elif self.status.felicidade >= 80:
                animacao = [feliz]

            else:
                animacao = [normal]


            desenho = animacao[quadro % len(animacao)]

            stdscr.clear()

            y = altura // 2
            x = largura // 2 - 5

            for linha in desenho:
                stdscr.addstr(y, x, linha)
                y += 1


            # Mostra status
            stdscr.addstr(
                1,
                2,
                f"Fome: {self.status.fome}  Felicidade: {self.status.felicidade}"
            )

            stdscr.refresh()

            quadro += 1

            time.sleep(0.5)

            tecla = stdscr.getch()

            if tecla == ord("q"):
                break

        
