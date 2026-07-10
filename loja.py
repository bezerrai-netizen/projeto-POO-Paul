class Loja:

    def __init__(self):
        self.__estoque = []

    @property
    def estoque(self):
        return self.__estoque

    def adicionar_item(self, item):
        self.__estoque.append(item)

    def remover_item(self, item):
        if item in self.__estoque:
            self.__estoque.remove(item)

    def procurar(self, nome):

        for item in self.__estoque:

            if item.nome.lower() == nome.lower():
                return item

        return None

    def listar(self):

        if not self.__estoque:
            print("\nLoja vazia.")
            return

        print("\n====== LOJA ======")

        for i, item in enumerate(self.__estoque, start=1):
            print(f"{i}. {item.nome} - {item.preco} moedas")

    def vender(self, nome_item, comprador):

        item = self.procurar(nome_item)

        if item is None:
            print("Esse item não existe.")
            return False

        if not comprador.carteira.retirar(item.preco):
            print(f"{comprador.nome} não possui moedas suficientes.")
            return False

        comprador.inventario.adicionar(item)

        self.remover_item(item)

        print(f"{comprador.nome} comprou {item.nome}.")

        return True

    def __len__(self):
        return len(self.__estoque)

    def __iter__(self):
        return iter(self.__estoque)

    def __str__(self):

        return f"Loja com {len(self)} itens."