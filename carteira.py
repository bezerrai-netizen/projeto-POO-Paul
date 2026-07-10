class Carteira:

    def __init__(self, saldo=100):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = max(0, valor)

    
    def retirar(self, valor):

        if valor <= self.__saldo:
            self.__saldo -= valor
            return True

        return False

    def __int__(self):
        return self.__saldo
    
    def __iadd__(self, other):
        self.__saldo += other
        return self.__saldo

    def __str__(self):
        return f"{self.__saldo} moedas"