class ProgramaDeTV:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 

    # Getter for the 'nome' attribute
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self): 
        # Dunder (Magic) Methods: Special methods in Python that start and end with double underscores. 
        # They allow customization of behavior for built-in operations, like printing (__str__), addition (__add__), etc.
        return f"{self._nome} - {self.ano} - {self._likes} Likes" 


# Subclass (child class) for movies, inheriting from ProgramaDeTV
class Filme(ProgramaDeTV):
    def __init__(self, nome, ano, duracao):
        # Inheritance: A subclass reuses the code of a parent class, inheriting its attributes and methods.
        # 'super()' is used to call the parent class constructor or methods.
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"


# Subclass (child class) for series, inheriting from ProgramaDeTV
class Serie(ProgramaDeTV):
    def __init__(self, nome, ano, temporadas):
        # Calls the parent class constructor using super().
        # This demonstrates reusing code from the parent class while adding new attributes.
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} seasons - {self._likes} Likes" 

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item): 
        # Duck Typing: The class implements __getitem__, allowing the object to behave like an iterable.
        # Python does not require inheritance from a specific class (e.g., list); it only needs the right methods.
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)


vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {playlist_fim_de_semana.tamanho}')

for programa in playlist_fim_de_semana: 
    # Polymorphism: The same interface (e.g., iteration or printing) works for different types (Filme, Serie) seamlessly.
    print(programa) # Calls __str__ (magic method)

print(f"Tá ou não tá? {demolidor in playlist_fim_de_semana}")

"""
Herança de um tipo built-in (nativo)
Vantagens da herança de um iterável
Desvantagem de fazer herança
"""

# Reuse vs. Interface: Reuse focuses on using existing methods and behaviors from a base class.
# Interface focuses on providing a common behavior, even if implemented differently in subclasses.
