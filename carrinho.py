class Carrinho:
    def __init__(self):
        self.lista_carrinho = []
    
    def adiciona_produto(self, produto):
        self.lista_carrinho.append(produto)
    
    def mostrar_lista(self):
        for produto in self.lista_carrinho:
            print(produto.nome, produto.preco)
    
    def soma_produtos(self):
        soma = 0
        for produto in self.lista_carrinho:
            soma += produto.preco
        return soma


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

