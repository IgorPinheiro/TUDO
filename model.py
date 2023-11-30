from datetime import date
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Criando a class e colocando os atributos do TUDO 
class Todo(BaseModel):
    tarefa: str
    realizado: bool
    prazo: Optional[date]

db_lista = []

 # Criando o endpoint inserir dados no db_lista
@app.post('/inserir')
def inserir(todo: Todo):
    try:
        db_lista.append(todo)
        return {'status': 'sucesso'}
    except:
        return {'status': 'error'}

# Crição do endipoint litar as informações do db_lista
@app.post('/listar')
def listar(opcao:  int = 0):

    if opcao == 0:
        return db_lista
    
    elif opcao == 1:
        return list(filter(lambda x: x.realizado == False, db_lista))
    
    elif opcao == 2: 
        return list(filter(lambda x: x.realizado == True, db_lista)) 

# Crição do endipoint listagem de uma unica informação do db_lista    
@app.get('/listagemUnica/{id}')
def listar(id: int):
    try:
        return db_lista[id]
    except:
        return {'status': 'erro'}
# Crição do endipoint alterar status de uma tarefa inserida no db_lista  
@app.post('/alteraStatus')
def alteraStatus(id: int):
    try:
        db_lista[id].realizado = not db_lista[id].realizado
        return {'status': 'sucesso'}
    except:
        {'status': 'erro'}
# exclusão de uma tarefa existente no db_lista
@app.post('/excluir')
def excluir(id: int):
    try:
        del db_lista[id]
        return {'status:' 'excluído sucesso'}
    except:
        return {'status': 'erro'}