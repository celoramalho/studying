class Filme:
    def __init__(self, nome, ano, duracao, likes):
        self.nome = nome.capitalize()
        self.ano = ano
        self.duracao = duracao
        self.likes = likes


class Serie:
    def __init__(self, nome, ano, temporadas, likes):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.like = likes


vingadores = Filme("vingadores - guerra infinita", 2018, 160, 100)

print( f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}")

atlanta = Serie("atlanta", 2018, 2, 75)
print(
    f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}"
)  # print(atlanta.nome)
