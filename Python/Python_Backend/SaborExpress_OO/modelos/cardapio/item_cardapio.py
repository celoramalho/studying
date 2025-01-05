from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @abstractmethod
    def aplicar_desconto(self): #Classe abstrata, toda classe filha precisa ter esse método
        pass