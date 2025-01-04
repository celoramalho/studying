class Restaurante:
    nome = '' 
    categoria = '' 
    ativo = False
    
restaurante_subuai = Restaurante()
restaurante_subuai.nome = 'Subuai'
restaurante_subuai.categoria = 'Fast Food'
restaurante_subuai.ativo = True

restaurante_pizza = Restaurante()

restaurantes = [restaurante_subuai, restaurante_pizza]

print(restaurante_subuai.ativo)






# print(vars(restaurante_subuai))
# {'nome': 'Subuai', 'categoria': 'Fast Food', 'ativo': True}

"""
print(dir(restaurante_subuai))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


"""


#Objeto é uma instância de uma classe, que armazena dados e permite a execução de métodos.

#[<__main__.Restaurante object at 0x7f0f67cd0760>, <__main__.Restaurante object at 0x7f0f67cd0730>] endereço na memoria