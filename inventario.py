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


