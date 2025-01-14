from flask import Flask, render_template


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route("/inicio")
def ola():
    jogo1 = Jogo("Tetris", "Puzzle", "Atari")
    jogo2 = Jogo("God of War", "Rack n Slash", "PS2")
    jogo3 = Jogo("Journey", "Aventura", "PS3")

    lista_jogos = [jogo1, jogo2, jogo3]
    return render_template("lista.html", titulo="Jogos", jogos=lista_jogos)

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo="Novo Jogo")


app.run()


# In dev -> app.run(host='0.0.0.0', port=8080) Don't use this definitions in prod

"""
Tipos de Delimitadores do Jinja2:
{%....%}: usado para inserir estruturas Python dentro de um arquivo html;
{{....}}: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
{#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML.
"""
