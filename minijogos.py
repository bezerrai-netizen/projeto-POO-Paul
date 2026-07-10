from abc import ABC, abstractmethod
class Migame(ABC):
    @abstractmethod
    def rodar(self) -> bool:
        pass
    

class Jogo_da_cobrinha(Migame):
    def rodar(self):
        return True
    
class Jogo_de_desviar(Migame):
    def rodar(self):
        return True

class Spaceinvaders(Migame):
    def rodar(self):
        return True
    


        








