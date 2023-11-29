# Importando as bibliotecas

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Criando a class e colocando os atributos do TUDO 
class Tudo(BaseModel):
    tarefa: str
    realizado: bool
    prazo: Optional[date]

db_lista = []
