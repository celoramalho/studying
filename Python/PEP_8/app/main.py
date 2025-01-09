from typing import Dict
from fastapi import FastAPI
from app.routers import routers_produtos, routers_usuarios


# Python Enhancement Proposal 8 https://peps.python.org/pep-0008/
#snake_case: usado para nomes de variáveis, funções e métodos;
#PascalCase: utilizado para nomes de classes;
#SCREAMING_SNAKE_CASE: reservado para constantes.
#Tipar fortemente

MENSAGEM_HOME: str    ="Bem-vindo à API de Recomendação de Produtos"

# Criando o App
app = FastAPI()

app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)
# Iniciando o servidor

@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}