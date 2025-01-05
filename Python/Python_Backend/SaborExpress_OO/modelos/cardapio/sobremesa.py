from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self._descricao = descricao
        self._tipo = tipo
        self._tamanho = tamanho
    
    def __str__(self):
        return f"{self._nome} ({self._tamanho}) - {self._tipo} - {self._descricao} - R$ {self._preco}"

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)