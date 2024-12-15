class ProgramaDeTV:
    def __init__(self, nome, ano):
        self._nome = nome.title() #just one underscore to show that it is a private attribute but still let sn class use it whithou name englibng
        self.ano = ano
        self._likes = 0

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


class Filme(ProgramaDeTV):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(ProgramaDeTV):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(
    f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}"
)


atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
#atlanta.nome = "atlanta de donald glover"
print(
    f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}"
)  # print(atlanta.nome)


#Pythonic