from typing import Dict  # Primeiro: Biblioteca padrao do Python
from fastapi import FastAPI  # Segundo: Biblioteca de terceiros
from app.routers import routers_produtos, routers_usuarios  # Terceiro: Biblioteca interna / importação local

# Python Enhancement Proposal 8 https://peps.python.org/pep-0008/

# Tipar fortemente
MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"

# Criando o App
app = FastAPI()

app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)
# Iniciando o servidor


@app.get("/")
def home() -> Dict[str, str]:
    global MENSAGEM_HOME
    return {"mensagem": MENSAGEM_HOME}
