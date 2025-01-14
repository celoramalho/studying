from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("Tetris", "Puzzle", "Atari")
jogo2 = Jogo("God of War", "Rack n Slash", "PS2")
jogo3 = Jogo("Journey", "Aventura", "PS3")

lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("lista.html", titulo="Jogos", jogos=lista_jogos)

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo="Novo Jogo")

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)
    


app.run(debug=True) #debug=True auto reload


# In dev -> app.run(host='0.0.0.0', port=8080) Don't use this definitions in prod

"""
Tipos de Delimitadores do Jinja2:
{%....%}: usado para inserir estruturas Python dentro de um arquivo html;
{{....}}: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
{#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML.
"""
