from abc import ABC #abstract base class
from collections.abc import MutableSequence
from numbers import Complex
class Playlist(MutableSequence):
    pass

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__(item)


#numero = Numero()
#filmes = Playlist()
#classe abstrata
#Duck typing
#Python data (object) model
#Dunder methods
#Uso de ABCs