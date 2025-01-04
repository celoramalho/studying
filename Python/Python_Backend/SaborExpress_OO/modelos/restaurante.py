from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = [] # atributo de classe
    def __init__(self, nome, categoria): # Construtor
        #Atributos de instância
        self._nome = nome.title() #.upper()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        
    
    
    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)} | {str(self.media_avaliacoes).ljust(20)} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('NOME'.ljust(20) + ' | ' + 'CATEGORIA'.ljust(20) + ' | '+ 'AVALIAÇÃO'.ljust(20) + ' | ' + 'STATUS')
        for restaurante in cls.restaurantes:
            print(restaurante)
            
    @property
    def ativo(self):
        return '☑ ativado' if self._ativo else '☒ desativado' #https://coolsymbol.com/
        
    def alterar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avalicao = Avaliacao(cliente, nota)
            self._avaliacao.append(avalicao)
    
    @property  
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma_das_notas / len(self._avaliacao), 1)
    
    def adicionar_item_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'\nCardapio do Restaurante {self._nome}')
        for index, item in enumerate(self._cardapio, start=1):
            print(f'{index} - {item}') #print(index, item)
        #if hasattr(self, 'tamanho'):
"""
def adicionar_bebida_no_cardapio(self, bebida):
    self._cardapio.append(bebida)
    
def adicionar_prato_no_cardapio(self, prato):
    self._cardapio.append(prato)
"""

# print(vars(restaurante_subuai))
# {'nome': 'Subuai', 'categoria': 'Fast Food', 'ativo': True}

"""
print(dir(restaurante_subuai))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


"""


#Objeto é uma instância de uma classe, que armazena dados e permite a execução de métodos.

#[<__main__.Restaurante object at 0x7f0f67cd0760>, <__main__.Restaurante object at 0x7f0f67cd0730>] endereço na memoria