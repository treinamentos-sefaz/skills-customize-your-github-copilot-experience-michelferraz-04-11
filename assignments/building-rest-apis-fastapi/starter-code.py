from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API de Tarefas")


class TarefaCreate(BaseModel):
    titulo: str = Field(min_length=3, description="Titulo da tarefa")


class TarefaUpdateStatus(BaseModel):
    concluida: bool


tarefas = [
    {"id": 1, "titulo": "Estudar FastAPI", "concluida": False},
    {"id": 2, "titulo": "Criar endpoint de tarefas", "concluida": False},
]


@app.get("/health")
def health_check():
    return {"status": "ok", "mensagem": "API online"}


@app.get("/tasks")
def listar_tarefas():
    return {"tarefas": tarefas}


@app.post("/tasks")
def criar_tarefa(payload: TarefaCreate):
    # TODO: Gerar um novo id incremental e adicionar a tarefa na lista.
    # TODO: Retornar a tarefa criada com status HTTP adequado.
    raise NotImplementedError("Implemente a criacao de tarefas")


@app.patch("/tasks/{task_id}")
def atualizar_status_tarefa(task_id: int, payload: TarefaUpdateStatus):
    # TODO: Encontrar a tarefa pelo id e atualizar o campo 'concluida'.
    # TODO: Se nao encontrar, retornar 404 com mensagem em portugues.
    raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
