class ProgramaDeTV:  # Base class (parent class) for TV programs
    def __init__(self, nome, ano):
        self._nome = nome.title()  # Protected attribute (single underscore indicates it's meant for internal use)
        self.ano = ano  # Public attribute
        self._likes = 0  # Protected attribute for tracking likes

    # Getter for the 'nome' attribute
    @property
    def nome(self):
        return self._nome

    # Setter for the 'nome' attribute, ensuring the name is always titled
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # Getter for the 'likes' attribute
    @property
    def likes(self):
        return self._likes

    # Method to increment the number of likes
    def dar_like(self):
        self._likes += 1


# Subclass (child class) for movies, inheriting from ProgramaDeTV
class Filme(ProgramaDeTV):
    def __init__(self, nome, ano, duracao):
        # Call the parent class constructor using super()
        # 'super()' allows the child class to call methods from the parent class
        super().__init__(nome, ano)
        # Adds an additional attribute specific to movies
        self.duracao = duracao  # Extends functionality with a new attribute


# Subclass (child class) for series, inheriting from ProgramaDeTV
class Serie(ProgramaDeTV):
    def __init__(self, nome, ano, temporadas):
        # Call the parent class constructor using super()
        super().__init__(nome, ano)
        # Adds an additional attribute specific to series
        self.temporadas = temporadas  # Extends functionality with a new attribute


# Create an instance of the Filme class
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
# Call the method from the parent class to increment likes
vingadores.dar_like()
print(
    f"{vingadores.nome} - {vingadores.ano} - {vingadores.duracao}min: {vingadores.likes}"
)  # Access attributes and display information about the movie

# Create an instance of the Serie class
atlanta = Serie("atlanta", 2018, 2)
# Call the method from the parent class to increment likes multiple times
atlanta.dar_like()
atlanta.dar_like()
# Uncommenting the line below would update the name of the series using the setter
# atlanta.nome = "atlanta de donald glover"
print(
    f"{atlanta.nome} - {atlanta.ano} - S-{atlanta.temporadas}: {atlanta.likes}"
)  # Display information about the series
