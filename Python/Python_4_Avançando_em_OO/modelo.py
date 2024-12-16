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

    def __str__(self): # Dunder or magic methods
        return f"{self._nome} - {self.ano} - {self._likes} Likes" 


# Subclass (child class) for movies, inheriting from ProgramaDeTV
class Filme(ProgramaDeTV):
    def __init__(self, nome, ano, duracao):
        # Call the parent class constructor using super()
        # 'super()' allows the child class to call methods from the parent class
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes"


# Subclass (child class) for series, inheriting from ProgramaDeTV
class Serie(ProgramaDeTV):
    def __init__(self, nome, ano, temporadas):
        # Call the parent class constructor using super()
        super().__init__(nome, ano)
        # Adds an additional attribute specific to series
        self.temporadas = temporadas  # Extends functionality with a new attribute

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} seasons - {self._likes} Likes" 

class Playlist(list): #Import list from Python Standard Library
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


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

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana: #Polimorfismo
    print(programa) #Calls __str__

print(f"Tá ou não tá? {demolidor in playlist_fim_de_semana}")
