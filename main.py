from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone top de linha",
        "preco": 1500.00
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um notebook gamer",
        "preco": 3500.00
    },
    {
        "id": 3,
        "nome": "Smart TV",
        "descricao": "Uma smart TV 4K",
        "preco": 2500.00
    }
]

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/") #request
def ola_mundo(): #response
    return {"Olá": "Pessoal"}

