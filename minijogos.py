from abc import ABC, abstractmethod
class Migame(ABC):
    @abstractmethod
    def rodar(self) -> bool:
        pass
    
    def ganha(self, bicho):
        if self.rodar:
            bicho.carteira += 30
            bicho.status.sono += 20

class Jogo_da_cobrinha(Migame):
    def rodar(self):
        return True
        








