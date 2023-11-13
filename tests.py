from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_response():
    response = client.get("/")
    assert response.json() == {"Olá": "Mundo"}

def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_da_lista_de_produto():
    response = client.get("/produtos")
    assert len(response.json()) == 3