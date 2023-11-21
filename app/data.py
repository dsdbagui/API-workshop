from typing import List, Dict


class Produtos:
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

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagem": "Produto não encontrado"}

    def adicionar_produto(self, produto: produtos):
        self.produtos.append(produto)
        return produto