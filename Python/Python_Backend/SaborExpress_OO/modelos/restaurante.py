class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria): # Construtor
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
        
    
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)
        
    
restaurante_subuai = Restaurante('Subuai', 'Fast Food')
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