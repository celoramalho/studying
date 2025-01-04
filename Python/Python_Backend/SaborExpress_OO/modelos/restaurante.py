class Restaurante:
    restaurantes = [] # atributo de classe
    def __init__(self, nome, categoria): # Construtor
        #Atributos de instância
        self._nome = nome.title() #.upper()
        self._categoria = categoria.title()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    
    
    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria.ljust(20)} | {self.ativo.ljust(20)}'
    
    def listar_restaurantes():
        print('NOME'.ljust(20) + ' | ' + 'CATEGORIA'.ljust(20) + ' | ' + 'STATUS')
        for restaurante in Restaurante.restaurantes:
            print(restaurante)
            
    @property
    def ativo(self):
        return '☑ ativado' if self._ativo else '☒ desativado' #https://coolsymbol.com/
        
    
restaurante_subuai = Restaurante('subuai', 'fast food')
restaurante_osteria = Restaurante('74 Osteria', 'Osteria')


print(Restaurante.listar_restaurantes())






# print(vars(restaurante_subuai))
# {'nome': 'Subuai', 'categoria': 'Fast Food', 'ativo': True}

"""
print(dir(restaurante_subuai))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


"""


#Objeto é uma instância de uma classe, que armazena dados e permite a execução de métodos.

#[<__main__.Restaurante object at 0x7f0f67cd0760>, <__main__.Restaurante object at 0x7f0f67cd0730>] endereço na memoria